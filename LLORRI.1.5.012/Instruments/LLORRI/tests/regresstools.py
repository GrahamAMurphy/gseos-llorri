# (c) 2003 Johns Hopkins University / Applied Physics Laboratory
# by John R. Hayes
from __main__ import *

# ------------------------------------------------------------------------
# Select instrument

# instr = 'MDS'; cmdprefix = instr; host = 'MESS'
# instr = 'MAG'; cmdprefix = instr; host = 'MESS'
# instr = 'NUS'; cmdprefix = instr; host = 'MESS'
# instr = 'LOR'; cmdprefix = instr; host = 'NH'
# instr = 'PEP'; cmdprefix = instr; host = 'NH'
# instr = 'VSL'; cmdprefix = instr; host = 'NH'
# instr = 'ATAS'; cmdprefix = instr; host = 'NH'
# instr = 'CRM'; cmdprefix = instr; host = 'MRO'
from HostConstants import host, instr, cmdprefix

host = 'Lucy'
instr = 'LOR'
cmdprefix = 'LOR'

# ------------------------------------------------------------------------
# Common functions here
# These can be overridden by host-specific things later

def fMemLoadEcho(addr, len, b0, b1):
  return [(addr>>24)&0xff, (addr>>16)&0xff, (addr>>8)&0xff, addr&0xff,
          (len>>8)&0xff, len&0xff,
          0, 0,
          b0, b1]

def fMemReadEcho(addr, len):
  return [(addr>>24)&0xff, (addr>>16)&0xff, (addr>>8)&0xff, addr&0xff,
          0, 0,
          (len>>8)&0xff, len&0xff]

# ------------------------------------------------------------------------
# MESSENGER-specific things here

if host == 'MESS':
  # use GSEOS 5.2; emulate 6.0
  from Monitor import Monitor as TMonitor
  from Sequencer import Sequencer as TSequencer, \
    TimeoutError as TSeqTimeoutError
  from core.core import CMD
  from Common.MET import SetMET
  from Common.config import fSetMacroMode

  dDests = {
	'MDS' : 0x06,
	'EPP' : 0x08,
	'GRS' : 0x09,
	'NUS' : 0x0a,
	'MAG' : 0x0b,
	'XRS' : 0x0c,
	'MASCS' : 0x0d
}

  dOpcodes = {
	'CMD_NULL' : 0x02,
	'CMD_WRAP' : 0x03,
	'MAC_CHECK' : 0x11,
	'MAC_DEF' : 0x10,
	'MAC_DELAY' : 0x11,
	'MAC_END' : 0x12,
	'MAC_ENDDEF' : 0x13,
	'MAC_HALT' : 0x14,
	'MAC_LOOP_BEGIN' : 0x18,
	'MAC_LOOP_END' : 0x19,
	'MAC_NEST' : 0x15,
	'MAC_PAUSE' : 0x16,
	'MAC_READ' : 0x25,
	'MAC_RESTORE' : 0x1c,
	'MAC_RUN' : 0x17,
	'MAC_RUN_SILENT' : 0x1f,
	'MAC_SAVE' : 0x1b,
	'MEM_CHECK' : 0x04,
	'MEM_COPY' : 0x05,
	'MEM_LOAD' : 0x06,
	'MEM_READ' : 0x07,
	'MEM_READ_ABRT' : 0x08,
	'MEM_READ_INT' : 0x24,
	'MEM_RUN' : 0x09,
	'MEM_STR_LOAD' : 0x0a,
	'MEM_STR_READ' : 0x0b,
	'MEM_WR_EN' : 0x23,
	'MON_CNTRL' : 0x0c,
	'PWR_OFF' : 0x20,
	'ROM_BOOT' : 0x0e,
	'ROM_GO' : 0x0f,
	'SAFE' : 0x1d,
	'SHUTDOWN' : 0x1e,
	'SOFT_RESET' : 0x22,
	'STAT_CLR' : 0x01,		# named COUNTER_CLR on MESSENGER
	'STAT_INT' : 0x0d,
	'STAT_MEM' : 0x21
  }

  dTrueNames = {
	'STAT_CLR' : 'COUNTER_CLR'
  }

  # Arguments: map to values
  enable=1					# Enable/Disable
  disable=0
  cmdexec=0					# Counters
  cmdrej=1
  maccmdexec=2
  maccmdrej=3
  telvol=4
  all=255

  # Programs to use in file load tests, etc.
  tstpg = 0x6
  testname = '/jrh/counts.mem'			# test pattern
  testlen = 8192; testsum = 0xf808
  progname = '/jrh/messfor.mem'
  proglen = 6150; progsum = 0x8a02
  progstart = 0x042a
  eeprogname = '/jrh/messfore.mem'
  eeproglen = 6155; eeprogsum = 0x8269
  eeprogpg = 0xa

  def fSetTime(t):
    SetMET(t)

  def fPktSeqNums(block):
    return (block.SeqCount, block.MET)

  def fPktSeqNext(seq, time, interval):
    return (seq+1, time+interval)

  def fPktDataLen(blk):
    return blk.Length + 1 - 4

  def fLoadFile(path, addr):
    core.loadFile.fLOAD_FILE(path, instr, addr)

  def fPktLenOk(blk, len):			# no padding
    return fPktDataLen(blk) == len

# ------------------------------------------------------------------------
# LORRI/PEPSSI-specific things here

if host == 'NH':
  # use GSEOS 5.2; emulate 6.0
  from Monitor import Monitor as TMonitor
  from Sequencer import Sequencer as TSequencer, \
    TimeoutError as TSeqTimeoutError
  from common.core import CMD
  from sceAPI import SetMET
  from common.config import fSetMacroMode

  dOpcodes = {
	'CMD_NULL' : 0x01,
	'CMD_WRAP' : 0x02,
	'MAC_CHECK' : 0x03,
	'MAC_DEF' : 0x04,
	'MAC_DELAY' : 0x05,
	'MAC_END' : 0x06,
	'MAC_ENDDEF' : 0x07,
	'MAC_HALT' : 0x08,
	'MAC_LOOP_BEGIN' : 0x09,
	'MAC_LOOP_END' : 0x0a,
	'MAC_NEST' : 0x0b,
	'MAC_PAUSE' : 0x0c,
	'MAC_READ' : 0x0d,
	'MAC_RESTORE' : 0x0e,
	'MAC_RUN' : 0x0f,
	'MAC_RUN_SILENT' : 0x10,
	'MAC_SAVE' : 0x11,
	'MEM_CHECK' : 0x12,
	'MEM_COPY' : 0x13,
	'MEM_LOAD' : 0x14,
	'MEM_READ' : 0x15,
	'MEM_READ_ABRT' : 0x16,
	'MEM_RUN' : 0x17,
	'MEM_STR_LOAD' : 0x18,
	'MEM_STR_READ' : 0x19,
	'MEM_WR_EN' : 0x1a,
	'MON_CNTRL' : 0x1b,
	'PWR_OFF' : 0x1c,
	'ROM_BOOT' : 0x23,
	'ROM_GO' : 0x24,
	'SAFE' : 0x1d,
	'SHUTDOWN' : 0x1e,
	'SOFT_RESET' : 0x1f,
	'STAT_CLR' : 0x20,
	'STAT_INT' : 0x21,
	'STAT_MEM' : 0x22
  }

  dTrueNames = {
  # none ...
  }

  # Arguments: map to values
  enable=1					# Enable/Disable
  disable=0
  cmdexec=0					# Counters
  cmdrej=1
  maccmdexec=2
  maccmdrej=3
  telvol=4
  all=255

  # Programs to use in file load tests, etc.
  tstpg = 0x6
  testname = '/jrh/counts.mem'			# test pattern
  testlen = 8192; testsum = 0xf808
  progname = '/jrh/messfor.mem'
  proglen = 6150; progsum = 0x8a02
  progstart = 0x042a
  eeprogname = '/jrh/messfore.mem'
  eeproglen = 6155; eeprogsum = 0x8269
  eeprogpg = 0xa

  def fSetTime(t):
    SetMET(t)

  def fPktSeqNums(block):
    return (block.SeqCount, block.MET)

  def fPktSeqNext(seq, time, interval):
    return (seq+1, time+interval)

  def fPktDataLen(blk):
    return blk.Length + 1 - 4

  if instr == 'LOR':
    fLoadFile = i_LORRI.lor_com_cmds.fLOR_LOAD_FILE
  elif instr == 'VSL':
    fLoadFile = i_VSLIT.vsl_com_cmds.fVSL_LOAD_FILE
  elif instr == 'ATAS':
    fLoadFile = i_ATAS.atas_com_cmds.fATAS_LOAD_FILE
  else:
    fLoadFile = i_PEPSSI.pep_com_cmds.fPEP_LOAD_FILE

  def fPktLenOk(blk, len):			# no padding
    return fPktDataLen(blk) == len

# ------------------------------------------------------------------------
# CRISM-specific things here

if host == 'MRO':
  # use GSEOS 5.2; emulate 6.0
  from Monitor import Monitor as TMonitor
  from Sequencer import Sequencer as TSequencer, \
    TimeoutError as TSeqTimeoutError
  from core.core import CMD
  from core.CRMTiming import fSetTime
  from common.config import fSetMacroMode

  dOpcodes = {
	'CMD_NULL' : 0x01,
	'CMD_WRAP' : 0x02,
	'MAC_CHECK' : 0x03,
	'MAC_DEF' : 0x04,
	'MAC_DELAY' : 0x05,
	'MAC_END' : 0x06,
	'MAC_ENDDEF' : 0x07,
	'MAC_HALT' : 0x08,
	'MAC_LOOP_BEGIN' : 0x09,		# MAC_LOOP_BEG on CRISM
	'MAC_LOOP_END' : 0x0a,
	'MAC_NEST' : 0x0b,
	'MAC_PAUSE' : 0x0c,
	'MAC_READ' : 0x0d,
	'MAC_RESTORE' : 0x0e,
	'MAC_RUN' : 0x0f,
	'MAC_RUN_SILENT' : 0x10,		# MAC_RUN_SIL on CRISM
	'MAC_SAVE' : 0x11,
	'MEM_CHECK' : 0x12,
	'MEM_COPY' : 0x13,
	'MEM_LOAD' : 0x14,
	'MEM_READ' : 0x15,
	'MEM_READ_ABRT' : 0x16,
	'MEM_RUN' : 0x17,
	'MEM_STR_LOAD' : 0x18,
	'MEM_STR_READ' : 0x19,
	'MEM_WR_EN' : 0x1a,
	'MON_CNTRL' : 0x1b,
	'ROM_BOOT' : 0x1e,
	'ROM_GO' : 0x1f,
	'STAT_CLR' : 0x1c,
	'STAT_INT' : 0x1d,
	'STAT_MEM' : 0x20,
  }

  dTrueNames = {
	'MAC_LOOP_BEGIN' : 'MAC_LOOP_BEG',
	'MAC_RUN_SILENT' : 'MAC_RUN_SIL'
  }

  # Arguments: map to values
  enable=1					# Enable/Disable
  disable=0
  cmdexec=0					# Counters
  cmdrej=1
  maccmdexec=2
  maccmdrej=3
  telvol=4
  all=255

  # Programs to use in file load tests, etc.
  tstpg = 0x6
  testname = '/jrh/counts.mem'			# test pattern
  testlen = 8192; testsum = 0xf808
  progname = '/jrh/messfor.mem'
  proglen = 6150; progsum = 0x8a02
  progstart = 0x042a
  eeprogname = '/jrh/messfore.mem'
  eeproglen = 6155; eeprogsum = 0x8269
  eeprogpg = 0xa

  def fPktSeqNums(block):
    return (0, block.Time_Tag)

  def fPktSeqNext(seq, time, interval):
    return (0, time+interval)

  def fPktDataLen(blk):
    return blk.Length + 1

  fLoadFile = core.loadFile.fLOAD_FILE

  def fPktLenOk(blk, len):			# no padding
    return fPktDataLen(blk) == len

# ------------------------------------------------------------------------
# Puck-specific things here

if (host == 'Juno') or (host == 'RBSP') or (host == 'MMS'):
  # use GSEOS 6.0
  from GseosMonitor import TMonitor
  from GseosSequencer import TSequencer, TSeqTimeoutError
  from HostCommands import fSetMacroMode, fSetTime
  from PuckCommands import CMD, fLoadFile

  dOpcodes = {
	'CMD_NULL' : 0x01,
	'CMD_WRAP' : 0x02,
	'MAC_CHECK' : 0x03,
	'MAC_DEF' : 0x04,
	'MAC_DELAY' : 0x05,
	'MAC_END' : 0x06,
	'MAC_ENDDEF' : 0x07,
	'MAC_HALT' : 0x08,
	'MAC_LOOP_BEGIN' : 0x09,
	'MAC_LOOP_END' : 0x0a,
	'MAC_NEST' : 0x0b,
	'MAC_PAUSE' : 0x0c,
	'MAC_READ' : 0x0d,
	'MAC_RESTORE' : 0x0e,
	'MAC_RUN' : 0x0f,
	'MAC_RUN_SILENT' : 0x10,
	'MAC_SAVE' : 0x11,
	'MEM_CHECK' : 0x12,
	'MEM_COPY' : 0x13,
	'MEM_LOAD' : 0x14,
	'MEM_READ' : 0x15,
	'MEM_READ_ABRT' : 0x16,
	'MEM_RUN' : 0x17,
	'MEM_STR_LOAD' : 0x18,
	'MEM_STR_READ' : 0x19,
	'MEM_WR_EN' : 0x1a,
	'MON_CNTRL' : 0x1b,
	'ROM_BOOT' : 0x1e,
	'ROM_GO' : 0x1f,
	'SAF_OFF' : 0x22,
	'SAF_RESET' : 0x23,
	'SAF_TIMEOUT' : 0x24,
	'STAT_CLR' : 0x1c,
	'STAT_INT' : 0x1d,
	'STAT_MEM' : 0x20,
  }

  dTrueNames = {
	'MAC_LOOP_BEGIN' : 'MAC_LOOP_BEG',
	'MAC_RUN_SILENT' : 'MAC_RUN_SIL',
	'MEM_READ_ABRT'  : 'MEM_READ_ABT'
  }

  # Arguments: map to strings
  enable='Enable'				# Enable/Disable
  disable='Disable'
  cmdexec='CmdExec'				# Counters
  cmdrej='CmdRej'
  maccmdexec='MacCmdExec'
  maccmdrej='MacCmdRej'
  telvol='TelVol'
  all='All'

  # Programs to use in file load tests, etc.
  tstpg = 0xf
  testname = '/jrh/counts.mem'			# test pattern
  testlen = 8192; testsum = 0xf808
  progname = '/jrh/puckfor.mem'
  proglen = 5217; progsum = 0x41da
  progstart = 0x0210
  eeprogname = '/jrh/puckfore.mem'
  eeproglen = 5222; eeprogsum = 0xee7b
  eeprogpg = 0x1b

  # Ignore sequence numbers.  Juno doesn't have them.  On MMS,
  # they are lost after packet re-assembly.  For all, the numbers
  # are not put in the decoded blocks.
  def fPktSeqNums(block):
    return (0, block.TimeTag)

  def fPktSeqNext(seq, time, interval):
    return (0, time+interval)

  def fPktDataLen(blk):
    return blk.Length

  # host-specific things here ...
  if (host == 'MMS') or (host == 'Juno'):	# MMs padding is variable
    def fPktLenOk(blk, len):			# Juno length is known, but
      return fPktDataLen(blk) >= len		#   MEM_STR_LOAD command is padded
  else:						# RBSP pads to even
    def fPktLenOk(blk, len):
      l = len
      if l%2 == 1:
        l += 1
      return fPktDataLen(blk) == l
  #else:					# Juno length is known
  #  def fPktLenOk(blk, len):
  #    return fPktDataLen(blk) == len

  # TBD: experiment; maybe move to PuckCommands?
  # Replace fLoadFile
  if (host == 'MMS'):
    from GseosFileUpload import StartUpload
    def fLoadFile(name, addr):
      StartUpload('MemLoad', name, ["%d" % addr])

# ------------------------------------------------------------------------
# Strofio-specific things here

if host=='BepiColombo':
  # use GSEOS 6.0
  from GseosMonitor import TMonitor
  from GseosSequencer import TSequencer, TSeqTimeoutError
  from HostCommands import fSetMacroMode, fSetTime
  from HostCommands import CMD, fLoadFile

  dOpcodes = {
	'CMD_ECHO' : 164,
	'CMD_NULL' : 0x80,
	'CMD_WRAP' : 0x82,
	'MAC_CHECK' : 0x83,
	'MAC_DEF' : 0x84,
	'MAC_DELAY' : 0x85,
	'MAC_END' : 0x86,
	'MAC_ENDDEF' : 0x87,
	'MAC_HALT' : 0x88,
	'MAC_LOOP_BEGIN' : 0x89,
	'MAC_LOOP_END' : 0x8a,
	'MAC_NEST' : 0x8b,
	'MAC_PAUSE' : 0x8c,
	'MAC_READ' : 0x8d,
	'MAC_RESTORE' : 0x8e,
	'MAC_RUN' : 0x8f,
	'MAC_RUN_SILENT' : 0x90,
	'MAC_SAVE' : 0x91,
	'MEM_CHECK' : 0x92,
	'MEM_COPY' : 0x93,
	'MEM_LOAD' : 0x94,
	'MEM_READ' : 0x95,
	'MEM_READ_ABRT' : 0x96,
	'MEM_RUN' : 0x97,
	'MEM_STR_LOAD' : 0x98,
	'MEM_STR_READ' : 0x99,
	'MEM_WR_EN' : 0x9a,
	'MON_CNTRL' : 0x9b,
	'ROM_BOOT' : 0x9c,
	'ROM_GO' : 0x9d,
	'SAF_OFF' : 0x9e,
	'SAF_RESET' : 0x9f,
	'SAF_TIMEOUT' : 0xa0,
	'STAT_CLR' : 0xa1,
	'STAT_INT' : 0xa2,
	'STAT_MEM' : 0xa3,
  }

  dTrueNames = {
  # none ...
  }

  # Arguments: map to strings
  enable='Enable'				# Enable/Disable
  disable='Disable'
  cmdexec='CmdExec'				# Counters
  cmdrej='CmdRej'
  maccmdexec='MacCmdExec'
  maccmdrej='MacCmdRej'
  telvol='TelVol'
  all='All'

  # Programs to use in file load tests, etc.
  # Note: MEM_CHECK uses byte lengths.
  tstpg = 0x6					# EM board missing pages 8-f
  testname = 'Instruments/Strofio/test-loads/counts.mem'	# test pattern
  testlen = 2*8192; testsum = 0xf808
  progname = 'Instruments/Strofio/test-loads/strofor.mem'	# program for RAM
  proglen = 10404; progsum = 0x04fe
  progstart = 0x0210
  eeprogname = 'Instruments/Strofio/test-loads/strofore.mem'	# program for EEPROM
  eeproglen = 10414; eeprogsum = 0xfc94
  eeprogpg = 0x1b

  def fPktSeqNums(block):
    return (0, block.TimeTag)

  def fPktSeqNext(seq, time, interval):
    return (0, time+interval)

  def fPktDataLen(blk):
    return blk.Length

  # host-specific things here ...
  def fPktLenOk(blk, len):			# Strofio pads to even
    l = len
    if l%2 == 1:
      l += 1
    return fPktDataLen(blk) == l

  def fMemLoadEcho(addr, len, b0, b1):
    return [0, 0,
            (addr>>24)&0xff, (addr>>16)&0xff, (addr>>8)&0xff, addr&0xff,
            0, 0,
            (len>>8)&0xff, len&0xff]

  def fMemReadEcho(addr, len):
    return [0, 0,
            (addr>>24)&0xff, (addr>>16)&0xff, (addr>>8)&0xff, addr&0xff,
            0, 0,
            (len>>8)&0xff, len&0xff]

# ------------------------------------------------------------------------
# SIS-specific things here

if host=='SolarOrbiter':
  # use GSEOS 7.0
  from GseosMonitor import TMonitor
  from GseosSequencer import TSequencer, TSeqTimeoutError
  from HostCommands import fSetMacroMode, fSetTime
  from HostCommands import CMD, fLoadFile

  dOpcodes = {
	'CMD_ECHO' : 164,
	'CMD_NULL' : 0x80,
	'CMD_WRAP' : 0x82,
	'MAC_CHECK' : 0x83,
	'MAC_DEF' : 0x84,
	'MAC_DELAY' : 0x85,
	'MAC_END' : 0x86,
	'MAC_ENDDEF' : 0x87,
	'MAC_HALT' : 0x88,
	'MAC_LOOP_BEGIN' : 0x89,
	'MAC_LOOP_END' : 0x8a,
	'MAC_NEST' : 0x8b,
	'MAC_PAUSE' : 0x8c,
	'MAC_READ' : 0x8d,
	'MAC_RESTORE' : 0x8e,
	'MAC_RUN' : 0x8f,
	'MAC_RUN_SILENT' : 0x90,
	'MAC_SAVE' : 0x91,
	'MEM_CHECK' : 0x92,
	'MEM_COPY' : 0x93,
	'MEM_LOAD' : 0x94,
	'MEM_READ' : 0x95,
	'MEM_READ_ABRT' : 0x96,
	'MEM_RUN' : 0x97,
	'MEM_STR_LOAD' : 0x98,
	'MEM_STR_READ' : 0x99,
	'MEM_WR_EN' : 0x9a,
	'MON_CNTRL' : 0x9b,
	'ROM_BOOT' : 0x9c,
	'ROM_GO' : 0x9d,
	'SAF_OFF' : 0x9e,
	'SAF_RESET' : 0x9f,
	'SAF_TIMEOUT' : 0xa0,
	'STAT_CLR' : 0xa1,
	'STAT_INT' : 0xa2,
	'STAT_MEM' : 0xa3,
  }

  dTrueNames = {
  # none ...
  }

  # Arguments: map to strings
  enable='Enable'				# Enable/Disable
  disable='Disable'
  cmdexec='CmdExec'				# Counters
  cmdrej='CmdRej'
  maccmdexec='MacCmdExec'
  maccmdrej='MacCmdRej'
  telvol='TelVol'
  all='All'

  # Programs to use in file load tests, etc.
  # Note: MEM_CHECK uses byte lengths.
  tstpg = 0x6					# EM board missing pages 8-f
  testname = 'Instruments/SIS/test-loads/counts.mem'	# test pattern
  testlen = 2*8192; testsum = 0xf808
  progname = 'Instruments/SIS/test-loads/com1for.mem'	# program for RAM
  proglen = 10404; progsum = 0x2d74
  progstart = 0x0210
  eeprogname = 'Instruments/SIS/test-loads/com1fore.mem'# program for EEPROM
  eeproglen = 10414; eeprogsum = 0xc746
  eeprogpg = 0x1b

  def fPktSeqNums(block):
    return (0, block.TimeTag)

  def fPktSeqNext(seq, time, interval):
    return (0, time+interval)

  def fPktDataLen(blk):
    return blk.Length

  # host-specific things here ...
  def fPktLenOk(blk, len):			# Strofio pads to even
    l = len
    if l%2 == 1:
      l += 1
    return fPktDataLen(blk) == l

  def fMemLoadEcho(addr, len, b0, b1):
    return [0, 0,
            (addr>>24)&0xff, (addr>>16)&0xff, (addr>>8)&0xff, addr&0xff,
            0, 0,
            (len>>8)&0xff, len&0xff]

  def fMemReadEcho(addr, len):
    return [0, 0,
            (addr>>24)&0xff, (addr>>16)&0xff, (addr>>8)&0xff, addr&0xff,
            0, 0,
            (len>>8)&0xff, len&0xff]

# ------------------------------------------------------------------------
# SSUSI-specific things here
# TBD: SSUSI's spacecraft is TBD; make it like RBSP for now
# TBD copy of Puck; hacking in progress

if (host == 'SSUSI'):
  # use GSEOS 6.0
  from GseosMonitor import TMonitor
  from GseosSequencer import TSequencer, TSeqTimeoutError
  from HostCommands import fSetMacroMode, fSetTime
  from HostCommands import CMD, fLoadFile

  dOpcodes = {
	'CMD_NULL' : 0x01,
	'CMD_WRAP' : 0x02,
	'MAC_CHECK' : 0x03,
	'MAC_DEF' : 0x04,
	'MAC_DELAY' : 0x05,
	'MAC_END' : 0x06,
	'MAC_ENDDEF' : 0x07,
	'MAC_HALT' : 0x08,
	'MAC_LOOP_BEGIN' : 0x09,
	'MAC_LOOP_END' : 0x0a,
	'MAC_NEST' : 0x0b,
	'MAC_PAUSE' : 0x0c,
	'MAC_READ' : 0x0d,
	'MAC_RESTORE' : 0x0e,
	'MAC_RUN' : 0x0f,
	'MAC_RUN_SILENT' : 0x10,
	'MAC_SAVE' : 0x11,
	'MEM_CHECK' : 0x12,
	'MEM_COPY' : 0x13,
	'MEM_LOAD' : 0x14,
	'MEM_READ' : 0x15,
	'MEM_READ_ABRT' : 0x16,
	'MEM_RUN' : 0x17,
	'MEM_STR_LOAD' : 0x18,
	'MEM_STR_READ' : 0x19,
	'MEM_WR_EN' : 0x1a,
	'MON_CNTRL' : 0x1b,
	'ROM_BOOT' : 0x1e,
	'ROM_GO' : 0x1f,
	'SAF_OFF' : 0x22,
	'SAF_RESET' : 0x23,
	'SAF_TIMEOUT' : 0x24,
	'STAT_CLR' : 0x1c,
	'STAT_INT' : 0x1d,
	'STAT_MEM' : 0x20,
  }

  dTrueNames = {
# TBD: Juno limitation
	'MAC_LOOP_BEGIN' : 'MAC_LOOP_BEG',
	'MAC_RUN_SILENT' : 'MAC_RUN_SIL',
	'MEM_READ_ABRT'  : 'MEM_READ_ABT'
  }

  # Arguments: map to strings
  enable='Enable'				# Enable/Disable
  disable='Disable'
  cmdexec='CmdExec'				# Counters
  cmdrej='CmdRej'
  maccmdexec='MacCmdExec'
  maccmdrej='MacCmdRej'
  telvol='TelVol'
  all='All'

  # Programs to use in file load tests, etc.
# TBD update
  tstpg = 0xf
  testname = '/jrh/counts.mem'			# test pattern
  testlen = 8192; testsum = 0xf808
  progname = '/jrh/puckfor.mem'
  proglen = 5217; progsum = 0x41da
  progstart = 0x0210
  eeprogname = '/jrh/puckfore.mem'
  eeproglen = 5222; eeprogsum = 0xee7b
  eeprogpg = 0x1b

  # Ignore sequence numbers.  Juno doesn't have them.  On MMS,
  # they are lost after packet re-assembly.  For all, the numbers
  # are not put in the decoded blocks.
  def fPktSeqNums(block):
    return (0, block.TimeTag)

  def fPktSeqNext(seq, time, interval):
    return (0, time+interval)

  def fPktDataLen(blk):
    return blk.Length

  def fPktLenOk(blk, len):			# pad to even
    l = len
    if l%2 == 1:
      l += 1
    return fPktDataLen(blk) == l

# ------------------------------------------------------------------------
# SPP-specific things here

if host=='SPP':
  # use GSEOS 7.0
  from GseosMonitor import TMonitor
  from GseosSequencer import TSequencer, TSeqTimeoutError
  from HostCommands import fSetMacroMode, fSetTime
  from HostCommands import CMD, fLoadFile
  from HostConstants import instrdir

  dOpcodes = {
	'CMD_NULL' : 0x01,
	'CMD_WRAP' : 0x02,
	'MAC_CHECK' : 0x03,
	'MAC_DEF' : 0x04,
	'MAC_DELAY' : 0x05,
	'MAC_END' : 0x06,
	'MAC_ENDDEF' : 0x07,
	'MAC_HALT' : 0x08,
	'MAC_LOOP_BEGIN' : 0x09,
	'MAC_LOOP_END' : 0x0a,
	'MAC_NEST' : 0x0b,
	'MAC_PAUSE' : 0x0c,
	'MAC_READ' : 0x0d,
	'MAC_RESTORE' : 0x0e,
	'MAC_RUN' : 0x0f,
	'MAC_RUN_SILENT' : 0x10,
	'MAC_SAVE' : 0x11,
	'MEM_CHECK' : 0x12,
	'MEM_COPY' : 0x13,
	'MEM_LOAD' : 0x14,
	'MEM_NV_ENB' : 0x26,
	'MEM_READ' : 0x15,
	'MEM_READ_ABRT' : 0x16,
	'MEM_RUN' : 0x17,
	'MEM_STR_LOAD' : 0x18,
	'MEM_STR_READ' : 0x19,
	'MEM_WR_EN' : 0x1a,
	'MON_CNTRL' : 0x1b,
	'ROM_BOOT' : 0x1e,
	'ROM_GO' : 0x1f,
	'SAF_CYCLE' : 0x25,
	'SAF_OFF' : 0x22,
	'SAF_RESET' : 0x23,
	'SAF_TIMEOUT' : 0x24,
	'STAT_CLR' : 0x1c,
	'STAT_INT' : 0x1d,
	'STAT_MEM' : 0x20,
  }

  dTrueNames = {
  # none ...
  }

  # Arguments: map to strings
  enable='Enable'				# Enable/Disable
  disable='Disable'
  cmdexec='CmdExec'				# Counters
  cmdrej='CmdRej'
  maccmdexec='MacCmdExec'
  maccmdrej='MacCmdRej'
  telvol='TelVol'
  all='All'

  # Programs to use in file load tests, etc.
  tstpg = 0xf
  testname = 'Instruments/' + instrdir + '/test-loads/counts.mem'	# test pattern
  testlen = 8192; testsum = 0xf808
  progname = 'Instruments/' + instrdir + '/test-loads/com1for.mem'	# program for RAM
  proglen = 5202; progsum = 0x2d74
  progstart = 0x0210
  eeprogname = 'Instruments/' + instrdir + '/test-loads/com1fore.mem'# program for EEPROM
  eeproglen = 5207; eeprogsum = 0xc746
  eeprogpg = 0x42

  def fPktSeqNums(block):
    return (0, block.TimeTag)

  def fPktSeqNext(seq, time, interval):
    return (0, time+interval)

  def fPktDataLen(blk):
    return blk.Length

  # host-specific things here ...
  def fPktLenOk(blk, len):			# SPP pads to even
    l = len
    if l%2 == 1:
      l += 1
    return fPktDataLen(blk) == l

# ------------------------------------------------------------------------
# JUICE-specific things here

if host=='JUICE':
  # use GSEOS 7.0
  from GseosMonitor import TMonitor
  from GseosSequencer import TSequencer, TSeqTimeoutError
  from HostCommands import fSetMacroMode, fSetTime
  from HostCommands import CMD, fLoadFile

  dOpcodes = {
	'CMD_ECHO' : 164,
	'CMD_NULL' : 0x80,
	'CMD_WRAP' : 0x82,
	'FILE_DEST' : 191,
	'FILE_SWITCH' : 192,
	'MAC_CHECK' : 0x83,
	'MAC_DEF' : 0x84,
	'MAC_DELAY' : 0x85,
	'MAC_END' : 0x86,
	'MAC_ENDDEF' : 0x87,
	'MAC_HALT' : 0x88,
	'MAC_LOOP_BEGIN' : 0x89,
	'MAC_LOOP_END' : 0x8a,
	'MAC_NEST' : 0x8b,
	'MAC_PAUSE' : 0x8c,
	'MAC_READ' : 0x8d,
	'MAC_RESTORE' : 0x8e,
	'MAC_RUN' : 0x8f,
	'MAC_RUN_SILENT' : 0x90,
	'MAC_SAVE' : 0x91,
	'MEM_CHECK' : 0x92,
	'MEM_COPY' : 0x93,
	'MEM_LOAD' : 0x94,
	'MEM_NV_ENB' : 167,
	'MEM_READ' : 0x95,
	'MEM_READ_ABRT' : 0x96,
	'MEM_READ_INT' : 165,
	'MEM_RUN' : 0x97,
	'MEM_STR_LOAD' : 0x98,
	'MEM_STR_READ' : 0x99,
	'MEM_WR_EN' : 0x9a,
	'MON_CNTRL' : 0x9b,
	'ROM_BOOT' : 0x9c,
	'ROM_GO' : 0x9d,
	'SAF_OFF' : 0x9e,
	'SAF_RESET' : 0x9f,
	'SAF_TIMEOUT' : 0xa0,
	'STAT_CLR' : 0xa1,
	'STAT_INT' : 0xa2,
	'STAT_MEM' : 0xa3,
  }

  dTrueNames = {
  # none ...
  }

  # Arguments: map to strings
  enable='Enable'				# Enable/Disable
  disable='Disable'
  cmdexec='CmdExec'				# Counters
  cmdrej='CmdRej'
  maccmdexec='MacCmdExec'
  maccmdrej='MacCmdRej'
  telvol='TelVol'
  all='All'

  # Programs to use in file load tests, etc.
  # Note: MEM_CHECK uses byte lengths.
  tstpg = 0x06
  testname = 'Instruments/PEPHI/Infrastructure/test-loads/counts.mem'	# test pattern
  testlen = 2*8192; testsum = 0xf808
  progname = 'Instruments/PEPHI/Infrastructure/test-loads/com1for.mem'	# program for RAM
  proglen = 10404; progsum = 0x2d74
  progstart = 0x0210
  eeprogname = 'Instruments/PEPHI/Infrastructure/test-loads/com1fore.mem'# program for MRAM
  eeproglen = 10414; eeprogsum = 0xc746
  eeprogpg = 0x42

  def fPktSeqNums(block):
    return (0, block.TimeTag)

  def fPktSeqNext(seq, time, interval):
    return (0, time+interval)

  def fPktDataLen(blk):
    return blk.Length

  # host-specific things here ...
  def fPktLenOk(blk, len):			# Strofio pads to even
    l = len
    if l%2 == 1:
      l += 1
    return fPktDataLen(blk) == l

  def fMemLoadEcho(addr, len, b0, b1):
    return [0, 0, 0, 1,
            (addr>>24)&0xff, (addr>>16)&0xff, (addr>>8)&0xff, addr&0xff,
            0, 0]

  def fMemReadEcho(addr, len):
    return [0, 0, 0, 1,
            (addr>>24)&0xff, (addr>>16)&0xff, (addr>>8)&0xff, addr&0xff,
            0, 0]

# ------------------------------------------------------------------------
# Europa-specific things here

if host=='Europa':
  # use GSEOS 7.0
  from GseosMonitor import TMonitor
  from GseosSequencer import TSequencer, TSeqTimeoutError
  from HostCommands import fSetMacroMode, fSetTime
  from HostCommands import CMD, fLoadFile

  dOpcodes = {
	'CMD_NULL' : 0x01,
	'CMD_WRAP' : 0x02,
	'MAC_CHECK' : 0x03,
	'MAC_DEF' : 0x04,
	'MAC_DELAY' : 0x05,
	'MAC_END' : 0x06,
	'MAC_ENDDEF' : 0x07,
	'MAC_HALT' : 0x08,
	'MAC_LOOP_BEGIN' : 0x09,
	'MAC_LOOP_END' : 0x0a,
	'MAC_NEST' : 0x0b,
	'MAC_PAUSE' : 0x0c,
	'MAC_READ' : 0x0d,
	'MAC_RESTORE' : 0x0e,
	'MAC_RUN' : 0x0f,
	'MAC_RUN_SILENT' : 0x10,
	'MAC_SAVE' : 0x11,
	'MEM_CHECK' : 0x12,
	'MEM_COPY' : 0x13,
	'MEM_LOAD' : 0x14,
	'MEM_READ' : 0x15,
	'MEM_READ_ABRT' : 0x16,
	'MEM_RUN' : 0x17,
	'MEM_STR_LOAD' : 0x18,
	'MEM_STR_READ' : 0x19,
	'MEM_WR_EN' : 0x1a,
	'MON_CNTRL' : 0x1b,
	'ROM_BOOT' : 0x1e,
	'ROM_GO' : 0x1f,
	'SAF_OFF' : 0x22,
	'SAF_RESET' : 0x23,
	'SAF_TIMEOUT' : 0x24,
	'STAT_CLR' : 0x1c,
	'STAT_INT' : 0x1d,
	'STAT_MEM' : 0x20,
  }

  dTrueNames = {
  # none ...
  }

  # Arguments: map to strings
  enable='Enable'				# Enable/Disable
  disable='Disable'
  cmdexec='CmdExec'				# Counters
  cmdrej='CmdRej'
  maccmdexec='MacCmdExec'
  maccmdrej='MacCmdRej'
  telvol='TelVol'
  all='All'

  # Programs to use in file load tests, etc.
  tstpg = 0xf
  testname = 'Instruments/MISE/Infrastructure/test-loads/counts.mem'	# test pattern
  testlen = 8192; testsum = 0xf808
  progname = 'Instruments/MISE/Infrastructure/test-loads/com2for.mem'	# program for RAM
  proglen = 5205; progsum = 0x8eb8
  progstart = 0x0210
  eeprogname = 'Instruments/MISE/Infrastructure/test-loads/com2fore.mem'# program for EEPROM
  eeproglen = 5210; eeprogsum = 0xd10b
  eeprogpg = 0x42

# TBD: why don't we test sequence numbers anymore?
  def fPktSeqNums(block):
    return (0, block.TimeTag)

  def fPktSeqNext(seq, time, interval):
    return (0, time+interval)

  def fPktDataLen(blk):
    return blk.Length

  # host-specific things here ...
  def fPktLenOk(blk, len):			# pads such that packet is multiple of 4
    p = (~len + 3) & 3
    return fPktDataLen(blk) == (len + p)

# ------------------------------------------------------------------------
# Lucy LORRI-specific things here

if (host == 'Lucy'):
  # use GSEOS 7.0+
  from GseosMonitor import TMonitor
  from GseosSequencer import TSequencer, TSeqTimeoutError
  from HostCommands import fSetMacroMode, fSetTime
  from HostCommands import CMD, fLoadFile

  dOpcodes = {
	'CMD_NULL' : 0x01,
	'CMD_WRAP' : 0x02,
	'MAC_CHECK' : 0x03,
	'MAC_DEF' : 0x04,
	'MAC_DELAY' : 0x05,
	'MAC_END' : 0x06,
	'MAC_ENDDEF' : 0x07,
	'MAC_HALT' : 0x08,
	'MAC_LOOP_BEGIN' : 0x09,
	'MAC_LOOP_END' : 0x0a,
	'MAC_NEST' : 0x0b,
	'MAC_PAUSE' : 0x0c,
	'MAC_READ' : 0x0d,
	'MAC_RESTORE' : 0x0e,
	'MAC_RUN' : 0x0f,
	'MAC_RUN_SILENT' : 0x10,
	'MAC_SAVE' : 0x11,
	'MEM_CHECK' : 0x12,
	'MEM_COPY' : 0x13,
	'MEM_LOAD' : 0x14,
	'MEM_READ' : 0x15,
	'MEM_READ_ABRT' : 0x16,
	'MEM_RUN' : 0x17,
	'MEM_STR_LOAD' : 0x18,
	'MEM_STR_READ' : 0x19,
	'MEM_WR_EN' : 0x1a,
	'MON_CNTRL' : 0x1b,
	'ROM_BOOT' : 0x1e,
	'ROM_GO' : 0x1f,
	'SAF_OFF' : 0x22,
	'SAF_RESET' : 0x23,
	'SAF_TIMEOUT' : 0x24,
	'STAT_CLR' : 0x1c,
	'STAT_INT' : 0x1d,
	'STAT_MEM' : 0x20,
	'MEM_NV_ENB' : 0x26
  }

  dTrueNames = {
  # none ...
  }
  IgnoredTrueNames = {
	'MAC_LOOP_BEGIN' : 'MAC_LOOP_BEG',
	'MAC_RUN_SILENT' : 'MAC_RUN_SIL',
	'MEM_READ_ABRT'  : 'MEM_READ_ABT'
  }

  # Arguments: map to strings
  enable='Enable'				# Enable/Disable
  disable='Disable'
  cmdexec='CmdExec'				# Counters
  cmdrej='CmdRej'
  maccmdexec='MacCmdExec'
  maccmdrej='MacCmdRej'
  telvol='TelVol'
  all='All'

  # Programs to use in file load tests, etc.
  dir = 'Instruments/LLORRI/tests/' 

  tstpg = 0x6
  testname = dir + 'counts.mem'			# test pattern
  testlen = 8192; testsum = 0xf808

  progname = dir + 'llorri.mem'
  proglen = 23834; progsum = 0xea8e
  progstart = 0x0210

  eeprogname = dir + 'llorri-e.mem'
  eeproglen = 23839; eeprogsum = 0x981c
  eeprogpg = 0x41

  # Ignore sequence numbers?
  # For all, the numbers are not put in the decoded blocks.
  def fPktSeqNums(block):
    return (0, block.TimeTag)

  def fPktSeqNext(seq, time, interval):
    return (0, time+interval)

  def fPktDataLen(blk):
    return blk.Length

  # host-specific things here ...
  if (host == 'Lucy'):	# MMs padding is variable
    def fPktLenOk(blk, len):			# Juno length is known, but
      return fPktDataLen(blk) >= len		#   MEM_STR_LOAD command is padded
  else:						# RBSP pads to even
    def fPktLenOk(blk, len):
      l = len
      if l%2 == 1:
        l += 1
      return fPktDataLen(blk) == l
  #else:					# Juno length is known
  #  def fPktLenOk(blk, len):
  #    return fPktDataLen(blk) == len

  # TBD: experiment; maybe move to PuckCommands?
  # Replace fLoadFile
  if (host == 'MMS'):
    from GseosFileUpload import StartUpload
    def fLoadFile(name, addr):
      StartUpload('MemLoad', name, ["%d" % addr])

# ------------------------------------------------------------------------
# Useful helpers

# Blocks -----------------------------------------------------------------

bAppStatus  = eval(instr + '_Status')
bBootStatus = eval(instr + '_Boot_Status')
bAlarm      = eval(instr + '_Alarm')
bEcho       = eval(instr + '_CmdEcho')
bMemCheck   = eval(instr + '_MemChecksum')
bMemRead    = eval(instr + '_MemDump')
bMacCheck   = eval(instr + '_MacroChecksum')
bMacRead    = eval(instr + '_MacroDump')

# Error/status logging ---------------------------------------------------

ierrors = 0

def C(s):
  print s

def ResetError():
  global ierrors
  ierrors = 0

def Error(s):
  global ierrors
  ierrors += 1
  print s

def ErrorReport():
  if ierrors == 0:
    print "No errors"
  else:
    print "%d errors seen" % ierrors

def ErrorsSeen():
  return ierrors

# Commanding --------------------------------------------------------------

def fSendCmd(name, *args):
  CMD(cmdprefix + '_' + dTrueNames.get(name, name), *args)

# Packet checking ---------------------------------------------------------

def fPacketSeen(oSeq, block, timeout):
  seen = 1
  try:
    oSeq.Wait(block, lambda:1, (), timeout)
  except TSeqTimeoutError:
    seen = 0
  return seen

def fSyncIdle(oSeq, timeout, block=bEcho):
  # TBD: value differs for each system
  if fPacketSeen(oSeq, block, 8):	# if block seen in round-trip time
    while fPacketSeen(oSeq, block, timeout):
      pass				# wait until no packets seen

def fSyncTime(oSeq, newtime, block):
  syncing = 1
  fSetTime(newtime)
  try:
    while syncing:
      oSeq.Wait(block, lambda:1, (), 10)
      seq,time = fPktSeqNums(block)
      if ((time >= newtime) and
         (time-newtime < 5)):
        syncing = 0
  except TSeqTimeoutError:
    Error('Cannot sync time')

# Waits for the given block which successfully executes function f.
# Contrast with fCheckPacket().
def fSyncPacket(oSeq, block, f, timeout=10):
  try:
    oSeq.Wait(block, f, (), timeout)
  except TSeqTimeoutError:
    Error('Cannot sync to packet')

def fCheckNoPacket(oSeq, block, timeout=10):
  if fPacketSeen(oSeq, block, timeout):
      Error('Unexpected packet seen')

# Waits for the next occurrence of the given block, then tests block
# by executing function f.  Contrast with fSyncPacket().
def fCheckPacket(oSeq, block, f, timeout=10):
  if fPacketSeen(oSeq, block, timeout):
    if not f():
      Error('Bad packet data')
  else:
    Error('No packet')

def fCheckSeq(oSeq, block, nblks, interval):
  try:
    oSeq.Wait(block, lambda:1, (), interval+5)
    seq,time = fPktSeqNums(block)
    for i in range(nblks):		# check expected seq. numbers and times
      seq,time = fPktSeqNext(seq, time, interval)
      oSeq.Wait(block, lambda:1, (), interval+5)
      if not (seq,time)==fPktSeqNums(block):
        Error('Packet sequence error')
  except TSeqTimeoutError:
    Error('Packet sequence timeout')

def fCheckAlarm(oSeq, alarmid, type, value=None, timeout=10):
  if fPacketSeen(oSeq, bAlarm, timeout):
    if not((bAlarm.AlarmId==alarmid) and (bAlarm.AlarmType==type) ):
      Error('Bad alarm')
    if value is not None and not(bAlarm.Value==value):
      Error('Bad alarm value')
  else:
    Error('No alarm')

def fCheckEcho(oSeq, cmdname, result, args=None, timeout=10):
  if fPacketSeen(oSeq, bEcho, timeout):
    if not((bEcho.Opcode==dOpcodes[cmdname]) and (bEcho.Result==result)):
      Error('Bad command echo %x' % bEcho.Opcode )
    elif args is not None:
      if not (fPktLenOk(bEcho, 2+len(args))):
        Error('Bad command echo length')
      elif list(bEcho.Args[:len(args)]) != args:
        Error('Bad command echo args')
  else:
    Error('No command echo')

def fCheckMemCheck(oSeq, src, words, sum):
  if fPacketSeen(oSeq, bMemCheck, 10):
    if not ((bMemCheck.Address==src) and
		(bMemCheck.MemLength==words) and
		(bMemCheck.CRC_Value==sum)):
      Error('Bad memory checksum')
  else:
    Error('No memory checksum')

def fCheckMemRead(oSeq, lowaddr, highaddr, bytes, expdata):
  if fPacketSeen(oSeq, bMemRead, 10):
    if not ((bMemRead.Address>=lowaddr) and
		(bMemRead.Address<=highaddr) and
		(bMemRead.DumpLength==bytes)):
      Error('Bad memory read')
    else:
      dataok = 1
      for i in range(len(expdata)):
        if bMemRead.DumpData[i]<>expdata[i]:
          dataok = 0
      if not dataok:
        Error('Bad memory read data')
  else:
    Error('No memory read')

def fCheckMacCheck(oSeq, firstid, lastid, sums):
  if fPacketSeen(oSeq, bMacCheck, 10):
    if not ((bMacCheck.FirstMacro==firstid) and
		(bMacCheck.LastMacro==lastid) and
		(fPktLenOk(bMacCheck, 2 + 2*len(sums)))):
      Error('Bad macro checksum packet')
    else:
      dataok = 1
      for i in range(len(sums)):
        if bMacCheck.Checksums[i]<>sums[i]:
          dataok = 0
      if not dataok:
        Error('Bad macro checksum')
  else:
    Error('No memory checksum')

def fCheckMacRead(oSeq, macid, blockno, expdata):
  if fPacketSeen(oSeq, bMacRead, 10):
    if not ((bMacRead.MacroId==macid) and
		(bMacRead.BlockIndex==blockno)):
      Error('Bad macro read')
    else:
      dataok = 1
      for i in range(len(expdata)):
        if bMacRead.MacroData[i]<>expdata[i]:
          dataok = 0
      for i in range(len(expdata), 32):
        if bMacRead.MacroData[i]<>0:
          dataok = 0
      if not dataok:
        Error('Bad macro read data')
  else:
    Error('No macro read')

def fCRC(b):
  crc = 0xffff
  for i in range(len(b)):
    crc ^= b[i] << 8
    for i in range(8):
      if crc & 0x8000:
        crc = crc<<1 ^ 0x1021
      else:
        crc = crc<<1
  return crc&0xffff

def fMacChecksum(b):
  return fCRC(b + [0]*((32 - len(b))%32))

# ------------------------------------------------------------------------
# Command echo sequence verification (from M. Paul)

iEchoSeqEnb = 0
lEchoSeqData = []

def fStartEchoSeq():
  global iEchoSeqEnb, lEchoSeqData
  iEchoSeqEnb = 1
  lEchoSeqData = []

def fCheckEchoSeq(expdata):
  global iEchoSeqEnb
  iEchoSeqEnb = 0
  if lEchoSeqData != expdata:
    Error('Bad command echo sequence')

def fBuildEchoSeq(block):
  global lEchoSeqData
  if iEchoSeqEnb:
    lEchoSeqData.append( (block.Opcode, block.Macro, block.Result) )

bEcho.Monitors.append(
  TMonitor('Echo Seq', fBuildEchoSeq))

# ------------------------------------------------------------------------
# Construct sequencer to run test

def fDefTest(str, fun):
  TSequencer(str, fun, bStart=0)
