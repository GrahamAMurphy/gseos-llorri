# ------------------------------------------------------------------------
# Custom command support:
#   - fill in APID
#   - pad to even length
#   - detect MAC_DEF and MAC_ENDDEF and automatically fill in macro flag

import GseosIni, GseosBlocks
import GseosDecoder
from GseosCmd import ExecCmd
from HostConstants import CMD_CHANNEL, APID_INSTR
from HostConstants import OP_MAC_DEF, OP_MAC_ENDDEF

class TMyInstrBinCmdDecoderError(Exception): 
    pass

macappend = 0

def fSetMacroMode(s):
  global macappend
  if s=="APPEND":
    macappend = 1
  else:
    macappend = 0

# * B i n C m d D e c o d e r * #
# * Intercept GSEOS commands on command channel CMD_CHANNEL_INSTR_CMD and * #
# * perform the proper command. * #
class TBinCmdDec:
  # * ctor() * #
  # * Initialize all decoder state and register the decoder with the * #
  # * data source requested. * #
  # * Parameters: -
  def __init__(self):
    # - Make sure our blocks are defined properly. - #
    try:
      oBlkSrc = GseosBlocks.Blocks['BinCmd']
      self.oBlkDestCmd = GseosBlocks.Blocks['BIN_CMD_IDP']
    except KeyError, oX:
      raise TMyInstrBinCmdDecoderError("GSEOS block %s is not defined." % oX)

    # - Create the decoder object and install on our source block. - #
    oDec = GseosDecoder.TDecoder('Custom BinCmd for Instrument Cmds Decoder',
		self.fDecoder, [self.oBlkDestCmd])
    # - Hook the decoder to our source block. - #
    oBlkSrc.Decoders.append(oDec)
    # - Record whether we are in 'raw' mode - #
    self.bRawCmdMode = GseosIni.fIsEnabled('Bios', 'RawCmdMode')

  # * fDecoder() * #
  # * Parameters: oBlkSrc: BinCmd block. * #
  def fDecoder(self, oBlkSrc):
    global macappend
    # - CMD_CHANNEL_INSTR_CMD - #
    if oBlkSrc.Channel == CMD_CHANNEL:
      # - Generate INSTR_CMD block - #
      if self.bRawCmdMode:
        self.oBlkDestCmd.Len = oBlkSrc.Len
        self.oBlkDestCmd.Data[:] = oBlkSrc.CmdData[:]
        self.oBlkDestCmd.SendBlock(bCopy=True)
      else:
        if oBlkSrc.CmdData[0] == OP_MAC_ENDDEF:
          macappend = 0
        l = oBlkSrc.Len
        padl = 4*((l+3)/4)
        self.oBlkDestCmd.Len = padl

        ### NOT USED ### self.oBlkDestCmd.ApID = APID_INSTR

        self.oBlkDestCmd.Data[:] = oBlkSrc.CmdData[:]
        for i in range(l, padl):
          self.oBlkDestCmd.Data[i] = 0
        self.oBlkDestCmd.Data[1] = macappend
        self.oBlkDestCmd.SendBlock(bCopy=True)
        if oBlkSrc.CmdData[0] == OP_MAC_DEF:
          macappend = 1

# - Create the BinCmd decoder. - #
_oBinCmdDec = TBinCmdDec()

# - Stop default system decoder. - #
try:
  GseosDecoder.StopDecoder('BinCmd for Instrument Cmds Decoder')
except Exception as e: ## pass
    print "made it here!!", e

# ------------------------------------------------------------------------
# Variable-length Commands

from struct import calcsize, pack, unpack
import GseosBlocks
from HostConstants import OP_CMD_WRAP, OP_CMD_TEXT, OP_MEM_LOAD, OP_MEM_STR_LOAD
from HostConstants import CMD_CHANNEL
from GseosCmd import SendBinCmd

# Command Wrap
def fWrapCommand(opcode, *args):
  count = len(args)
  fmt = '>BBB%dB' % count			# build format string
  str = pack(fmt, OP_CMD_WRAP, 0,		# convert to internal format
			opcode, *args)
  SendBinCmd(CMD_CHANNEL, str)

# Command Text
def fCmdText(text):
  count = min(len(text), 77)			# silently truncate long strings
  fmt = '>BBB%ds' % count			# build format string
  str = pack(fmt, OP_CMD_TEXT, 0,		# convert to internal format
			count, text[:count])
  SendBinCmd(CMD_CHANNEL, str)

# Memory Load
def fMemLoad(addr, *data):
  count = len(data)
  fmt = '>BBLHH%dB' % count			# build format string
  str = pack(fmt, OP_MEM_LOAD, 0,		# convert to internal format
			addr, count, 0, *data)
  SendBinCmd(CMD_CHANNEL, str)

# Memory Structure Load
def fMemStrLoad(id, offset, *data):
  count = len(data)
  fmt = '>BBBBH%dB' % count			# build format string
  str = pack(fmt, OP_MEM_STR_LOAD, 0,		# convert to internal format
			id, count, offset, *data)
  SendBinCmd(CMD_CHANNEL, str)

# ------------------------------------------------------------------------
# General command: CMD

from types import IntType, LongType
from GseosCmd import ExecCmd
from HostConstants import cmdprefix

# Execute given command with arguments supplied.  For most commands,
# this is done by converting the entire command to a text string
# and passing it to ExecCmd for execution.  The exceptions are the
# variable-length commands.  These are intercepted and passed to the
# functions above.
def CMD(name, *args):
  if name==cmdprefix+'_CMD_TEXT':
    fCmdText(*args)
  elif name==cmdprefix+'_CMD_WRAP':
    fWrapCommand(args[0], *args[1:])
  elif name==cmdprefix+'_MEM_LOAD':
    fMemLoad(args[0], *args[1:])
  elif name==cmdprefix+'_MEM_STR_LOAD':
    fMemStrLoad(args[0], args[1], *args[2:])
  else:
    cmdstr = name + '('
    cont = ''
    for arg in args:
      if type(arg) is IntType:
        cmdstr += cont + '%d'%arg
      elif type(arg) is LongType:
        cmdstr += cont + '%dL'%arg		# Note: works without L too!
      else:
        cmdstr += cont + arg
      cont = ',' # TBD: no blank
    cmdstr += ')'
    ExecCmd(cmdstr)

# ---------------------------------------------------------------------------
# File upload - from File Open menu

from struct import unpack
from GseosFileUpload import StartUpload, IsUploadActive
from HostConstants import MAX_MEM_LOAD

# globals
oFile = None				# file descriptor
wCurrAddr = 0				# current memory address

# Start file load
def fOnStart(strFile, ctArgs):
  global oFile
  global wCurrAddr

  wCurrAddr = eval(ctArgs[0])
  oFile = open(strFile, 'rb')
  return True

# Continue file load
def fOnTimer():
  global oFile
  global wCurrAddr

  b = oFile.read(MAX_MEM_LOAD)
  l = len(b)
  if l != 0:
    t = unpack('%dB' % l, b)
    fMemLoad(wCurrAddr, *t)
    wCurrAddr += l
    return True
  else:
    oFile.close()
    return False

# Load file using metered FileUpload, implemented above.
# Note: assumes upload is defined in .ini file by [MemLoad]
def fLoadFile(name, addr):
  StartUpload('MemLoad', name, ["0x%x" % addr])

def fLoadActive():
  return IsUploadActive('MemLoad')

# ---------------------------------------------------------------------------
# ---------------------------------------------------------------------------

# globals
oStrFile = None				# file descriptor
wStrStructure = 0				# current memory address
wStrCurrAddr = 0				# current memory address

# Start str file load
def fOnStartStr(strFile, ctArgs):
  global oStrFile
  global wStrStructure, wStrCurrAddr

  # Also need to update gseos.ini for *.str file type.
  strStructure = ctArgs[0].strip() 
  wStrStructure = { 'IP_MASK':0 } [ strStructure ] 
  wStrCurrAddr = eval(ctArgs[1])
  oStrFile = open(strFile, 'rb')
  return True

# Continue file load
def fOnTimerStr():
  global oStrFile
  global wStrStructure, wStrCurrAddr

  b = oStrFile.read(MAX_MEM_LOAD)
  l = len(b)
  ## print 'wStrCurrAddr: ', wStrCurrAddr
  if l != 0:
    t = unpack('%dB' % l, b)
    fMemStrLoad(wStrStructure, wStrCurrAddr, *t)
    wStrCurrAddr += l
    return True
  else:
    oStrFile.close()
    return False

def fStrLoadActive():
  return IsUploadActive('StrLoad')
# ---------------------------------------------------------------------------

# ---------------------------------------------------------------------------
# Time

def fSetTime(t):
  ExecCmd('GSEOS_CMD_SET_TIME(%u,0)' % t)
