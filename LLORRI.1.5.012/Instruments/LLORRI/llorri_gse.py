from __main__ import *
from GseosMonitor import TMonitor
import Gseos
import LLORRI_Bios
import HostCommands
from struct import pack, unpack
from GseosCmd import SendBinCmd

import time
import sys
import os

global iCount

try:
    emulator = os.environ[ 'EMULATOR' ]
    DecStatus_SPPCmd_EmulatorType = int(emulator)
except:
    DecStatus_SPPCmd_EmulatorType = 2

iCount = 0

InstrPwrEnableA = 0
InstrPwrEnableB = 0
ActiveSide = 0
StartupState = 0

if( DecStatus_SPPCmd_EmulatorType == 0 ):
    StartupState = 1

RequestPowerOff = 0
RequestPowerCycle = 0
RequestPowerCycleTime = 0

global WBS_TimeTag, WBS_Valid
global WS_TimeTag, WS_Valid
WBS_TimeTag = 0
WBS_Valid = 0
WS_TimeTag = 0
WS_Valid = 0

Uptime = 0
dUptime = 0

iTick = 0
iMaxTick = 3
iPowerOffs = 0
iModeSelect = 0

def fTrigger( aDummy ):
    global iCount
    global RequestPowerOff, RequestPowerCycle, RequestPowerCycleTime
    global StartupState, InstrPwrEnableA, InstrPwrEnableB , ActiveSide

    global iTick, iMaxTick, iPowerOffs
    global iModeSelect
    
    if( aDummy.strName == "DSACtrl" ):
	global Uptime
	Uptime += dUptime
	iTick += 1
	### print "DSACtrl", iTick, dUptime, Uptime

    if( aDummy.strName == "LOR_Boot_Status" ):
	### print "Boot Status %08x" % aDummy.TimeTag
	iMaxTick = aDummy.StatusInt + 2
	iTick = 0
	if( StartupState == 1 ):
	    print "LOR_Boot_Status says ON."
	    InstrPwrEnableA = 1 # This packet is proof we are alive.
	    StartupState = 0

	iModeSelect = iModeSelect + 1
	if( iModeSelect < 100 ) :
	    iModeSelect = 100
	if( iModeSelect > 104 ) :
	    iModeSelect = 100
	return

    if( aDummy.strName == "LOR_Status" ):
	### print "Status %08x" % aDummy.TimeTag
	iMaxTick = aDummy.StatusInt + 2
	iTick = 0
	if( StartupState == 1 ):
	    print "LOR_Status says ON."
	    InstrPwrEnableA = 1 # This packet is proof we are alive.
	    StartupState = 0

        iModeSelect = iModeSelect + 1
        if( 0 == 0 ):
            if( iModeSelect < 200 ) :
                iModeSelect = 200
            if( iModeSelect > 211 ) :
                iModeSelect = 200
	return

    if( iTick > iMaxTick ):
	LOR_LOS.TimeTag = iTick
	iMaxTick = 3
	### LOR_LOS.send(0)
	iModeSelect = iModeSelect + 1
	if( iModeSelect > 1 ) :
	    iModeSelect = 0

    if( (RequestPowerOff+RequestPowerCycle+RequestPowerCycleTime) > 0 ):
	t_out = time.localtime()
        sT = "%03d:%02d:%02d:%02d" % ( t_out.tm_yday, t_out.tm_hour, t_out.tm_min, t_out.tm_sec )
	print 'Power A', sT, RequestPowerOff, RequestPowerCycle, RequestPowerCycleTime 

    if( RequestPowerOff > 5 ):
	InstrPwrEnableA = 0
	RequestPowerOff = 0
	fFileUpdate( 0 )
	iPowerOffs = iPowerOffs + 1

    if( RequestPowerCycle > 5 ):
	InstrPwrEnableA = 0
	fFileUpdate( 0 )
	RequestPowerCycle = 0
	RequestPowerCycleTime = 1
	iPowerOffs = iPowerOffs + 1

    if( RequestPowerCycleTime > 0 ):
	RequestPowerCycleTime = RequestPowerCycleTime + 1

    if( RequestPowerCycleTime > 6 ):
	InstrPwrEnableA = 1
	fFileUpdate( 1 )
	RequestPowerCycleTime = 0
	RequestPowerOff = 0
	RequestPowerCycle = 0

    """
    if( InstrPwrEnableA == -1 ):
	InstrPwrEnableA = SCE_IN_STATUS.InstrPwrEnableA
    if( InstrPwrEnableB == -1 ):
	InstrPwrEnableB = SCE_IN_STATUS.InstrPwrEnableB
    """

    sce_in_status = 0
    if( DecStatus_SPPCmd_EmulatorType == 0 ):
	SCE_IN_STATUS.ReasonCode = SPPBios.STATUS_REASON_CODE_TIME_PULSE
	SCE_IN_STATUS.FifoCmdSync = 1
	SCE_IN_STATUS.FifoCtrlSync = 1
	SCE_IN_STATUS.FifoCmdFrameCnt = iCount
	SCE_IN_STATUS.FifoCtrlFrameCnt = iCount
	SCE_IN_STATUS.FifoTlmFrameCnt = iCount
	SCE_IN_STATUS.FifoStatusFrameCnt = iCount

	SCE_IN_STATUS.MajorFrameCurr = iCount
	SCE_IN_STATUS.MajorFrameTop = iCount
	SCE_IN_STATUS.MajorFrameDelay = 1
	SCE_IN_STATUS.InstrPwrEnableA = InstrPwrEnableA 
	SCE_IN_STATUS.InstrPwrEnableB = InstrPwrEnableB 
	SCE_IN_STATUS.ActiveSide = ActiveSide 
	SCE_IN_STATUS.FrontPanelPwrEnable = 1
	SCE_IN_STATUS.send(1)
	sce_in_status = 1

    else:
	if( SCE_IN_STATUS.InstrPwrEnableA != InstrPwrEnableA ):
	    if( InstrPwrEnableA ):
		HostCommands.fSetMacroMode("")	# In case a macro gets opened immediately before a power change.
		GseosCmd.ExecCmd( "SCE_CTRL_ENABLE_INSTR_A_POWER()" )
	    else:
		HostCommands.fSetMacroMode("")	# In case a macro gets opened immediately before a power change.
		GseosCmd.ExecCmd( "SCE_CTRL_DISABLE_INSTR_A_POWER()" )

    global WBS_TimeTag, WBS_Valid
    global WS_TimeTag, WS_Valid
    if( WBS_TimeTag != LOR_Boot_Status.TimeTag ):
	WBS_TimeTag = LOR_Boot_Status.TimeTag
	WBS_Valid = 1
    else:
	WBS_Valid = 0

    global WS_TimeTag, WS_Valid
    if( WS_TimeTag != LOR_Status.TimeTag ):
	WS_TimeTag = LOR_Status.TimeTag
	WS_Valid = 1
    else:
	WS_Valid = 0

    SCE_IN_ANALOG.InstrVolts = 0
    SCE_IN_ANALOG.InstrCurr = 0
    if( WBS_Valid ):
	SCE_IN_ANALOG.InstrVolts = 2800
	SCE_IN_ANALOG.InstrCurr = 90
    if( WS_Valid ):
	SCE_IN_ANALOG.InstrVolts = 2800
	SCE_IN_ANALOG.InstrCurr = 90
	SCE_IN_ANALOG.InstrCurr = 290

    iM = (iCount & 1)
    iM = 1
    sce_in_analog = 0
    if( DecStatus_SPPCmd_EmulatorType != 2 ):
	SCE_IN_ANALOG.BusVolts = 2800
	SCE_IN_ANALOG.AuxVolts = 2800 * iM
	SCE_IN_ANALOG.AuxCurr = 200 * iM
	SCE_IN_ANALOG.PeakBusVolts = 2800 * iM
	SCE_IN_ANALOG.PeakInstrVolts = 2800 * iM
	SCE_IN_ANALOG.PeakInstrCurr = 200 * iM
	SCE_IN_ANALOG.PeakAuxVolts = 2800 * iM
	SCE_IN_ANALOG.PeakAuxCurr = 200 * iM
	SCE_IN_ANALOG.Temp0 = 9999 * iM
	SCE_IN_ANALOG.Temp1 = 9999 * iM
	SCE_IN_ANALOG.Temp2 = 9999 * iM
	SCE_IN_ANALOG.Temp3 = 9999 * iM
	SCE_IN_ANALOG.Temp4 = 9999 * iM
	SCE_IN_ANALOG.Temp5 = 9999 * iM
	SCE_IN_ANALOG.Temp6 = 9999 * iM
	SCE_IN_ANALOG.Temp7 = 9999 * iM
	SCE_IN_ANALOG.PotADTest = 9999 * iM
	SCE_IN_ANALOG.PotADTest1 = 9999 * iM
	SCE_IN_ANALOG.PotADTest2 = 9999 * iM
	SCE_IN_ANALOG.send(1)
	sce_in_analog = 1

    iCount = iCount+1
    if( iCount == 2 ):
	print 'Emulator type: ', DecStatus_SPPCmd_EmulatorType
	print 'Support for spacecraft power requests installed.\n'
        if( DecStatus_SPPCmd_EmulatorType == 0 ):
	    print '1PPS Simulation Installed successfully.\n'
        if( sce_in_status ):
            print 'Sending SCE_IN_STATUS'
        if( sce_in_analog ):
            print 'Sending SCE_IN_ANALOG'
	    GseosCmd.ExecCmd ( "SCE_CTRL_SET_ANALOG_UPDATE_TIME(0x7FFFFFFF)" )

    LOR_LOS.Value = iModeSelect
    LOR_LOS.send(0)

m_fTrigger = TMonitor( 'FakePPS', fTrigger )
DSACtrl.Monitors.append( m_fTrigger )
LOR_Boot_Status.Monitors.append( m_fTrigger )
LOR_Status.Monitors.append( m_fTrigger )

def fFileUpdate( iOut ):
    if( DecStatus_SPPCmd_EmulatorType == 0 ):
	sPowerstate = Gseos.GetProjectPath() + '/powerstate.txt'
	fx = open( sPowerstate, 'a' )
	fx.write( '%d\n' % iOut )
	fx.close()

def fCatchCmd( oBinCmd ):
    global InstrPwrEnableA, InstrPwrEnableB , ActiveSide
    global dUptime, Uptime
    try:
	## print '0x%08x' % oBinCmd.Channel 
	if( oBinCmd.Channel != 0x100 ):
	    return
	sBinCmd = pack( '12B', *oBinCmd.CmdData[0:12] )
	nibs = unpack( '>LLL', sBinCmd[0:12] )
	# print 'SCE Request: %08x %08x %08x' % (nibs[0], nibs[1], nibs[2])

	if( nibs[0] == 0x10 ):
	    if( (nibs[1] == 0x800) and (nibs[2] == 0x800) ):
		InstrPwrEnableA = 1
		fFileUpdate( 1 )
		dUptime = 1
		## Uptime = 0 
		### print "ON 1" 
	    if( (nibs[1] == 0x000) and (nibs[2] == 0x800) ):
		InstrPwrEnableA = 0
		fFileUpdate( 0 )
		dUptime = 0
		### print "OFF 1" 
	    if( (nibs[1] == 0x400) and (nibs[2] == 0x400) ):
		InstrPwrEnableB = 1
		### fFileUpdate( 1 )
	    if( (nibs[1] == 0x000) and (nibs[2] == 0x400) ):
		InstrPwrEnableB = 0
		### fFileUpdate( 0 )
	if( nibs[0] == 0x14 ):
	    ActiveSide = nibs[1]

    except Exception as E:
    	print E

m_fCatchCmd = TMonitor( 'fCatchCmd', fCatchCmd )
BinCmd.Monitors.append( m_fCatchCmd )

# Support for scripting power and telemetry.
TLMDefault = "A"
def fTLM__Off():
    GseosCmd.ExecCmd( "SCE_CTRL_SWITCH_SIDE(None)" )
def fTLM_Select(Q):
    GseosCmd.ExecCmd( "SCE_CTRL_SWITCH_SIDE(%s)" % Q )
def fTLM_Default():
    GseosCmd.ExecCmd( "SCE_CTRL_SWITCH_SIDE(%s)" % TLMDefault )
def fTLM_SetDefault(Q):
    global TLMDefault
    TLMDefault = Q
def fTLM_GetDefault():
    return( TLMDefault )

def fPower_On():
    global Uptime, dUptime
    GseosCmd.ExecCmd( "SCE_CTRL_ENABLE_INSTR_A_POWER()" )
    ### print "ON 2"
    if( dUptime == 0 ):
	Uptime = 0
    dUptime = 1

def fPower_Off():
    global Uptime, dUptime
    dUptime = 0
    ### print "OFF 2"
    GseosCmd.ExecCmd( "SCE_CTRL_DISABLE_INSTR_A_POWER()" )

def fUptime():
    global Uptime
    return ( Uptime )
