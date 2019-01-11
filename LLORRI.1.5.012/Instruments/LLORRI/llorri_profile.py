from GseosMonitor import TMonitor
from __main__ import *
import Gseos
import GseosCmd
import os.path
import sys
from struct import pack
import imp
import llorri_processes

def fHandleProfile( oBlock ):
    reload(llorri_processes)

    ## print llorri_processes.dIDtoProcess.values()

    for i in range(0,10):
	ibeg = i * 0x20
	iend = (i+1) * 0x20
	q = oBlock.Data1[2*i]
	try:
	    str = llorri_processes.dIDtoProcess[ q ]
	    ### print "%04x" % q, str
	    LOR_Profile_Name.Data[ibeg:iend] = str[0:32]
	except Exception as E:
	    LOR_Profile_Name.Data[ibeg:iend] = "Profile %d" % (i+1)

    LOR_Profile_Name.send()

m_fHandleProfile = TMonitor( 'HandleProfile', fHandleProfile )
LOR_Profile.Monitors.append( m_fHandleProfile )
