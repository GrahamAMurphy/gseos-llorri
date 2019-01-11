# LLORRI constants

import LLORRI_Bios

# ------------------------------------------------------------------------
# Command constants

# Base APID: start of range of telemetry APIDs; all telecommands use this APID
APID_INSTR = 0x0
APID_INSTR_MAX = APID_INSTR + 0x40 - 1

# Command opcodes:
OP_CMD_WRAP = 0x02
OP_MAC_DEF  = 0x04
OP_MAC_END  = 0x06

OP_MAC_ENDDEF = 0x07
OP_MEM_LOAD = 0x14
OP_MEM_STR_LOAD = 0x18
OP_CMD_TEXT = 0x21

# EXTRAS

# Maximum number of data bytes in MEM_LOAD command
# Note: assumes maximum ITF payload is 500 bytes, 84 bytes
# of which are consumed by the time and status packet.  Also
# assumes two memory load commands are issued per ITF.  This
# results in full use of the command ITF bandwidth.
MAX_MEM_LOAD = 192    # even((500 - 84)/2) - 16

# Command channel number
CMD_CHANNEL = LLORRI_Bios.CMD_CHANNEL_INSTR_CMD

# Define host/instrument for regresstools
instr = 'LOR'; cmdprefix = instr; host = 'Lucy'
instrdir = 'LLORRI'

# ------------------------------------------------------------------------
# Telemetry constants

from __main__ import LOR_CmdEcho, LOR_Alarm, LOR_MemChecksum, LOR_MemDump, \
	LOR_Status, LOR_Boot_Status, LOR_MacroDump, LOR_MacroChecksum, \
	LOR_CmdText

# Dictionary to map data data ids to blocks.
dIdToBlk = {
  1:LOR_CmdEcho,
  2:LOR_Alarm,
  3:LOR_MemChecksum,
  4:LOR_MemDump,
  5:LOR_Status,
  6:LOR_Boot_Status,
  7:LOR_MacroDump,
  8:LOR_MacroChecksum,
 11:LOR_CmdText
}

# Log files
CMDECHOLOG = 'Instruments/LLORRI/Log/Cmd_echo.log'
EVENTLOG = 'Instruments/LLORRI/Log/Event.log'
MACRODUMPLOG = 'Instruments/LLORRI/Log/Macros.log'
LOGSEP = '================================================================\n'
