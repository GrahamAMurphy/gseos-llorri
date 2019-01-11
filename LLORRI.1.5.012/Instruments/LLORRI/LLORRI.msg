Info	12/03/18	12:28:05	GSEOS	0	1	********************************************************************************
Info	12/03/18	12:28:05	GSEOS	0	1	GSEOS 7.1.1150
Info	12/03/18	12:28:05	GSEOS	0	1	LUCY L'LORRI
Info	12/03/18	12:28:05	GSEOS	0	1	Platform: Windows-10-10.0.17134
Info	12/03/18	12:28:05	GSEOS	0	1	Mon Dec 03 12:28:05 2018
Info	12/03/18	12:28:05	GSEOS	0	1	********************************************************************************
Info	12/03/18	12:28:06	Net	0	1	Server connection: CMDServer has been started.
Info	12/03/18	12:28:06	Net	0	1	Server connection: TLMServer has been started.
Info	12/03/18	12:28:06	LLORRI_Bios	0	1	Starting up session for LUCY L'LORRI, Version: 1.5.012
Info	12/03/18	12:28:06	LLORRI_Bios	0	1	******************************************************
Info	12/03/18	12:28:06	LLORRI_Bios	0	1	Loading L'LORRI SCE interface.
Info	12/03/18	12:28:06	LLORRI_Bios	0	1	Configuring for SCE mode.
Info	12/03/18	12:28:06	Message	0	1	Setting Message Filter: "OKBios", Gseos.MSG_ERROR, "Error reading from pipeOut:*".
Info	12/03/18	12:28:06	OKBios	0	1	Initializing device: XEM1
Info	12/03/18	12:28:06	OKBios	0	1	Entering device service thread for device: XEM1.
Info	12/03/18	12:28:07	OKBios	0	1	Device board model: XEM7310-A200.
Info	12/03/18	12:28:07	OKBios	0	1	Setting transfer size to: 16 bytes.
Info	12/03/18	12:28:07	OKBios	0	1	Device: XEM1 (Opal Kelly XEM7310) configured. No bit file loaded.
Error	12/03/18	12:28:08	LLORRI Command	0	1	Major Frame skip detected. Expected major frame: 0. Current major frame: 1463. Resetting expected major frame to 1463.
Info	12/03/18	12:28:08	LLORRI_Bios	0	1	SCE detected to be running...
Info	12/03/18	12:28:08	LLORRI_Bios	0	1	Instrument power switch detected to be off.
Info	12/03/18	12:28:08	LLORRI_Bios	0	1	Resetting FPGA with bitfile: Instruments/LLORRI/top_level_mini.bit...
Info	12/03/18	12:28:10	LLORRI_Bios	0	1	Resetting SCE FPGA.
Info	12/03/18	12:28:10	LLORRI_Bios	0	1	Configuring UART: (115200, o, 1).
Info	12/03/18	12:28:10	LLORRI_Bios	0	1	Configuring minor frame count: 50.
Info	12/03/18	12:28:10	LLORRI_Bios	0	1	Configuring minor frame time: 20 ms.
Info	12/03/18	12:28:10	LLORRI_Bios	0	1	Configuring analog update time: 1000 ms.
Info	12/03/18	12:28:10	LLORRI_Bios	0	1	Configuring instrument voltage limits: 0.00 .. 33.00 V.
Info	12/03/18	12:28:10	LLORRI_Bios	0	1	Configuring instrument current limits: 0.000 .. 2.000 A.
Info	12/03/18	12:28:10	LLORRI_Bios	0	1	Configuring aux voltage limits: 0.00 .. 33.00 V.
Info	12/03/18	12:28:10	LLORRI_Bios	0	1	Configuring aux current limits: 0.000 .. 2.000 A.
Info	12/03/18	12:28:10	LLORRI_Bios	0	1	SCE configuration completed.
Info	12/03/18	12:28:10	LLORRI_Bios	0	1	Starting TLM data acquisition.
Info	12/03/18	12:28:10	Message	0	1	Removing Message Filter: "OKBios", Gseos.MSG_ERROR, "Error reading from pipeOut:*".
Info	12/03/18	12:28:10	Version	0	1	
Info	12/03/18	12:28:10	Version	0	1	Version Control Information
Info	12/03/18	12:28:10	Version	0	1	----------------------------------------------------------------------
Info	12/03/18	12:28:10	Version	0	1	GSEOS:         7.1.1150
Info	12/03/18	12:28:10	Version	0	1	Python:        2.7.12 (default, Sep  8 2016, 19:20:19) [MSC v.1500 32 bit (Intel)]
Info	12/03/18	12:28:10	Version	0	1	ExcelLoad:     3.0.086
Info	12/03/18	12:28:10	Version	0	1	LUCY L'LORRI:  1.5.012
Info	12/03/18	12:28:10	Version	0	1	
Info	12/03/18	12:28:10	Version	0	1	Spreadsheet Version Information
Info	12/03/18	12:28:10	Version	0	2	----------------------------------------------------------------------
Info	12/03/18	12:28:10	Version	0	1	
Info	12/03/18	12:28:08	OKBios	0	1	Device: XEM1 (Opal Kelly XEM7310) configured using bit file: Instruments/LLORRI/top_level_mini.bit.
Info	12/03/18	12:28:11	SCE	0	1	cmd baud=115200 par=O stop=1
Info	12/03/18	12:28:12	SCE	0	1	Minor Frame Time set to 20 ms
Info	12/03/18	12:28:12	SCE	0	1	Acquisition started
Error	12/03/18	12:28:13	LLORRI Command	0	1	Major Frame skip detected. Expected major frame: 1516. Current major frame: 1. Resetting expected major frame to 1.
Error	12/03/18	12:53:37	Cmd	0	1	Error executing Python command 'LOR_CMD_WRAP_0(01)': name 'LOR_CMD_WRAP_0' is not defined
Error	12/03/18	12:53:37	Cmd	0	1	Traceback (most recent call last):
Error	12/03/18	12:53:37	Cmd	0	1	File "<string>", line 1, in <module>
Error	12/03/18	12:53:37	Cmd	0	1	NameError: name 'LOR_CMD_WRAP_0' is not defined
Error	12/03/18	12:55:08	Cmd	0	1	Error executing Python command 'LOR_CMD_WRAP_1(01,0x34)': name 'LOR_CMD_WRAP_1' is not defined
Error	12/03/18	12:55:08	Cmd	0	1	Traceback (most recent call last):
Error	12/03/18	12:55:08	Cmd	0	1	File "<string>", line 1, in <module>
Error	12/03/18	12:55:08	Cmd	0	1	NameError: name 'LOR_CMD_WRAP_1' is not defined
Info	12/03/18	12:59:42	GSEOS	0	1	********************************************************************************
Info	12/03/18	12:59:42	GSEOS	0	1	GSEOS 7.1.1150
Info	12/03/18	12:59:42	GSEOS	0	1	LUCY L'LORRI
Info	12/03/18	12:59:42	GSEOS	0	1	Platform: Windows-10-10.0.17134
Info	12/03/18	12:59:42	GSEOS	0	1	Mon Dec 03 12:59:43 2018
Info	12/03/18	12:59:42	GSEOS	0	1	********************************************************************************
Info	12/03/18	12:59:43	Net	0	1	Server connection: CMDServer has been started.
Info	12/03/18	12:59:43	Net	0	1	Server connection: TLMServer has been started.
Info	12/03/18	12:59:44	LLORRI_Bios	0	1	Starting up session for LUCY L'LORRI, Version: 1.5.012
Info	12/03/18	12:59:44	LLORRI_Bios	0	1	******************************************************
Info	12/03/18	12:59:44	LLORRI_Bios	0	1	Loading L'LORRI SCE interface.
Info	12/03/18	12:59:44	LLORRI_Bios	0	1	Configuring for SCE mode.
Info	12/03/18	12:59:44	Message	0	1	Setting Message Filter: "OKBios", Gseos.MSG_ERROR, "Error reading from pipeOut:*".
Info	12/03/18	12:59:44	OKBios	0	1	Initializing device: XEM1
Info	12/03/18	12:59:44	OKBios	0	1	Entering device service thread for device: XEM1.
Info	12/03/18	12:59:44	OKBios	0	1	Device board model: XEM7310-A200.
Info	12/03/18	12:59:44	OKBios	0	1	Setting transfer size to: 16 bytes.
Info	12/03/18	12:59:44	OKBios	0	1	Device: XEM1 (Opal Kelly XEM7310) configured. No bit file loaded.
Error	12/03/18	12:59:45	LLORRI Command	0	1	Major Frame skip detected. Expected major frame: 0. Current major frame: 1635. Resetting expected major frame to 1635.
Error	12/03/18	12:59:45	LLORRI Command	0	1	Major Frame skip detected. Expected major frame: 1687. Current major frame: 768. Resetting expected major frame to 768.
Error	12/03/18	12:59:45	LLORRI Command	0	1	Major Frame skip detected. Expected major frame: 771. Current major frame: 1894. Resetting expected major frame to 1894.
Info	12/03/18	12:59:45	LLORRI_Bios	0	1	SCE detected to be running...
Info	12/03/18	12:59:45	LLORRI_Bios	0	1	Instrument power switch detected to be off.
Info	12/03/18	12:59:45	LLORRI_Bios	0	1	Resetting FPGA with bitfile: Instruments/LLORRI/top_level_mini.bit...
Info	12/03/18	12:59:47	LLORRI_Bios	0	1	Resetting SCE FPGA.
Info	12/03/18	12:59:47	LLORRI_Bios	0	1	Configuring UART: (115200, o, 1).
Info	12/03/18	12:59:47	LLORRI_Bios	0	1	Configuring minor frame count: 50.
Info	12/03/18	12:59:47	LLORRI_Bios	0	1	Configuring minor frame time: 20 ms.
Info	12/03/18	12:59:47	LLORRI_Bios	0	1	Configuring analog update time: 1000 ms.
Info	12/03/18	12:59:47	LLORRI_Bios	0	1	Configuring instrument voltage limits: 0.00 .. 33.00 V.
Info	12/03/18	12:59:47	LLORRI_Bios	0	1	Configuring instrument current limits: 0.000 .. 2.000 A.
Info	12/03/18	12:59:47	LLORRI_Bios	0	1	Configuring aux voltage limits: 0.00 .. 33.00 V.
Info	12/03/18	12:59:47	LLORRI_Bios	0	1	Configuring aux current limits: 0.000 .. 2.000 A.
Info	12/03/18	12:59:47	LLORRI_Bios	0	1	SCE configuration completed.
Info	12/03/18	12:59:47	LLORRI_Bios	0	1	Starting TLM data acquisition.
Info	12/03/18	12:59:47	Message	0	1	Removing Message Filter: "OKBios", Gseos.MSG_ERROR, "Error reading from pipeOut:*".
Info	12/03/18	12:59:47	Version	0	1	
Info	12/03/18	12:59:47	Version	0	1	Version Control Information
Info	12/03/18	12:59:47	Version	0	1	----------------------------------------------------------------------
Info	12/03/18	12:59:47	Version	0	1	GSEOS:         7.1.1150
Info	12/03/18	12:59:47	Version	0	1	Python:        2.7.12 (default, Sep  8 2016, 19:20:19) [MSC v.1500 32 bit (Intel)]
Info	12/03/18	12:59:47	Version	0	1	ExcelLoad:     3.0.086
Info	12/03/18	12:59:47	Version	0	1	LUCY L'LORRI:  1.5.012
Info	12/03/18	12:59:47	Version	0	1	
Info	12/03/18	12:59:47	Version	0	1	Spreadsheet Version Information
Info	12/03/18	12:59:47	Version	0	2	----------------------------------------------------------------------
Info	12/03/18	12:59:47	Version	0	1	
Info	12/03/18	12:59:46	OKBios	0	1	Device: XEM1 (Opal Kelly XEM7310) configured using bit file: Instruments/LLORRI/top_level_mini.bit.
Info	12/03/18	12:59:48	SCE	0	1	Bitfile version number 004
Info	12/03/18	12:59:48	SCE	0	1	cmd baud=115200 par=O stop=1
Error	12/03/18	12:59:48	CIP Decoder	0	1	UDP checksum error. Expected: 0x8CEA, received: 0x44BC.
Info	12/03/18	12:59:49	SCE	0	1	Minor Frame Time set to 20 ms
Info	12/03/18	12:59:49	SCE	0	1	Acquisition started
Error	12/03/18	12:59:50	LLORRI Command	0	1	Major Frame skip detected. Expected major frame: 1897. Current major frame: 1. Resetting expected major frame to 1.
Error	12/03/18	14:14:11	Packet Decoder	0	1	Telemetry error: unknown APID: 0x012
Info	12/19/18	13:57:47	GSEOS	0	1	********************************************************************************
Info	12/19/18	13:57:47	GSEOS	0	1	GSEOS 7.1.1150
Info	12/19/18	13:57:47	GSEOS	0	1	LUCY L'LORRI
Info	12/19/18	13:57:47	GSEOS	0	1	Platform: Windows-10-10.0.17134
Info	12/19/18	13:57:47	GSEOS	0	1	Wed Dec 19 13:57:50 2018
Info	12/19/18	13:57:47	GSEOS	0	1	********************************************************************************
Info	12/19/18	13:57:52	Net	0	1	Server connection: CMDServer has been started.
Info	12/19/18	13:57:52	Net	0	1	Server connection: TLMServer has been started.
Info	12/19/18	13:58:01	LLORRI_Bios	0	1	Starting up session for LUCY L'LORRI, Version: 1.5.012
Info	12/19/18	13:58:01	LLORRI_Bios	0	1	******************************************************
Info	12/19/18	13:58:01	LLORRI_Bios	0	1	Loading L'LORRI SCE interface.
Info	12/19/18	13:58:01	LLORRI_Bios	0	1	Configuring for SCE mode.
Info	12/19/18	13:58:01	Message	0	1	Setting Message Filter: "OKBios", Gseos.MSG_ERROR, "Error reading from pipeOut:*".
Info	12/19/18	13:58:01	OKBios	0	1	Initializing device: XEM1
Info	12/19/18	13:58:01	OKBios	0	1	Entering device service thread for device: XEM1.
Error	12/19/18	13:58:02	OKBios	0	1	Error loading OKBios: Error initializing device: XEM1: No Opal Kelly FrontPanel devices found.
Error	12/19/18	13:58:02	LLORRI_Bios	0	1	Error importing module OKBios: Error initializing device: XEM1: No Opal Kelly FrontPanel devices found..
Info	12/19/18	13:58:02	Message	0	1	Removing Message Filter: "OKBios", Gseos.MSG_ERROR, "Error reading from pipeOut:*".
Info	12/19/18	13:58:02	Version	0	1	
Info	12/19/18	13:58:02	Version	0	1	Version Control Information
Info	12/19/18	13:58:02	Version	0	1	----------------------------------------------------------------------
Info	12/19/18	13:58:02	Version	0	1	GSEOS:         7.1.1150
Info	12/19/18	13:58:02	Version	0	1	Python:        2.7.12 (default, Sep  8 2016, 19:20:19) [MSC v.1500 32 bit (Intel)]
Info	12/19/18	13:58:02	Version	0	1	ExcelLoad:     3.0.086
Info	12/19/18	13:58:02	Version	0	1	LUCY L'LORRI:  1.5.012
Info	12/19/18	13:58:02	Version	0	1	
Info	12/19/18	13:58:02	Version	0	1	Spreadsheet Version Information
Info	12/19/18	13:58:02	Version	0	2	----------------------------------------------------------------------
Info	12/19/18	13:58:02	Version	0	1	
Info	12/19/18	13:58:02	OKBios	0	1	Device service thread for device: XEM1 terminated.
Info	12/19/18	14:10:01	GSEOS	0	1	********************************************************************************
Info	12/19/18	14:10:01	GSEOS	0	1	GSEOS 7.1.1150
Info	12/19/18	14:10:01	GSEOS	0	1	LUCY L'LORRI
Info	12/19/18	14:10:01	GSEOS	0	1	Platform: Windows-10-10.0.17134
Info	12/19/18	14:10:01	GSEOS	0	1	Wed Dec 19 14:10:03 2018
Info	12/19/18	14:10:01	GSEOS	0	1	********************************************************************************
Info	12/19/18	14:10:04	Net	0	1	Server connection: CMDServer has been started.
Info	12/19/18	14:10:04	Net	0	1	Server connection: TLMServer has been started.
Info	12/19/18	14:10:06	LLORRI_Bios	0	1	Starting up session for LUCY L'LORRI, Version: 1.5.012
Info	12/19/18	14:10:06	LLORRI_Bios	0	1	******************************************************
Info	12/19/18	14:10:06	LLORRI_Bios	0	1	Loading L'LORRI SCE interface.
Info	12/19/18	14:10:06	LLORRI_Bios	0	1	Configuring for SCE mode.
Info	12/19/18	14:10:06	Message	0	1	Setting Message Filter: "OKBios", Gseos.MSG_ERROR, "Error reading from pipeOut:*".
Info	12/19/18	14:10:06	OKBios	0	1	Initializing device: XEM1
Info	12/19/18	14:10:06	OKBios	0	1	Entering device service thread for device: XEM1.
Error	12/19/18	14:10:06	OKBios	0	1	Error loading OKBios: Error initializing device: XEM1: No Opal Kelly FrontPanel devices found.
Error	12/19/18	14:10:06	LLORRI_Bios	0	1	Error importing module OKBios: Error initializing device: XEM1: No Opal Kelly FrontPanel devices found..
Info	12/19/18	14:10:06	Message	0	1	Removing Message Filter: "OKBios", Gseos.MSG_ERROR, "Error reading from pipeOut:*".
Info	12/19/18	14:10:06	Version	0	1	
Info	12/19/18	14:10:06	Version	0	1	Version Control Information
Info	12/19/18	14:10:06	Version	0	1	----------------------------------------------------------------------
Info	12/19/18	14:10:06	Version	0	1	GSEOS:         7.1.1150
Info	12/19/18	14:10:06	Version	0	1	Python:        2.7.12 (default, Sep  8 2016, 19:20:19) [MSC v.1500 32 bit (Intel)]
Info	12/19/18	14:10:06	Version	0	1	ExcelLoad:     3.0.086
Info	12/19/18	14:10:06	Version	0	1	LUCY L'LORRI:  1.5.012
Info	12/19/18	14:10:06	Version	0	1	
Info	12/19/18	14:10:06	Version	0	1	Spreadsheet Version Information
Info	12/19/18	14:10:06	Version	0	2	----------------------------------------------------------------------
Info	12/19/18	14:10:06	Version	0	1	
Info	12/19/18	14:10:06	OKBios	0	1	Device service thread for device: XEM1 terminated.
Info	12/19/18	14:11:31	GSEOS	0	1	********************************************************************************
Info	12/19/18	14:11:31	GSEOS	0	1	GSEOS 7.1.1150
Info	12/19/18	14:11:31	GSEOS	0	1	LUCY L'LORRI
Info	12/19/18	14:11:31	GSEOS	0	1	Platform: Windows-10-10.0.17134
Info	12/19/18	14:11:31	GSEOS	0	1	Wed Dec 19 14:11:32 2018
Info	12/19/18	14:11:31	GSEOS	0	1	********************************************************************************
Info	12/19/18	14:11:32	Net	0	1	Server connection: CMDServer has been started.
Info	12/19/18	14:11:32	Net	0	1	Server connection: TLMServer has been started.
Info	12/19/18	14:11:33	LLORRI_Bios	0	1	Starting up session for LUCY L'LORRI, Version: 1.5.012
Info	12/19/18	14:11:33	LLORRI_Bios	0	1	******************************************************
Info	12/19/18	14:11:33	LLORRI_Bios	0	1	Loading L'LORRI SCE interface.
Info	12/19/18	14:11:33	LLORRI_Bios	0	1	Configuring for SCE mode.
Info	12/19/18	14:11:33	Message	0	1	Setting Message Filter: "OKBios", Gseos.MSG_ERROR, "Error reading from pipeOut:*".
Info	12/19/18	14:11:33	OKBios	0	1	Initializing device: XEM1
Info	12/19/18	14:11:33	OKBios	0	1	Entering device service thread for device: XEM1.
Info	12/19/18	14:11:33	OKBios	0	1	Device board model: XEM7310-A200.
Info	12/19/18	14:11:33	OKBios	0	1	Setting transfer size to: 16 bytes.
Info	12/19/18	14:11:33	OKBios	0	1	Device: XEM1 (Opal Kelly XEM7310) configured. No bit file loaded.
Error	12/19/18	14:11:34	LLORRI Command	0	1	Major Frame skip detected. Expected major frame: 0. Current major frame: 3187. Resetting expected major frame to 3187.
Error	12/19/18	14:11:34	LLORRI Command	0	1	Major Frame skip detected. Expected major frame: 3239. Current major frame: 33751040. Resetting expected major frame to 33751040.
Info	12/19/18	14:11:34	LLORRI_Bios	0	1	SCE detected to be running...
Info	12/19/18	14:11:34	LLORRI_Bios	0	1	Instrument power switch detected to be off.
Info	12/19/18	14:11:34	LLORRI_Bios	0	1	Resetting FPGA with bitfile: Instruments/LLORRI/top_level_mini.bit...
Info	12/19/18	14:11:36	LLORRI_Bios	0	1	Resetting SCE FPGA.
Info	12/19/18	14:11:36	LLORRI_Bios	0	1	Configuring UART: (115200, o, 1).
Info	12/19/18	14:11:36	LLORRI_Bios	0	1	Configuring minor frame count: 50.
Info	12/19/18	14:11:36	LLORRI_Bios	0	1	Configuring minor frame time: 20 ms.
Info	12/19/18	14:11:36	LLORRI_Bios	0	1	Configuring analog update time: 1000 ms.
Info	12/19/18	14:11:36	LLORRI_Bios	0	1	Configuring instrument voltage limits: 0.00 .. 33.00 V.
Info	12/19/18	14:11:36	LLORRI_Bios	0	1	Configuring instrument current limits: 0.000 .. 2.000 A.
Info	12/19/18	14:11:36	LLORRI_Bios	0	1	Configuring aux voltage limits: 0.00 .. 33.00 V.
Info	12/19/18	14:11:36	LLORRI_Bios	0	1	Configuring aux current limits: 0.000 .. 2.000 A.
Info	12/19/18	14:11:36	LLORRI_Bios	0	1	SCE configuration completed.
Info	12/19/18	14:11:36	LLORRI_Bios	0	1	Starting TLM data acquisition.
Info	12/19/18	14:11:36	Message	0	1	Removing Message Filter: "OKBios", Gseos.MSG_ERROR, "Error reading from pipeOut:*".
Info	12/19/18	14:11:36	Version	0	1	
Info	12/19/18	14:11:36	Version	0	1	Version Control Information
Info	12/19/18	14:11:36	Version	0	1	----------------------------------------------------------------------
Info	12/19/18	14:11:36	Version	0	1	GSEOS:         7.1.1150
Info	12/19/18	14:11:36	Version	0	1	Python:        2.7.12 (default, Sep  8 2016, 19:20:19) [MSC v.1500 32 bit (Intel)]
Info	12/19/18	14:11:36	Version	0	1	ExcelLoad:     3.0.086
Info	12/19/18	14:11:36	Version	0	1	LUCY L'LORRI:  1.5.012
Info	12/19/18	14:11:36	Version	0	1	
Info	12/19/18	14:11:36	Version	0	1	Spreadsheet Version Information
Info	12/19/18	14:11:36	Version	0	2	----------------------------------------------------------------------
Info	12/19/18	14:11:36	Version	0	1	
Info	12/19/18	14:11:35	OKBios	0	1	Device: XEM1 (Opal Kelly XEM7310) configured using bit file: Instruments/LLORRI/top_level_mini.bit.
Info	12/19/18	14:11:37	SCE	0	1	cmd baud=115200 par=O stop=1
Info	12/19/18	14:11:38	SCE	0	1	Minor Frame Time set to 20 ms
Info	12/19/18	14:11:38	SCE	0	1	Acquisition started
Info	12/20/18	15:56:05	GSEOS	0	1	********************************************************************************
Info	12/20/18	15:56:05	GSEOS	0	1	GSEOS 7.1.1150
Info	12/20/18	15:56:05	GSEOS	0	1	LUCY L'LORRI
Info	12/20/18	15:56:05	GSEOS	0	1	Platform: Windows-10-10.0.17134
Info	12/20/18	15:56:05	GSEOS	0	1	Thu Dec 20 15:56:06 2018
Info	12/20/18	15:56:05	GSEOS	0	1	********************************************************************************
Info	12/20/18	15:56:07	Net	0	1	Server connection: CMDServer has been started.
Info	12/20/18	15:56:07	Net	0	1	Server connection: TLMServer has been started.
Info	12/20/18	15:56:09	LLORRI_Bios	0	1	Starting up session for LUCY L'LORRI, Version: 1.5.012
Info	12/20/18	15:56:09	LLORRI_Bios	0	1	******************************************************
Info	12/20/18	15:56:09	LLORRI_Bios	0	1	Loading L'LORRI SCE interface.
Info	12/20/18	15:56:09	LLORRI_Bios	0	1	Configuring for SCE mode.
Info	12/20/18	15:56:09	Message	0	1	Setting Message Filter: "OKBios", Gseos.MSG_ERROR, "Error reading from pipeOut:*".
Info	12/20/18	15:56:09	OKBios	0	1	Initializing device: XEM1
Info	12/20/18	15:56:09	OKBios	0	1	Entering device service thread for device: XEM1.
Info	12/20/18	15:56:10	OKBios	0	1	Device board model: XEM7310-A200.
Info	12/20/18	15:56:10	OKBios	0	1	Setting transfer size to: 16 bytes.
Info	12/20/18	15:56:10	OKBios	0	1	Device: XEM1 (Opal Kelly XEM7310) configured. No bit file loaded.
Error	12/20/18	15:56:11	LLORRI Command	0	1	Major Frame skip detected. Expected major frame: 0. Current major frame: 12551. Resetting expected major frame to 12551.
Error	12/20/18	15:56:11	CIP Decoder	0	1	UDP checksum error. Expected: 0x08F8, received: 0x02DC.
Error	12/20/18	15:56:11	LLORRI Command	0	1	Major Frame skip detected. Expected major frame: 12603. Current major frame: 33751040. Resetting expected major frame to 33751040.
Info	12/20/18	15:56:11	LLORRI_Bios	0	1	SCE detected to be running...
Info	12/20/18	15:56:11	LLORRI_Bios	0	1	Instrument power switch detected to be off.
Info	12/20/18	15:56:11	LLORRI_Bios	0	1	Resetting FPGA with bitfile: Instruments/LLORRI/top_level_mini.bit...
Info	12/20/18	15:56:13	LLORRI_Bios	0	1	Resetting SCE FPGA.
Info	12/20/18	15:56:13	LLORRI_Bios	0	1	Configuring UART: (115200, o, 1).
Info	12/20/18	15:56:13	LLORRI_Bios	0	1	Configuring minor frame count: 50.
Info	12/20/18	15:56:13	LLORRI_Bios	0	1	Configuring minor frame time: 20 ms.
Info	12/20/18	15:56:13	LLORRI_Bios	0	1	Configuring analog update time: 1000 ms.
Info	12/20/18	15:56:13	LLORRI_Bios	0	1	Configuring instrument voltage limits: 0.00 .. 33.00 V.
Info	12/20/18	15:56:13	LLORRI_Bios	0	1	Configuring instrument current limits: 0.000 .. 2.000 A.
Info	12/20/18	15:56:13	LLORRI_Bios	0	1	Configuring aux voltage limits: 0.00 .. 33.00 V.
Info	12/20/18	15:56:13	LLORRI_Bios	0	1	Configuring aux current limits: 0.000 .. 2.000 A.
Info	12/20/18	15:56:13	LLORRI_Bios	0	1	SCE configuration completed.
Info	12/20/18	15:56:13	LLORRI_Bios	0	1	Starting TLM data acquisition.
Info	12/20/18	15:56:13	Message	0	1	Removing Message Filter: "OKBios", Gseos.MSG_ERROR, "Error reading from pipeOut:*".
Info	12/20/18	15:56:13	Version	0	1	
Info	12/20/18	15:56:13	Version	0	1	Version Control Information
Info	12/20/18	15:56:13	Version	0	1	----------------------------------------------------------------------
Info	12/20/18	15:56:13	Version	0	1	GSEOS:         7.1.1150
Info	12/20/18	15:56:13	Version	0	1	Python:        2.7.12 (default, Sep  8 2016, 19:20:19) [MSC v.1500 32 bit (Intel)]
Info	12/20/18	15:56:13	Version	0	1	ExcelLoad:     3.0.086
Info	12/20/18	15:56:13	Version	0	1	LUCY L'LORRI:  1.5.012
Info	12/20/18	15:56:13	Version	0	1	
Info	12/20/18	15:56:13	Version	0	1	Spreadsheet Version Information
Info	12/20/18	15:56:13	Version	0	2	----------------------------------------------------------------------
Info	12/20/18	15:56:13	Version	0	1	
Info	12/20/18	15:56:12	OKBios	0	1	Device: XEM1 (Opal Kelly XEM7310) configured using bit file: Instruments/LLORRI/top_level_mini.bit.
Info	12/20/18	15:56:14	SCE	0	1	cmd baud=115200 par=O stop=1
Info	12/20/18	15:56:15	SCE	0	1	Minor Frame Time set to 20 ms
Info	12/20/18	15:56:15	SCE	0	1	Acquisition started
Info	01/04/19	09:59:20	GSEOS	0	1	********************************************************************************
Info	01/04/19	09:59:20	GSEOS	0	1	GSEOS 7.1.1150
Info	01/04/19	09:59:20	GSEOS	0	1	LUCY L'LORRI
Info	01/04/19	09:59:20	GSEOS	0	1	Platform: Windows-10-10.0.17134
Info	01/04/19	09:59:20	GSEOS	0	1	Fri Jan 04 09:59:21 2019
Info	01/04/19	09:59:20	GSEOS	0	1	********************************************************************************
Info	01/04/19	09:59:21	Net	0	1	Server connection: CMDServer has been started.
Info	01/04/19	09:59:21	Net	0	1	Server connection: TLMServer has been started.
Info	01/04/19	09:59:24	LLORRI_Bios	0	1	Starting up session for LUCY L'LORRI, Version: 1.5.012
Info	01/04/19	09:59:24	LLORRI_Bios	0	1	******************************************************
Info	01/04/19	09:59:24	LLORRI_Bios	0	1	Loading L'LORRI SCE interface.
Info	01/04/19	09:59:24	LLORRI_Bios	0	1	Configuring for SCE mode.
Info	01/04/19	09:59:24	Message	0	1	Setting Message Filter: "OKBios", Gseos.MSG_ERROR, "Error reading from pipeOut:*".
Info	01/04/19	09:59:24	OKBios	0	1	Initializing device: XEM1
Info	01/04/19	09:59:24	OKBios	0	1	Entering device service thread for device: XEM1.
Info	01/04/19	09:59:24	OKBios	0	1	Device board model: XEM7310-A200.
Info	01/04/19	09:59:24	OKBios	0	1	Setting transfer size to: 16 bytes.
Info	01/04/19	09:59:24	OKBios	0	1	Device: XEM1 (Opal Kelly XEM7310) configured. No bit file loaded.
Error	01/04/19	09:59:26	LLORRI Command	0	1	Major Frame skip detected. Expected major frame: 0. Current major frame: 24031. Resetting expected major frame to 24031.
Error	01/04/19	09:59:26	LLORRI Command	0	1	Major Frame skip detected. Expected major frame: 24083. Current major frame: 33751040. Resetting expected major frame to 33751040.
Info	01/04/19	09:59:26	LLORRI_Bios	0	1	SCE detected to be running...
Info	01/04/19	09:59:26	LLORRI_Bios	0	1	Instrument power switch detected to be off.
Info	01/04/19	09:59:26	LLORRI_Bios	0	1	Resetting FPGA with bitfile: Instruments/LLORRI/top_level_mini.bit...
Info	01/04/19	09:59:27	LLORRI_Bios	0	1	Resetting SCE FPGA.
Info	01/04/19	09:59:28	LLORRI_Bios	0	1	Configuring UART: (115200, o, 1).
Info	01/04/19	09:59:28	LLORRI_Bios	0	1	Configuring minor frame count: 50.
Info	01/04/19	09:59:28	LLORRI_Bios	0	1	Configuring minor frame time: 20 ms.
Info	01/04/19	09:59:28	LLORRI_Bios	0	1	Configuring analog update time: 1000 ms.
Info	01/04/19	09:59:28	LLORRI_Bios	0	1	Configuring instrument voltage limits: 0.00 .. 33.00 V.
Info	01/04/19	09:59:28	LLORRI_Bios	0	1	Configuring instrument current limits: 0.000 .. 2.000 A.
Info	01/04/19	09:59:28	LLORRI_Bios	0	1	Configuring aux voltage limits: 0.00 .. 33.00 V.
Info	01/04/19	09:59:28	LLORRI_Bios	0	1	Configuring aux current limits: 0.000 .. 2.000 A.
Info	01/04/19	09:59:28	LLORRI_Bios	0	1	SCE configuration completed.
Info	01/04/19	09:59:28	LLORRI_Bios	0	1	Starting TLM data acquisition.
Info	01/04/19	09:59:28	Message	0	1	Removing Message Filter: "OKBios", Gseos.MSG_ERROR, "Error reading from pipeOut:*".
Info	01/04/19	09:59:28	Version	0	1	
Info	01/04/19	09:59:28	Version	0	1	Version Control Information
Info	01/04/19	09:59:28	Version	0	1	----------------------------------------------------------------------
Info	01/04/19	09:59:28	Version	0	1	GSEOS:         7.1.1150
Info	01/04/19	09:59:28	Version	0	1	Python:        2.7.12 (default, Sep  8 2016, 19:20:19) [MSC v.1500 32 bit (Intel)]
Info	01/04/19	09:59:28	Version	0	1	ExcelLoad:     3.0.086
Info	01/04/19	09:59:28	Version	0	1	LUCY L'LORRI:  1.5.012
Info	01/04/19	09:59:28	Version	0	1	
Info	01/04/19	09:59:28	Version	0	1	Spreadsheet Version Information
Info	01/04/19	09:59:28	Version	0	2	----------------------------------------------------------------------
Info	01/04/19	09:59:28	Version	0	1	
Info	01/04/19	09:59:26	OKBios	0	1	Device: XEM1 (Opal Kelly XEM7310) configured using bit file: Instruments/LLORRI/top_level_mini.bit.
Info	01/04/19	09:59:29	SCE	0	1	Bitfile version number 004
Info	01/04/19	09:59:29	SCE	0	1	cmd baud=115200 par=O stop=1
Info	01/04/19	09:59:30	SCE	0	1	Minor Frame Time set to 20 ms
Info	01/04/19	09:59:30	SCE	0	1	Acquisition started
Error	01/04/19	09:59:32	CIP Decoder	0	1	UDP checksum error. Expected: 0x986B, received: 0x07A9.
Error	01/04/19	09:59:34	IP Decoder	0	2	IP sync error at position: 0. Expected: 0x45, received: 0x00.
Info	01/04/19	09:59:59	GSEOS	0	1	********************************************************************************
Info	01/04/19	09:59:59	GSEOS	0	1	GSEOS 7.1.1150
Info	01/04/19	09:59:59	GSEOS	0	1	LUCY L'LORRI
Info	01/04/19	09:59:59	GSEOS	0	1	Platform: Windows-10-10.0.17134
Info	01/04/19	09:59:59	GSEOS	0	1	Fri Jan 04 09:59:59 2019
Info	01/04/19	09:59:59	GSEOS	0	1	********************************************************************************
Info	01/04/19	10:00:00	Net	0	1	Server connection: CMDServer has been started.
Info	01/04/19	10:00:00	Net	0	1	Server connection: TLMServer has been started.
Info	01/04/19	10:00:00	LLORRI_Bios	0	1	Starting up session for LUCY L'LORRI, Version: 1.5.012
Info	01/04/19	10:00:00	LLORRI_Bios	0	1	******************************************************
Info	01/04/19	10:00:00	LLORRI_Bios	0	1	Loading L'LORRI SCE interface.
Info	01/04/19	10:00:00	LLORRI_Bios	0	1	Configuring for SCE mode.
Info	01/04/19	10:00:00	Message	0	1	Setting Message Filter: "OKBios", Gseos.MSG_ERROR, "Error reading from pipeOut:*".
Info	01/04/19	10:00:00	OKBios	0	1	Initializing device: XEM1
Info	01/04/19	10:00:00	OKBios	0	1	Entering device service thread for device: XEM1.
Info	01/04/19	10:00:00	OKBios	0	1	Device board model: XEM7310-A200.
Info	01/04/19	10:00:00	OKBios	0	1	Setting transfer size to: 16 bytes.
Info	01/04/19	10:00:00	OKBios	0	1	Device: XEM1 (Opal Kelly XEM7310) configured. No bit file loaded.
Error	01/04/19	10:00:02	LLORRI Command	0	1	Major Frame skip detected. Expected major frame: 0. Current major frame: 29. Resetting expected major frame to 29.
Info	01/04/19	10:00:02	LLORRI_Bios	0	1	SCE detected to be running...
Info	01/04/19	10:00:02	LLORRI_Bios	0	1	Instrument power switch detected to be off.
Info	01/04/19	10:00:02	LLORRI_Bios	0	1	Resetting FPGA with bitfile: Instruments/LLORRI/top_level_mini.bit...
Info	01/04/19	10:00:04	LLORRI_Bios	0	1	Resetting SCE FPGA.
Info	01/04/19	10:00:04	LLORRI_Bios	0	1	Configuring UART: (115200, o, 1).
Info	01/04/19	10:00:04	LLORRI_Bios	0	1	Configuring minor frame count: 50.
Info	01/04/19	10:00:04	LLORRI_Bios	0	1	Configuring minor frame time: 20 ms.
Info	01/04/19	10:00:04	LLORRI_Bios	0	1	Configuring analog update time: 1000 ms.
Info	01/04/19	10:00:04	LLORRI_Bios	0	1	Configuring instrument voltage limits: 0.00 .. 33.00 V.
Info	01/04/19	10:00:04	LLORRI_Bios	0	1	Configuring instrument current limits: 0.000 .. 2.000 A.
Info	01/04/19	10:00:04	LLORRI_Bios	0	1	Configuring aux voltage limits: 0.00 .. 33.00 V.
Info	01/04/19	10:00:04	LLORRI_Bios	0	1	Configuring aux current limits: 0.000 .. 2.000 A.
Info	01/04/19	10:00:04	LLORRI_Bios	0	1	SCE configuration completed.
Info	01/04/19	10:00:04	LLORRI_Bios	0	1	Starting TLM data acquisition.
Info	01/04/19	10:00:04	Message	0	1	Removing Message Filter: "OKBios", Gseos.MSG_ERROR, "Error reading from pipeOut:*".
Info	01/04/19	10:00:04	Version	0	1	
Info	01/04/19	10:00:04	Version	0	1	Version Control Information
Info	01/04/19	10:00:04	Version	0	1	----------------------------------------------------------------------
Info	01/04/19	10:00:04	Version	0	1	GSEOS:         7.1.1150
Info	01/04/19	10:00:04	Version	0	1	Python:        2.7.12 (default, Sep  8 2016, 19:20:19) [MSC v.1500 32 bit (Intel)]
Info	01/04/19	10:00:04	Version	0	1	ExcelLoad:     3.0.086
Info	01/04/19	10:00:04	Version	0	1	LUCY L'LORRI:  1.5.012
Info	01/04/19	10:00:04	Version	0	1	
Info	01/04/19	10:00:04	Version	0	1	Spreadsheet Version Information
Info	01/04/19	10:00:04	Version	0	2	----------------------------------------------------------------------
Info	01/04/19	10:00:04	Version	0	1	
Info	01/04/19	10:00:02	OKBios	0	1	Device: XEM1 (Opal Kelly XEM7310) configured using bit file: Instruments/LLORRI/top_level_mini.bit.
Info	01/04/19	10:00:05	SCE	0	1	cmd baud=115200 par=O stop=1
Error	01/04/19	10:00:05	CIP Decoder	0	1	UDP checksum error. Expected: 0x18D1, received: 0x0761.
Info	01/04/19	10:00:06	SCE	0	1	Minor Frame Time set to 20 ms
Info	01/04/19	10:00:06	SCE	0	1	Acquisition started
Error	01/04/19	10:00:07	LLORRI Command	0	1	Major Frame skip detected. Expected major frame: 36. Current major frame: 1. Resetting expected major frame to 1.
Info	01/04/19	15:32:41	GSEOS	0	1	********************************************************************************
Info	01/04/19	15:32:41	GSEOS	0	1	GSEOS 7.1.1150
Info	01/04/19	15:32:41	GSEOS	0	1	LUCY L'LORRI
Info	01/04/19	15:32:41	GSEOS	0	1	Platform: Windows-10-10.0.17134
Info	01/04/19	15:32:41	GSEOS	0	1	Fri Jan 04 15:32:41 2019
Info	01/04/19	15:32:41	GSEOS	0	1	********************************************************************************
Info	01/04/19	15:32:42	Net	0	1	Server connection: CMDServer has been started.
Info	01/04/19	15:32:42	Net	0	1	Server connection: TLMServer has been started.
Info	01/04/19	15:32:42	LLORRI_Bios	0	1	Starting up session for LUCY L'LORRI, Version: 1.5.012
Info	01/04/19	15:32:42	LLORRI_Bios	0	1	******************************************************
Info	01/04/19	15:32:42	LLORRI_Bios	0	1	Loading L'LORRI SCE interface.
Info	01/04/19	15:32:42	LLORRI_Bios	0	1	Configuring for SCE mode.
Info	01/04/19	15:32:42	Message	0	1	Setting Message Filter: "OKBios", Gseos.MSG_ERROR, "Error reading from pipeOut:*".
Info	01/04/19	15:32:42	OKBios	0	1	Initializing device: XEM1
Info	01/04/19	15:32:42	OKBios	0	1	Entering device service thread for device: XEM1.
Info	01/04/19	15:32:43	OKBios	0	1	Device board model: XEM7310-A200.
Info	01/04/19	15:32:43	OKBios	0	1	Setting transfer size to: 16 bytes.
Info	01/04/19	15:32:43	OKBios	0	1	Device: XEM1 (Opal Kelly XEM7310) configured. No bit file loaded.
Info	01/04/19	15:32:46	LLORRI_Bios	0	1	SCE detected to be not running. Reset SCE.
Info	01/04/19	15:32:46	LLORRI_Bios	0	1	Resetting FPGA with bitfile: Instruments/LLORRI/top_level_mini.bit...
Info	01/04/19	15:32:47	LLORRI_Bios	0	1	Resetting SCE FPGA.
Info	01/04/19	15:32:48	LLORRI_Bios	0	1	Configuring UART: (115200, o, 1).
Info	01/04/19	15:32:48	LLORRI_Bios	0	1	Configuring minor frame count: 50.
Info	01/04/19	15:32:48	LLORRI_Bios	0	1	Configuring minor frame time: 20 ms.
Info	01/04/19	15:32:48	LLORRI_Bios	0	1	Configuring analog update time: 1000 ms.
Info	01/04/19	15:32:48	LLORRI_Bios	0	1	Configuring instrument voltage limits: 0.00 .. 33.00 V.
Info	01/04/19	15:32:48	LLORRI_Bios	0	1	Configuring instrument current limits: 0.000 .. 2.000 A.
Info	01/04/19	15:32:48	LLORRI_Bios	0	1	Configuring aux voltage limits: 0.00 .. 33.00 V.
Info	01/04/19	15:32:48	LLORRI_Bios	0	1	Configuring aux current limits: 0.000 .. 2.000 A.
Info	01/04/19	15:32:48	LLORRI_Bios	0	1	SCE configuration completed.
Info	01/04/19	15:32:48	LLORRI_Bios	0	1	Starting TLM data acquisition.
Info	01/04/19	15:32:48	Message	0	1	Removing Message Filter: "OKBios", Gseos.MSG_ERROR, "Error reading from pipeOut:*".
Info	01/04/19	15:32:48	Version	0	1	
Info	01/04/19	15:32:48	Version	0	1	Version Control Information
Info	01/04/19	15:32:48	Version	0	1	----------------------------------------------------------------------
Info	01/04/19	15:32:48	Version	0	1	GSEOS:         7.1.1150
Info	01/04/19	15:32:48	Version	0	1	Python:        2.7.12 (default, Sep  8 2016, 19:20:19) [MSC v.1500 32 bit (Intel)]
Info	01/04/19	15:32:48	Version	0	1	ExcelLoad:     3.0.086
Info	01/04/19	15:32:48	Version	0	1	LUCY L'LORRI:  1.5.012
Info	01/04/19	15:32:48	Version	0	1	
Info	01/04/19	15:32:48	Version	0	1	Spreadsheet Version Information
Info	01/04/19	15:32:48	Version	0	2	----------------------------------------------------------------------
Info	01/04/19	15:32:48	Version	0	1	
Info	01/04/19	15:32:46	OKBios	0	1	Device: XEM1 (Opal Kelly XEM7310) configured using bit file: Instruments/LLORRI/top_level_mini.bit.
Info	01/04/19	15:32:48	SCE	0	1	Bitfile version number 004
Info	01/04/19	15:32:49	SCE	0	1	cmd baud=115200 par=O stop=1
Error	01/04/19	15:32:49	GseosGraph	0	1	Can't find graph file: 'Instruments\LLORRI\test.graph'
Info	01/04/19	15:32:49	SCE	0	1	Minor Frame Time set to 20 ms
Info	01/04/19	15:32:50	SCE	0	1	Acquisition started
Error	01/04/19	15:32:51	LLORRI Command	0	1	Major Frame skip detected. Expected major frame: 0. Current major frame: 1. Resetting expected major frame to 1.
Info	01/04/19	15:37:41	GSEOS	0	1	********************************************************************************
Info	01/04/19	15:37:41	GSEOS	0	1	GSEOS 7.1.1150
Info	01/04/19	15:37:41	GSEOS	0	1	LUCY L'LORRI
Info	01/04/19	15:37:41	GSEOS	0	1	Platform: Windows-10-10.0.17134
Info	01/04/19	15:37:41	GSEOS	0	1	Fri Jan 04 15:37:42 2019
Info	01/04/19	15:37:41	GSEOS	0	1	********************************************************************************
Info	01/04/19	15:37:42	Net	0	1	Server connection: CMDServer has been started.
Info	01/04/19	15:37:42	Net	0	1	Server connection: TLMServer has been started.
Info	01/04/19	15:37:43	LLORRI_Bios	0	1	Starting up session for LUCY L'LORRI, Version: 1.5.012
Info	01/04/19	15:37:43	LLORRI_Bios	0	1	******************************************************
Info	01/04/19	15:37:43	LLORRI_Bios	0	1	Loading L'LORRI SCE interface.
Info	01/04/19	15:37:43	LLORRI_Bios	0	1	Configuring for SCE mode.
Info	01/04/19	15:37:43	Message	0	1	Setting Message Filter: "OKBios", Gseos.MSG_ERROR, "Error reading from pipeOut:*".
Info	01/04/19	15:37:43	OKBios	0	1	Initializing device: XEM1
Info	01/04/19	15:37:43	OKBios	0	1	Entering device service thread for device: XEM1.
Info	01/04/19	15:37:43	OKBios	0	1	Device board model: XEM7310-A200.
Info	01/04/19	15:37:43	OKBios	0	1	Setting transfer size to: 16 bytes.
Info	01/04/19	15:37:43	OKBios	0	1	Device: XEM1 (Opal Kelly XEM7310) configured. No bit file loaded.
Info	01/04/19	15:37:46	LLORRI_Bios	0	1	SCE detected to be not running. Reset SCE.
Info	01/04/19	15:37:46	LLORRI_Bios	0	1	Resetting FPGA with bitfile: Instruments/LLORRI/top_level_mini.bit...
Info	01/04/19	15:37:48	LLORRI_Bios	0	1	Resetting SCE FPGA.
Info	01/04/19	15:37:48	LLORRI_Bios	0	1	Configuring UART: (115200, o, 1).
Info	01/04/19	15:37:48	LLORRI_Bios	0	1	Configuring minor frame count: 50.
Info	01/04/19	15:37:48	LLORRI_Bios	0	1	Configuring minor frame time: 20 ms.
Info	01/04/19	15:37:48	LLORRI_Bios	0	1	Configuring analog update time: 1000 ms.
Info	01/04/19	15:37:48	LLORRI_Bios	0	1	Configuring instrument voltage limits: 0.00 .. 33.00 V.
Info	01/04/19	15:37:48	LLORRI_Bios	0	1	Configuring instrument current limits: 0.000 .. 2.000 A.
Info	01/04/19	15:37:48	LLORRI_Bios	0	1	Configuring aux voltage limits: 0.00 .. 33.00 V.
Info	01/04/19	15:37:48	LLORRI_Bios	0	1	Configuring aux current limits: 0.000 .. 2.000 A.
Info	01/04/19	15:37:48	LLORRI_Bios	0	1	SCE configuration completed.
Info	01/04/19	15:37:48	LLORRI_Bios	0	1	Starting TLM data acquisition.
Info	01/04/19	15:37:48	Message	0	1	Removing Message Filter: "OKBios", Gseos.MSG_ERROR, "Error reading from pipeOut:*".
Info	01/04/19	15:37:48	Version	0	1	
Info	01/04/19	15:37:48	Version	0	1	Version Control Information
Info	01/04/19	15:37:48	Version	0	1	----------------------------------------------------------------------
Info	01/04/19	15:37:48	Version	0	1	GSEOS:         7.1.1150
Info	01/04/19	15:37:48	Version	0	1	Python:        2.7.12 (default, Sep  8 2016, 19:20:19) [MSC v.1500 32 bit (Intel)]
Info	01/04/19	15:37:48	Version	0	1	ExcelLoad:     3.0.086
Info	01/04/19	15:37:48	Version	0	1	LUCY L'LORRI:  1.5.012
Info	01/04/19	15:37:48	Version	0	1	
Info	01/04/19	15:37:48	Version	0	1	Spreadsheet Version Information
Info	01/04/19	15:37:48	Version	0	2	----------------------------------------------------------------------
Info	01/04/19	15:37:48	Version	0	1	
Info	01/04/19	15:37:47	OKBios	0	1	Device: XEM1 (Opal Kelly XEM7310) configured using bit file: Instruments/LLORRI/top_level_mini.bit.
Info	01/04/19	15:37:49	SCE	0	1	Bitfile version number 004
Info	01/04/19	15:37:49	SCE	0	1	cmd baud=115200 par=O stop=1
Info	01/04/19	15:37:50	SCE	0	1	Minor Frame Time set to 20 ms
Info	01/04/19	15:37:50	SCE	0	1	Acquisition started
Error	01/04/19	15:37:51	LLORRI Command	0	1	Major Frame skip detected. Expected major frame: 0. Current major frame: 1. Resetting expected major frame to 1.
Info	01/04/19	15:39:14	GSEOS	0	1	********************************************************************************
Info	01/04/19	15:39:14	GSEOS	0	1	GSEOS 7.1.1150
Info	01/04/19	15:39:14	GSEOS	0	1	LUCY L'LORRI
Info	01/04/19	15:39:14	GSEOS	0	1	Platform: Windows-10-10.0.17134
Info	01/04/19	15:39:14	GSEOS	0	1	Fri Jan 04 15:39:15 2019
Info	01/04/19	15:39:14	GSEOS	0	1	********************************************************************************
Info	01/04/19	15:39:15	Net	0	1	Server connection: CMDServer has been started.
Info	01/04/19	15:39:15	Net	0	1	Server connection: TLMServer has been started.
Info	01/04/19	15:39:15	LLORRI_Bios	0	1	Starting up session for LUCY L'LORRI, Version: 1.5.012
Info	01/04/19	15:39:15	LLORRI_Bios	0	1	******************************************************
Info	01/04/19	15:39:15	LLORRI_Bios	0	1	Loading L'LORRI SCE interface.
Info	01/04/19	15:39:15	LLORRI_Bios	0	1	Configuring for SCE mode.
Info	01/04/19	15:39:15	Message	0	1	Setting Message Filter: "OKBios", Gseos.MSG_ERROR, "Error reading from pipeOut:*".
Info	01/04/19	15:39:15	OKBios	0	1	Initializing device: XEM1
Info	01/04/19	15:39:15	OKBios	0	1	Entering device service thread for device: XEM1.
Info	01/04/19	15:39:16	OKBios	0	1	Device board model: XEM7310-A200.
Info	01/04/19	15:39:16	OKBios	0	1	Setting transfer size to: 16 bytes.
Info	01/04/19	15:39:16	OKBios	0	1	Device: XEM1 (Opal Kelly XEM7310) configured. No bit file loaded.
Error	01/04/19	15:39:17	LLORRI Command	0	1	Major Frame skip detected. Expected major frame: 0. Current major frame: 79. Resetting expected major frame to 79.
Info	01/04/19	15:39:17	LLORRI_Bios	0	1	SCE detected to be running...
Info	01/04/19	15:39:17	LLORRI_Bios	0	1	Instrument power switch detected to be off.
Info	01/04/19	15:39:17	LLORRI_Bios	0	1	Resetting FPGA with bitfile: Instruments/LLORRI/top_level_mini.bit...
Info	01/04/19	15:39:19	LLORRI_Bios	0	1	Resetting SCE FPGA.
Info	01/04/19	15:39:19	LLORRI_Bios	0	1	Configuring UART: (115200, o, 1).
Info	01/04/19	15:39:19	LLORRI_Bios	0	1	Configuring minor frame count: 50.
Info	01/04/19	15:39:19	LLORRI_Bios	0	1	Configuring minor frame time: 20 ms.
Info	01/04/19	15:39:19	LLORRI_Bios	0	1	Configuring analog update time: 1000 ms.
Info	01/04/19	15:39:19	LLORRI_Bios	0	1	Configuring instrument voltage limits: 0.00 .. 33.00 V.
Info	01/04/19	15:39:19	LLORRI_Bios	0	1	Configuring instrument current limits: 0.000 .. 2.000 A.
Info	01/04/19	15:39:19	LLORRI_Bios	0	1	Configuring aux voltage limits: 0.00 .. 33.00 V.
Info	01/04/19	15:39:19	LLORRI_Bios	0	1	Configuring aux current limits: 0.000 .. 2.000 A.
Info	01/04/19	15:39:19	LLORRI_Bios	0	1	SCE configuration completed.
Info	01/04/19	15:39:19	LLORRI_Bios	0	1	Starting TLM data acquisition.
Info	01/04/19	15:39:19	Message	0	1	Removing Message Filter: "OKBios", Gseos.MSG_ERROR, "Error reading from pipeOut:*".
Info	01/04/19	15:39:19	Version	0	1	
Info	01/04/19	15:39:19	Version	0	1	Version Control Information
Info	01/04/19	15:39:19	Version	0	1	----------------------------------------------------------------------
Info	01/04/19	15:39:19	Version	0	1	GSEOS:         7.1.1150
Info	01/04/19	15:39:19	Version	0	1	Python:        2.7.12 (default, Sep  8 2016, 19:20:19) [MSC v.1500 32 bit (Intel)]
Info	01/04/19	15:39:19	Version	0	1	ExcelLoad:     3.0.086
Info	01/04/19	15:39:19	Version	0	1	LUCY L'LORRI:  1.5.012
Info	01/04/19	15:39:19	Version	0	1	
Info	01/04/19	15:39:19	Version	0	1	Spreadsheet Version Information
Info	01/04/19	15:39:19	Version	0	2	----------------------------------------------------------------------
Info	01/04/19	15:39:19	Version	0	1	
Info	01/04/19	15:39:18	OKBios	0	1	Device: XEM1 (Opal Kelly XEM7310) configured using bit file: Instruments/LLORRI/top_level_mini.bit.
Info	01/04/19	15:39:20	SCE	0	1	Bitfile version number 004
Info	01/04/19	15:39:20	SCE	0	1	cmd baud=115200 par=O stop=1
Info	01/04/19	15:39:21	SCE	0	1	Minor Frame Time set to 20 ms
Info	01/04/19	15:39:21	SCE	0	1	Acquisition started
Error	01/04/19	15:39:22	LLORRI Command	0	1	Major Frame skip detected. Expected major frame: 91. Current major frame: 1. Resetting expected major frame to 1.
Info	01/04/19	15:39:55	GSEOS	0	1	********************************************************************************
Info	01/04/19	15:39:55	GSEOS	0	1	GSEOS 7.1.1150
Info	01/04/19	15:39:55	GSEOS	0	1	LUCY L'LORRI
Info	01/04/19	15:39:55	GSEOS	0	1	Platform: Windows-10-10.0.17134
Info	01/04/19	15:39:55	GSEOS	0	1	Fri Jan 04 15:39:55 2019
Info	01/04/19	15:39:55	GSEOS	0	1	********************************************************************************
Info	01/04/19	15:39:55	Net	0	1	Server connection: CMDServer has been started.
Info	01/04/19	15:39:55	Net	0	1	Server connection: TLMServer has been started.
Info	01/04/19	15:39:56	LLORRI_Bios	0	1	Starting up session for LUCY L'LORRI, Version: 1.5.012
Info	01/04/19	15:39:56	LLORRI_Bios	0	1	******************************************************
Info	01/04/19	15:39:56	LLORRI_Bios	0	1	Loading L'LORRI SCE interface.
Info	01/04/19	15:39:56	LLORRI_Bios	0	1	Configuring for SCE mode.
Info	01/04/19	15:39:56	Message	0	1	Setting Message Filter: "OKBios", Gseos.MSG_ERROR, "Error reading from pipeOut:*".
Info	01/04/19	15:39:56	OKBios	0	1	Initializing device: XEM1
Info	01/04/19	15:39:56	OKBios	0	1	Entering device service thread for device: XEM1.
Info	01/04/19	15:39:56	OKBios	0	1	Device board model: XEM7310-A200.
Info	01/04/19	15:39:56	OKBios	0	1	Setting transfer size to: 16 bytes.
Info	01/04/19	15:39:56	OKBios	0	1	Device: XEM1 (Opal Kelly XEM7310) configured. No bit file loaded.
Info	01/04/19	15:39:59	LLORRI_Bios	0	1	SCE detected to be not running. Reset SCE.
Info	01/04/19	15:39:59	LLORRI_Bios	0	1	Resetting FPGA with bitfile: Instruments/LLORRI/top_level_mini.bit...
Info	01/04/19	15:40:01	LLORRI_Bios	0	1	Resetting SCE FPGA.
Info	01/04/19	15:40:01	LLORRI_Bios	0	1	Configuring UART: (115200, o, 1).
Info	01/04/19	15:40:01	LLORRI_Bios	0	1	Configuring minor frame count: 50.
Info	01/04/19	15:40:01	LLORRI_Bios	0	1	Configuring minor frame time: 20 ms.
Info	01/04/19	15:40:01	LLORRI_Bios	0	1	Configuring analog update time: 1000 ms.
Info	01/04/19	15:40:01	LLORRI_Bios	0	1	Configuring instrument voltage limits: 0.00 .. 33.00 V.
Info	01/04/19	15:40:01	LLORRI_Bios	0	1	Configuring instrument current limits: 0.000 .. 2.000 A.
Info	01/04/19	15:40:01	LLORRI_Bios	0	1	Configuring aux voltage limits: 0.00 .. 33.00 V.
Info	01/04/19	15:40:01	LLORRI_Bios	0	1	Configuring aux current limits: 0.000 .. 2.000 A.
Info	01/04/19	15:40:01	LLORRI_Bios	0	1	SCE configuration completed.
Info	01/04/19	15:40:01	LLORRI_Bios	0	1	Starting TLM data acquisition.
Info	01/04/19	15:40:01	Message	0	1	Removing Message Filter: "OKBios", Gseos.MSG_ERROR, "Error reading from pipeOut:*".
Info	01/04/19	15:40:01	Version	0	1	
Info	01/04/19	15:40:01	Version	0	1	Version Control Information
Info	01/04/19	15:40:01	Version	0	1	----------------------------------------------------------------------
Info	01/04/19	15:40:01	Version	0	1	GSEOS:         7.1.1150
Info	01/04/19	15:40:01	Version	0	1	Python:        2.7.12 (default, Sep  8 2016, 19:20:19) [MSC v.1500 32 bit (Intel)]
Info	01/04/19	15:40:01	Version	0	1	ExcelLoad:     3.0.086
Info	01/04/19	15:40:01	Version	0	1	LUCY L'LORRI:  1.5.012
Info	01/04/19	15:40:01	Version	0	1	
Info	01/04/19	15:40:01	Version	0	1	Spreadsheet Version Information
Info	01/04/19	15:40:01	Version	0	2	----------------------------------------------------------------------
Info	01/04/19	15:40:01	Version	0	1	
Info	01/04/19	15:40:00	OKBios	0	1	Device: XEM1 (Opal Kelly XEM7310) configured using bit file: Instruments/LLORRI/top_level_mini.bit.
Info	01/04/19	15:40:02	SCE	0	1	Bitfile version number 004
Info	01/04/19	15:40:02	SCE	0	1	cmd baud=115200 par=O stop=1
Info	01/04/19	15:40:03	SCE	0	1	Minor Frame Time set to 20 ms
Info	01/04/19	15:40:03	SCE	0	1	Acquisition started
Error	01/04/19	15:40:04	LLORRI Command	0	1	Major Frame skip detected. Expected major frame: 0. Current major frame: 1. Resetting expected major frame to 1.
Info	01/04/19	16:24:09	GSEOS	0	1	********************************************************************************
Info	01/04/19	16:24:09	GSEOS	0	1	GSEOS 7.1.1150
Info	01/04/19	16:24:09	GSEOS	0	1	LUCY L'LORRI
Info	01/04/19	16:24:09	GSEOS	0	1	Platform: Windows-10-10.0.17134
Info	01/04/19	16:24:09	GSEOS	0	1	Fri Jan 04 16:24:10 2019
Info	01/04/19	16:24:09	GSEOS	0	1	********************************************************************************
Info	01/04/19	16:24:10	Net	0	1	Server connection: CMDServer has been started.
Info	01/04/19	16:24:10	Net	0	1	Server connection: TLMServer has been started.
Info	01/04/19	16:24:11	LLORRI_Bios	0	1	Starting up session for LUCY L'LORRI, Version: 1.5.012
Info	01/04/19	16:24:11	LLORRI_Bios	0	1	******************************************************
Info	01/04/19	16:24:11	LLORRI_Bios	0	1	Loading L'LORRI SCE interface.
Info	01/04/19	16:24:11	LLORRI_Bios	0	1	Configuring for SCE mode.
Info	01/04/19	16:24:11	Message	0	1	Setting Message Filter: "OKBios", Gseos.MSG_ERROR, "Error reading from pipeOut:*".
Info	01/04/19	16:24:11	OKBios	0	1	Initializing device: XEM1
Info	01/04/19	16:24:11	OKBios	0	1	Entering device service thread for device: XEM1.
Info	01/04/19	16:24:11	OKBios	0	1	Device board model: XEM7310-A200.
Info	01/04/19	16:24:11	OKBios	0	1	Setting transfer size to: 16 bytes.
Info	01/04/19	16:24:11	OKBios	0	1	Device: XEM1 (Opal Kelly XEM7310) configured. No bit file loaded.
Info	01/04/19	16:24:14	LLORRI_Bios	0	1	SCE detected to be not running. Reset SCE.
Info	01/04/19	16:24:14	LLORRI_Bios	0	1	Resetting FPGA with bitfile: Instruments/LLORRI/top_level_mini.bit...
Info	01/04/19	16:24:16	LLORRI_Bios	0	1	Resetting SCE FPGA.
Info	01/04/19	16:24:16	LLORRI_Bios	0	1	Configuring UART: (115200, o, 1).
Info	01/04/19	16:24:16	LLORRI_Bios	0	1	Configuring minor frame count: 50.
Info	01/04/19	16:24:16	LLORRI_Bios	0	1	Configuring minor frame time: 20 ms.
Info	01/04/19	16:24:16	LLORRI_Bios	0	1	Configuring analog update time: 1000 ms.
Info	01/04/19	16:24:16	LLORRI_Bios	0	1	Configuring instrument voltage limits: 0.00 .. 33.00 V.
Info	01/04/19	16:24:16	LLORRI_Bios	0	1	Configuring instrument current limits: 0.000 .. 2.000 A.
Info	01/04/19	16:24:16	LLORRI_Bios	0	1	Configuring aux voltage limits: 0.00 .. 33.00 V.
Info	01/04/19	16:24:16	LLORRI_Bios	0	1	Configuring aux current limits: 0.000 .. 2.000 A.
Info	01/04/19	16:24:16	LLORRI_Bios	0	1	SCE configuration completed.
Info	01/04/19	16:24:16	LLORRI_Bios	0	1	Starting TLM data acquisition.
Info	01/04/19	16:24:16	Message	0	1	Removing Message Filter: "OKBios", Gseos.MSG_ERROR, "Error reading from pipeOut:*".
Info	01/04/19	16:24:16	Version	0	1	
Info	01/04/19	16:24:16	Version	0	1	Version Control Information
Info	01/04/19	16:24:16	Version	0	1	----------------------------------------------------------------------
Info	01/04/19	16:24:16	Version	0	1	GSEOS:         7.1.1150
Info	01/04/19	16:24:16	Version	0	1	Python:        2.7.12 (default, Sep  8 2016, 19:20:19) [MSC v.1500 32 bit (Intel)]
Info	01/04/19	16:24:16	Version	0	1	ExcelLoad:     3.0.086
Info	01/04/19	16:24:16	Version	0	1	LUCY L'LORRI:  1.5.012
Info	01/04/19	16:24:16	Version	0	1	
Info	01/04/19	16:24:16	Version	0	1	Spreadsheet Version Information
Info	01/04/19	16:24:16	Version	0	2	----------------------------------------------------------------------
Info	01/04/19	16:24:16	Version	0	1	
Info	01/04/19	16:24:15	OKBios	0	1	Device: XEM1 (Opal Kelly XEM7310) configured using bit file: Instruments/LLORRI/top_level_mini.bit.
Info	01/04/19	16:24:17	SCE	0	1	Bitfile version number 004
Info	01/04/19	16:24:17	SCE	0	1	cmd baud=115200 par=O stop=1
Info	01/04/19	16:24:18	SCE	0	1	Minor Frame Time set to 20 ms
Info	01/04/19	16:24:18	SCE	0	1	Acquisition started
Error	01/04/19	16:24:19	LLORRI Command	0	1	Major Frame skip detected. Expected major frame: 0. Current major frame: 1. Resetting expected major frame to 1.
Error	01/04/19	16:26:07	IP Decoder	0	1	IP sync error at position: 0. Expected: 0x45, received: 0x00.
Error	01/04/19	16:26:22	IP Decoder	0	1	IP sync error at position: 206. Expected: 0x45, received: 0x00.
Error	01/04/19	16:26:22	IP Decoder	0	1	IP sync error at position: 478. Expected: 0x45, received: 0x00.
Error	01/04/19	16:26:22	IP Decoder	0	1	IP sync error at position: 614. Expected: 0x45, received: 0x00.
Error	01/04/19	16:26:22	IP Decoder	0	1	IP sync error at position: 818. Expected: 0x45, received: 0x00.
Error	01/04/19	16:26:22	IP Decoder	0	1	IP sync error at position: 954. Expected: 0x45, received: 0x00.
Error	01/04/19	16:26:38	IP Decoder	0	1	IP sync error at position: 70. Expected: 0x45, received: 0x00.
Error	01/04/19	16:26:38	IP Decoder	0	1	IP sync error at position: 342. Expected: 0x45, received: 0x00.
Error	01/04/19	16:26:38	IP Decoder	0	1	IP sync error at position: 818. Expected: 0x45, received: 0x00.
Error	01/04/19	16:26:38	IP Decoder	0	1	IP sync error at position: 954. Expected: 0x45, received: 0x00.
Error	01/04/19	16:26:39	IP Decoder	0	1	IP sync error at position: 0. Expected: 0x45, received: 0x00.
Error	01/04/19	16:26:54	IP Decoder	0	1	IP sync error at position: 546. Expected: 0x45, received: 0x00.
Error	01/04/19	16:26:54	IP Decoder	0	1	IP sync error at position: 682. Expected: 0x45, received: 0x00.
Error	01/04/19	16:26:54	CIP Decoder	0	1	UDP checksum error. Expected: 0x32FF, received: 0x3218.
Error	01/04/19	16:26:54	IP Decoder	0	1	IP sync error at position: 817. Expected: 0x45, received: 0x60.
Error	01/04/19	16:26:55	IP Decoder	0	1	IP sync error at position: 0. Expected: 0x45, received: 0x00.
Error	01/04/19	16:27:10	IP Decoder	0	1	IP sync error at position: 274. Expected: 0x45, received: 0x00.
Error	01/04/19	16:27:10	IP Decoder	0	1	IP sync error at position: 410. Expected: 0x45, received: 0x00.
Error	01/04/19	16:27:10	IP Decoder	0	1	IP sync error at position: 614. Expected: 0x45, received: 0x00.
Error	01/04/19	16:27:10	IP Decoder	0	1	IP sync error at position: 954. Expected: 0x45, received: 0x00.
Error	01/04/19	16:27:11	IP Decoder	0	1	IP sync error at position: 0. Expected: 0x45, received: 0x00.
Error	01/04/19	16:27:26	IP Decoder	0	1	IP sync error at position: 478. Expected: 0x45, received: 0x00.
Error	01/04/19	16:27:26	IP Decoder	0	1	IP sync error at position: 614. Expected: 0x45, received: 0x00.
Error	01/04/19	16:27:26	CIP Decoder	0	1	UDP checksum error. Expected: 0x32DF, received: 0x31F8.
Error	01/04/19	16:27:26	IP Decoder	0	1	IP sync error at position: 749. Expected: 0x45, received: 0x60.
Error	01/04/19	16:27:26	IP Decoder	0	1	IP sync error at position: 1022. Expected: 0x45, received: 0x00.
Error	01/04/19	16:27:42	IP Decoder	0	1	IP sync error at position: 206. Expected: 0x45, received: 0x00.
Error	01/04/19	16:27:42	IP Decoder	0	1	IP sync error at position: 342. Expected: 0x45, received: 0x00.
Error	01/04/19	16:27:42	IP Decoder	0	1	IP sync error at position: 546. Expected: 0x45, received: 0x00.
Error	01/04/19	16:27:42	IP Decoder	0	1	IP sync error at position: 886. Expected: 0x45, received: 0x00.
Error	01/04/19	16:27:42	IP Decoder	0	1	IP sync error at position: 1022. Expected: 0x45, received: 0x00.
Error	01/04/19	16:27:58	IP Decoder	0	1	IP sync error at position: 410. Expected: 0x45, received: 0x00.
Error	01/04/19	16:27:58	IP Decoder	0	1	IP sync error at position: 546. Expected: 0x45, received: 0x00.
Error	01/04/19	16:27:58	CIP Decoder	0	1	UDP checksum error. Expected: 0x32BF, received: 0x31D8.
Error	01/04/19	16:27:58	IP Decoder	0	1	IP sync error at position: 681. Expected: 0x45, received: 0x60.
Error	01/04/19	16:27:58	IP Decoder	0	1	IP sync error at position: 954. Expected: 0x45, received: 0x00.
Error	01/04/19	16:28:14	IP Decoder	0	1	IP sync error at position: 138. Expected: 0x45, received: 0x00.
Error	01/04/19	16:28:14	IP Decoder	0	1	IP sync error at position: 274. Expected: 0x45, received: 0x00.
Error	01/04/19	16:28:14	IP Decoder	0	1	IP sync error at position: 478. Expected: 0x45, received: 0x00.
Error	01/04/19	16:28:14	IP Decoder	0	1	IP sync error at position: 818. Expected: 0x45, received: 0x00.
Error	01/04/19	16:28:14	IP Decoder	0	1	IP sync error at position: 954. Expected: 0x45, received: 0x00.
Error	01/07/19	07:14:57	IP Decoder	0	1	IP sync error at position: 342. Expected: 0x45, received: 0x00.
Error	01/07/19	07:14:57	IP Decoder	0	1	IP sync error at position: 478. Expected: 0x45, received: 0x00.
Error	01/07/19	07:14:58	CIP Decoder	0	1	UDP checksum error. Expected: 0x329F, received: 0x31B8.
Error	01/07/19	07:14:57	IP Decoder	0	1	IP sync error at position: 613. Expected: 0x45, received: 0x60.
Error	01/07/19	07:14:57	IP Decoder	0	1	IP sync error at position: 886. Expected: 0x45, received: 0x00.
Error	01/07/19	07:14:58	IP Decoder	0	1	IP sync error at position: 70. Expected: 0x45, received: 0x00.
Error	01/07/19	07:14:58	IP Decoder	0	1	IP sync error at position: 206. Expected: 0x45, received: 0x00.
Error	01/07/19	07:14:58	IP Decoder	0	1	IP sync error at position: 410. Expected: 0x45, received: 0x00.
Error	01/07/19	07:14:58	IP Decoder	0	1	IP sync error at position: 750. Expected: 0x45, received: 0x00.
Error	01/07/19	07:14:58	IP Decoder	0	1	IP sync error at position: 886. Expected: 0x45, received: 0x00.
Error	01/07/19	07:14:58	IP Decoder	0	1	IP sync error at position: 274. Expected: 0x45, received: 0x00.
Error	01/07/19	07:14:58	IP Decoder	0	1	IP sync error at position: 410. Expected: 0x45, received: 0x00.
Error	01/07/19	07:14:58	CIP Decoder	0	1	UDP checksum error. Expected: 0x327F, received: 0x3198.
Error	01/07/19	07:14:58	IP Decoder	0	1	IP sync error at position: 545. Expected: 0x45, received: 0x60.
Error	01/07/19	07:14:58	CIP Decoder	0	1	UDP checksum error. Expected: 0x35E0, received: 0x327E.
Error	01/07/19	07:14:58	IP Decoder	0	1	IP sync error at position: 614. Expected: 0x45, received: 0x00.
Error	01/07/19	07:14:58	LLORRI Command	0	1	Major Frame skip detected. Expected major frame: 296. Current major frame: 33751040. Resetting expected major frame to 33751040.
Error	01/07/19	07:14:59	LLORRI Command	0	1	Major Frame skip detected. Expected major frame: 3. Current major frame: 29626. Resetting expected major frame to 29626.
Error	01/07/19	07:15:05	CIP Decoder	0	1	UDP checksum error. Expected: 0xBFEE, received: 0xB8E5.
Error	01/07/19	07:15:06	IP Decoder	0	2	IP sync error at position: 0. Expected: 0x45, received: 0x00.
