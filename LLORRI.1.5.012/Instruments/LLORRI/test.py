from GseosMonitor import TMonitor
from __main__ import *
import Gseos
import GseosCmd
import os.path
import sys
from struct import pack
import imp

print Gseos.GetProjectPath()
newpath = Gseos.GetProjectPath() + "\\Instruments\\LLORRI"
print newpath
try:
    ## print imp.find_module( "llorri_processes", newpath )
    print imp.load_source( "llorri_processes", newpath, "llorri_processes.py" )
except:
    print 'fail'


def ftest( oBlock ):
    print llorri_processes.dIDtoProcess.values()

m_test = TMonitor( 'HandleProfile', ftest )
LOR_Profile.Monitors.append( m_test )
