# (c) 2017 Johns Hopkins University / Applied Physics Laboratory
# by John R. Hayes
from regresstools import *
import GseosBlocks

# Need access to Bios to enable/disable time message.
import PEP_HI_SPW_Bios as PEP_HI_Bios

# Precondition: RawCmdMode = No in gseos.ini file.

# Notes:
# - Tests miscellaneous features/extensions of the common code.
# - Not repeatable without restart because of SAF_RESET.

# ------------------------------------------------------------------------
# Boot vs. Application

from __main__ import PEPHI_Hsk_A as bStatusA
from __main__ import PEPHI_Hsk_B as bStatusB

# Map housekeeping name to SID
sids = {
	'BootHsk': 1,
	'HskA'   : 2,
	'HskB'   : 3,
}

# Housekeeping packets: block, name of interval within block, and SID
hskboot = [
  (bBootStatus, 'StatusInt', 'BootHsk')
]
hskapp = [
  (bStatusA, 'JENI_StatusAInt', 'HskA'),
  (bStatusB, 'JENI_StatusBInt', 'HskB'),
]

# Things that are different:
bStatus = bAppStatus		# status packet
hsk = hskapp

def fPrepApp():
  global bStatus, hsk
  bStatus = bAppStatus
  hsk = hskapp

def fPrepBoot():
  global bStatus, hsk
  bStatus = bBootStatus
  hsk = hskboot

# ------------------------------------------------------------------------
# Helpers

# Emergency packets, i.e. TM(5,4)
from HostConstants import EVT_EMG_BASE, EVT_PRG_BASE
from __main__ import PEPHI_EmergencyEvent, PEPHI_ProgressEvent 
from __main__ import CPTP_TLM as bSpW

cmd_executed = 0
cmd_rejected = 0

def fSyncCmd():
  global cmd_executed, cmd_rejected
  cmd_executed = bStatus.CmdExec
  cmd_rejected = bStatus.CmdReject

def fClrCmdExec():
  global cmd_executed
  cmd_executed = 0

def fClrCmdReject():
  global cmd_rejected
  cmd_rejected = 0

def fGoodCmd():
  global cmd_executed
  cmd_executed = (cmd_executed + 1) % 256

def fBadCmd():
  global cmd_rejected
  cmd_rejected = (cmd_rejected + 1) % 256

def fCheckCmdCounts(oSeq):
  if fPacketSeen(oSeq, bStatus, 10):
    if not((bStatus.CmdExec==cmd_executed) and
           (bStatus.CmdReject==cmd_rejected)):
      Error('Bad command counts')
      fSyncCmd()
  else:
    Error('No status')

def fCheckProgress(oSeq, progressid):
  bProgress = PEPHI_ProgressEvent
  if fPacketSeen(oSeq, bProgress, 10):
    if not(bProgress.EventId==EVT_PRG_BASE+progressid):
      Error('Bad progress ID')
  else:
    Error('No emergency packet')

def fCheckEmergency(oSeq, emergencyid):
  bEmergency = PEPHI_EmergencyEvent
  if fPacketSeen(oSeq, bEmergency, 10):
    if not(bEmergency.EventId==EVT_EMG_BASE+emergencyid):
      Error('Bad emergency ID')
  else:
    Error('No emergency packet')

# Establish preconditions: status/housekeeping on interval=1
def fEstablishPreconditions(oSeq):
  C('---Establish preconditions---')
  PEP_HI_Bios.EnableTimeMsg(True)
  fSendCmd('STAT_CLR', all)
  fClrCmdExec(); fClrCmdReject(); fGoodCmd()
  fCheckEcho(oSeq, 'STAT_CLR', 0, [255])
  fSendCmd('STAT_INT', 1)
  fGoodCmd()
  fCheckEcho(oSeq, 'STAT_INT', 0, [0,1])

# Functions to return MSBs and LSBs of 16-bit input x.
def MSBs(x): return (x>>8)&0xff
def LSBs(x): return x&0xff

# ------------------------------------------------------------------------
# Command echo enable/disable

def fCommandEcho(oSeq):
  # Precondition: command echoes enabled.
  C('---Command echo enable/disable---')
  C('---Checking defaults---')
  fCheckPacket(oSeq, bStatus, lambda: (bStatus.CommandEcho==1) )
  C('---CMD_NULL should be echoed---')
  fSendCmd('CMD_NULL')
  fCheckEcho(oSeq, 'CMD_NULL', 0, [])
  fGoodCmd()
  fCheckCmdCounts(oSeq)
  C('---CMD_ECHO(Disable) disables command echoes (including this one)---')
  fSendCmd('CMD_ECHO', 'Disable')
  #fCheckEcho(oSeq, 'CMD_ECHO', 0, [0])
  fCheckNoPacket(oSeq, bEcho)
  fGoodCmd()
  fCheckPacket(oSeq, bStatus, lambda: (bStatus.CommandEcho==0) )
  fCheckCmdCounts(oSeq)
  C('---CMD_NULL should not be echoed---')
  fSendCmd('CMD_NULL')
  #fCheckEcho(oSeq, 'CMD_NULL', 0, [])
  fCheckNoPacket(oSeq, bEcho)
  fGoodCmd()
  fCheckCmdCounts(oSeq)
  C('---CMD_ECHO(Enable) re-enables command echoes---')
  fSendCmd('CMD_ECHO', 'Enable')
  fCheckEcho(oSeq, 'CMD_ECHO', 0, [1])
  fGoodCmd()
  fCheckPacket(oSeq, bStatus, lambda: (bStatus.CommandEcho==1) )
  C('---Check command counts---')
  fCheckCmdCounts(oSeq)

# ------------------------------------------------------------------------
# Command bursts

# There is an implicit requirement in the SpaceWire ICD of handling bursts of
# five commands per second.

def fCommandBurst(oSeq):
  C('---Command bursts---')
  # Disable echo to lessen burden on GSEOS
  C('---CMD_ECHO(Disable) disables command echoes (including this one)---')
  fSendCmd('CMD_ECHO', 'Disable')
  #fCheckEcho(oSeq, 'CMD_ECHO', 0, [0])
  fGoodCmd()
  C('---Send burts of CMD_NULL---')
  for burst in range(10):
    C('---   burst %d ...'%(burst+1))
    for i in range(10):			# send command burst
      fSendCmd('CMD_NULL')
      fGoodCmd()
    fSyncIdle(oSeq, 4)			# wait for command echos to stop
  C('---CMD_ECHO(Enable) re-enables command echoes---')
  fSendCmd('CMD_ECHO', 'Enable')
  fCheckEcho(oSeq, 'CMD_ECHO', 0, [1])
  fGoodCmd()
  C('---Check command counts---')
  fCheckCmdCounts(oSeq)

# ------------------------------------------------------------------------
# File control
# Note: this should be in CPTPRaw test, but it is easier here.

def fFileControl(oSeq):
  # Pre/post-condition: status/housekeeping on
  C('---File control---')
  C('---STAT_INT(0) disables status/housekeeping--')
  fSendCmd('STAT_INT', 0)
  fCheckEcho(oSeq, 'STAT_INT', 0, [0])
  fGoodCmd()
  C('---FILE_DEST rejected: unknown file---')
  # Note: file range is 0-8 here, but 0-7 for FILE_SWITCH below
  fSendCmd('CMD_WRAP', dOpcodes['FILE_DEST'], 9, 0)
  fCheckEcho(oSeq, 'FILE_DEST', 0x03, [9, 0])
  fBadCmd()
  C('---FILE_SWITCH rejected: unknown file---')
  fSendCmd('CMD_WRAP', dOpcodes['FILE_SWITCH'], 8)
  fCheckEcho(oSeq, 'FILE_SWITCH', 0x03, [8])
  fBadCmd()
  C('---FILE_DEST(1, 1) routes command echo to file 1---')
  fSendCmd('FILE_DEST', 1, 1)
  fCheckEcho(oSeq, 'FILE_DEST', 0, [1, 1])
  fGoodCmd()
  fSendCmd('CMD_NULL')
  #fCheckEcho(oSeq, 'CMD_NULL', 0, [])	# check SpW-level packet
  fCheckPacket(oSeq, bSpW, lambda: (bSpW.CPTP_TargetLogicalAddr==0x45) )
  fGoodCmd()
  C('---FILE_DEST(7, 1) routes command echo to file 7, PEP-Lo!---')
  fSendCmd('FILE_DEST', 7, 1)
  fCheckEcho(oSeq, 'FILE_DEST', 0, [7, 1])
  fGoodCmd()
  fSendCmd('CMD_NULL')
  #fCheckEcho(oSeq, 'CMD_NULL', 0, [])	# check SpW-level packet
  fCheckPacket(oSeq, bSpW, lambda: (bSpW.CPTP_TargetLogicalAddr==0x66) )
  fGoodCmd()
  C('---FILE_DEST(8, 1) routes command echo to OBC!---')
  fSendCmd('FILE_DEST', 8, 1)
  fCheckEcho(oSeq, 'FILE_DEST', 0, [8, 1])
  fGoodCmd()
  fSendCmd('CMD_NULL')
  #fCheckEcho(oSeq, 'CMD_NULL', 0, [])	# check SpW-level packet
  fCheckPacket(oSeq, bSpW, lambda: (bSpW.CPTP_TargetLogicalAddr==0x25) )
  fGoodCmd()
  C('---FILE_DEST(0, 1) restores default file 0---')
  fSendCmd('FILE_DEST', 0, 1)
  fCheckEcho(oSeq, 'FILE_DEST', 0, [0, 1])
  fGoodCmd()
  CMD('PEPHI_CMD_NULL')
  #fCheckEcho(oSeq, 'PEPHI_CMD_NULL', 0, [])	# check SpW-level packet
  fCheckPacket(oSeq, bSpW, lambda: (bSpW.CPTP_TargetLogicalAddr==0x35) )
  fGoodCmd()
  C('---FILE_SWITCH(0) switches file 0---')
  fSendCmd('FILE_SWITCH', 0)
  #fCheckEcho(oSeq, 'FILE_SWITCH', 0, [0])
  fCheckProgress(oSeq, 3+0)
  fGoodCmd()
  C('---FILE_SWITCH(1) switches file 1---')
  fSendCmd('FILE_SWITCH', 1)
  #fCheckEcho(oSeq, 'FILE_SWITCH', 0, [1])
  fCheckProgress(oSeq, 3+1)
  fGoodCmd()
  C('---FILE_SWITCH(7) switches file 7, PEP-Lo!---')
  fSendCmd('FILE_SWITCH', 7)
  #fCheckEcho(oSeq, 'FILE_SWITCH', 0, [7])
  fCheckProgress(oSeq, 3+7)
  fGoodCmd()
  C('---STAT_INT(1) restores status/housekeeping--')
  fSendCmd('STAT_INT', 1)
  fCheckEcho(oSeq, 'STAT_INT', 0, [0, 1])
  fGoodCmd()
  C('---Check command counts---')
  fCheckCmdCounts(oSeq)

# ------------------------------------------------------------------------
# Housekeeping service

def fHskService(oSeq):
  C('---Housekeeping telecommand functionality---')
  # Precondition: status on
  C('---STAT_INT(0) turns off all housekeeping (and derived status)---')
  fSendCmd('STAT_INT', 0)
  fCheckEcho(oSeq, 'STAT_INT', 0, [0,0])
  fGoodCmd()
  oSeq.Sleep(2)				# wait for status to be off
  fCheckNoPacket(oSeq, bStatus)
  C('---HSK_INT rejected: undefined housekeeping packet---')
  fSendCmd('CMD_WRAP', dOpcodes['HSK_INT'], 0, 0, 0, 0, 0, 0)
  fCheckEcho(oSeq, 'HSK_INT', 0x03, [0, 0, 0, 0, 0, 0])
  fBadCmd()
  # For each housekeeping packet
  for i in range(len(hsk)):
    (blk, stname, hskname) = hsk[i]
    sid = sids[hskname]
    C('---Test housekeeping: %s (SID=%d)---'%(hskname,sid))
    C('---Check HSK_INT command with different intervals---')
    for interval in [1, 2, 3, 10]:
      C('\tinterval = %d' % interval)
      fSendCmd('HSK_INT', hskname, interval)	# interval in seconds
      fCheckEcho(oSeq, 'HSK_INT', 0, [0,0,0,sid,0,interval])
      fGoodCmd()
      fCheckPacket(oSeq, blk, lambda:(blk.ReadItem(stname)==interval))
      fCheckSeq(oSeq, blk, 4, interval)
    C('---HSK_INT(0) turns off housekeeping---')
    fSendCmd('HSK_INT', hskname, 0)
    fCheckEcho(oSeq, 'HSK_INT', 0, [0,0,0,sid,0,0])
    fGoodCmd()
    oSeq.Sleep(2)				# wait for housekeeping to be off
    fCheckNoPacket(oSeq, blk)
    C('---STAT_FORCE generates housekeeping---')# note: generates all housekeeping
    fSendCmd('STAT_FORCE')
    #fCheckEcho(oSeq, 'STAT_FORCE', 0, [])
    fGoodCmd()
    if not fPacketSeen(oSeq, blk, 10):
      Error('No housekeeping packet')
    C('---Housekeeping remains off---')
    fCheckNoPacket(oSeq, blk)
  # Test force status
  C('---STAT_FORCE generates status---')
  fSendCmd('STAT_FORCE')
  #fCheckEcho(oSeq, 'STAT_FORCE', 0, [])
  fGoodCmd()
  if not fPacketSeen(oSeq, bStatus, 10):
    Error('No housekeeping packet')
  C('---Status remains off---')
  fCheckNoPacket(oSeq, bStatus)
  # Restore defaults
  C('---STAT_INT(1) turns on status---')
  fSendCmd('STAT_INT', 1)
  fCheckEcho(oSeq, 'STAT_INT', 0, [0,1])
  fGoodCmd()
  C('---Check command counts---')
  fCheckCmdCounts(oSeq)

# ------------------------------------------------------------------------
# Memory extension - enbable/disable NV memory

def fMemoryExtend(oSeq,):
  C('---Memory extension---')
  C('---Checking defaults---')
  fCheckPacket(oSeq, bStatus, lambda: (bStatus.NVMemEnb==0) )
  C('---MEM_NV_ENB(Sleep/Reset)---')
  fSendCmd('MEM_NV_ENB', 'SleepReset')
  fCheckEcho(oSeq, 'MEM_NV_ENB', 0, [1])
  fGoodCmd()
  fCheckPacket(oSeq, bStatus, lambda: (bStatus.NVMemEnb==1) )
  C('---MEM_NV_ENB(Enable)---')
  fSendCmd('MEM_NV_ENB', 'Enable')
  fCheckEcho(oSeq, 'MEM_NV_ENB', 0, [0])
  fGoodCmd()
  fCheckPacket(oSeq, bStatus, lambda: (bStatus.NVMemEnb==0) )
  C('---Check command counts---')
  fCheckCmdCounts(oSeq)

# ------------------------------------------------------------------------
# Dump extension - dump packet interval

def fDumpExtend(oSeq):
  C('---Dump extension---')
  C('---MEM_READ used to dump entire page---')
  fSendCmd('MEM_READ', 0x00000, 0xffff)
  fGoodCmd()
  fCheckMemRead(oSeq, 0x00000, 0x01000, 256, [])
  fCheckSeq(oSeq, bMemRead, 10, 1)
  C('---MEM_READ_INT(200) produces a packet every 2 seconds---')
  fSendCmd('MEM_READ_INT', 200)
  fCheckEcho(oSeq, 'MEM_READ_INT', 0, [MSBs(200), LSBs(200)])
  fGoodCmd()
  oSeq.Sleep(3)
  fCheckSeq(oSeq, bMemRead, 10, 2)
  C('---MEM_READ_INT(300) produces a packet every 3 seconds---')
  fSendCmd('MEM_READ_INT', 300)
  fCheckEcho(oSeq, 'MEM_READ_INT', 0, [MSBs(300), LSBs(300)])
  fGoodCmd()
  oSeq.Sleep(3)
  fCheckSeq(oSeq, bMemRead, 10, 3)
  C('---MEM_READ_INT(0) restores default, a packet every second---')
  fSendCmd('MEM_READ_INT', 0)
  fCheckEcho(oSeq, 'MEM_READ_INT', 0, [MSBs(0), LSBs(0)])
  fGoodCmd()
  oSeq.Sleep(3)
  fCheckSeq(oSeq, bMemRead, 10, 1)
  C('---MEM_READ_ABRT aborts memory dump---')
  fSendCmd('MEM_READ_ABRT')
  fGoodCmd()
  fCheckEcho(oSeq, 'MEM_READ_ABRT', 0x00, [])
  oSeq.Sleep(3)				# wait for dump to stop
  fCheckNoPacket(oSeq, bMemRead)	# pre-condition re-established
  C('---Check command counts---')
  fCheckCmdCounts(oSeq)

# ------------------------------------------------------------------------
# Macro extension - MAC_END includes macro ID (application only)

def fMacroExtend(oSeq):
  # Precondition: instrument in application mode.
  C('---Macro extension---')
  for id in range(11, 14):
    C('---MAC_DEF(%d), MAC_DELAY(10), MAC_ENDDEF() defines macro %d---'%(id,id))
    fSendCmd('MAC_DEF', id)
    fCheckEcho(oSeq, 'MAC_DEF', 0, [id])
    fGoodCmd()
    fSendCmd('MAC_DELAY', 10)
    fCheckEcho(oSeq, 'MAC_DELAY', 1, [0,10])
    fGoodCmd()
    fSendCmd('MAC_ENDDEF')
    fCheckEcho(oSeq, 'MAC_ENDDEF', 0, [])
    fGoodCmd()
  for id in range(11, 14):
    C('---MAC_RUN(%d) runs macro %d--'%(id,id))
    fStartEchoSeq()
    fSendCmd('MAC_RUN', id)
    fGoodCmd()
    fSyncIdle(oSeq, 4)
    fCheckEchoSeq([
	(dOpcodes['MAC_RUN'], 0, 0),
	(dOpcodes['MAC_DELAY'], 1, 0)])
    C('---   MAC_END(%d) automatically generated---'%id)
    oSeq.Sleep(2)
    fCheckEcho(oSeq, 'MAC_END', 0, [id])
  C('---Check command counts---')
  fCheckCmdCounts(oSeq)

# ------------------------------------------------------------------------
# Safing (application only)

def fSafingApp(oSeq):
  # Precondition: instrument in application mode.
  C('---Safing---')
  C('---SAF_TIMEOUT(5) to establish precondition---')
  fSendCmd('SAF_TIMEOUT', 5)
  fCheckEcho(oSeq, 'SAF_TIMEOUT', 0, [0,5])
  fGoodCmd()
  fCheckPacket(oSeq, bStatus, lambda: (bStatus.SafingTime==5) )
  C('---Confirm that a shutdown macro is defined---')
  fSendCmd('MAC_READ', 1, 1)
  fGoodCmd()
  fCheckPacket(oSeq, bMacRead, lambda:1)
  C('---Confirm that a safing macro is defined---')
  fSendCmd('MAC_READ', 2, 2)
  fGoodCmd()
  fCheckPacket(oSeq, bMacRead, lambda:1)
  C('---MAC_DEF(2), CMD_NULL(), CMD_NULL(), MAC_ENDDEF() replaces safing macro---')
  fSendCmd('MAC_DEF', 2)
  fCheckEcho(oSeq, 'MAC_DEF', 0, [2])
  fGoodCmd()
  fSendCmd('CMD_NULL')
  fCheckEcho(oSeq, 'CMD_NULL', 1, [])
  fGoodCmd()
  fSendCmd('CMD_NULL')
  fCheckEcho(oSeq, 'CMD_NULL', 1, [])
  fGoodCmd()
  fSendCmd('MAC_ENDDEF')
  fCheckEcho(oSeq, 'MAC_ENDDEF', 0, [])
  fGoodCmd()
  C('---SAF_TIMEOUT(20) sets 20 second timeout---')
  fSendCmd('SAF_TIMEOUT', 20)
  fCheckEcho(oSeq, 'SAF_TIMEOUT', 0, [0,20])
  fGoodCmd()
  fCheckPacket(oSeq, bStatus, lambda: (bStatus.SafingTime==20) )
  C('---Turn off time message, confirm safing---')
  PEP_HI_Bios.EnableTimeMsg(False)
  fSendCmd('CMD_NULL')
  fCheckEcho(oSeq, 'CMD_NULL', 0, [])	# reset timeout using command
  fGoodCmd()
  fCheckNoPacket(oSeq, bEcho, 18)
  fStartEchoSeq()
  fSyncIdle(oSeq, 4)
  fCheckEchoSeq([
	(dOpcodes['CMD_NULL'], 1, 0),
	(dOpcodes['CMD_NULL'], 1, 0),
	(dOpcodes['MAC_END'],  1, 0)])
  fCheckPacket(oSeq, bStatus, lambda: (bStatus.MacId==2) )
  C('---SAF_TIMEOUT(10) resets to 10 second timeout---')
  fSendCmd('SAF_TIMEOUT', 10)
  fCheckEcho(oSeq, 'SAF_TIMEOUT', 0, [0,10])
  fGoodCmd()
  fStartEchoSeq()
  fCheckNoPacket(oSeq, bEcho, 8)
  fSyncIdle(oSeq, 4)
  fCheckEchoSeq([
	(dOpcodes['CMD_NULL'], 1, 0),
	(dOpcodes['CMD_NULL'], 1, 0),
	(dOpcodes['MAC_END'],  1, 0)])
  C('---SAF_TIMEOUT(5), turn time message back on---')
  fSendCmd('SAF_TIMEOUT', 5)
  fCheckEcho(oSeq, 'SAF_TIMEOUT', 0, [0,5])
  fGoodCmd()
  fCheckPacket(oSeq, bStatus, lambda: (bStatus.SafingTime==5) )
  PEP_HI_Bios.EnableTimeMsg(True)
  C('---SAF_OFF requests power off---')
  fSendCmd('SAF_OFF')
  #fCheckEcho(oSeq, 'SAF_OFF', 0, [])
  fCheckEmergency(oSeq, 0)
  fGoodCmd()
  C('---Check command counts---')
  fCheckCmdCounts(oSeq)
  # TBD: no boot ROM ...
  #C('---SAF_RESET returns to boot---')
  #fSendCmd('SAF_RESET')
  #fCheckPacket(oSeq, bBootStatus, lambda: (bBootStatus.Cause==1), 20)
  # Note: no longer in application mode; must be last step.

# ------------------------------------------------------------------------
# Top level test

def fAppCommonPlusRegression(oSeq):
  # Precondition: instrument in application mode.
  C('---Starting application common-plus regression test---')
  fPrepApp()
  ResetError()
  fEstablishPreconditions(oSeq)
  fCommandEcho(oSeq)
  fCommandBurst(oSeq)
  fFileControl(oSeq)
  fHskService(oSeq)
  fMemoryExtend(oSeq)
  fDumpExtend(oSeq)
  fMacroExtend(oSeq)
  fSafingApp(oSeq)
  C('---Regression test done---')
  ErrorReport()

fDefTest('JENI Application Common-Plus Test', fAppCommonPlusRegression)

def fBootCommonPlusRegression(oSeq):
  # Precondition: instrument in boot mode.
  C('---Starting boot common-plus regression test---')
  fPrepBoot()
  ResetError()
  fEstablishPreconditions(oSeq)
  fCommandEcho(oSeq)
  fCommandBurst(oSeq)
  fFileControl(oSeq)
  fHskService(oSeq)
  fMemoryExtend(oSeq)
  fDumpExtend(oSeq)
  C('---Regression test done---')
  ErrorReport()

fDefTest('JENI Boot Common-Plus Test', fBootCommonPlusRegression)
