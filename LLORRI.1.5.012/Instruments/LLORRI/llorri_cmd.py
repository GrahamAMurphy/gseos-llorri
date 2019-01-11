import GseosCmd
import LLorriCmd

def CMD( mnemonic, *args ):
	## print args[0] ## a = args.__str__()
	c = args[0]
	print c
	d = "'" + c.__str__() + "'"
	print d
        fullcmd = 'LLorriCmd.' + mnemonic + '(' + d + ')'
        print "cmd: ", fullcmd
	GseosCmd.ExecCmd( fullcmd )
	pass
