#!/usr/bin/env python
#-*- coding: utf-8 -*-
# By Jonatas Fil (Dkr)

import shodan
import sys

# API
API_KEY = ""

# BANNER
if len(sys.argv) == 1:
        print """
▓█████▄  ██ ▄█▀ ██▀███    ██████  ▄████▄   ▄▄▄       ███▄    █ 
▒██▀ ██▌ ██▄█▒ ▓██ ▒ ██▒▒██    ▒ ▒██▀ ▀█  ▒████▄     ██ ▀█   █ 
░██   █▌▓███▄░ ▓██ ░▄█ ▒░ ▓██▄   ▒▓█    ▄ ▒██  ▀█▄  ▓██  ▀█ ██▒
░▓█▄   ▌▓██ █▄ ▒██▀▀█▄    ▒   ██▒▒▓▓▄ ▄██▒░██▄▄▄▄██ ▓██▒  ▐▌██▒
░▒████▓ ▒██▒ █▄░██▓ ▒██▒▒██████▒▒▒ ▓███▀ ░ ▓█   ▓██▒▒██░   ▓██░
 ▒▒▓  ▒ ▒ ▒▒ ▓▒░ ▒▓ ░▒▓░▒ ▒▓▒ ▒ ░░ ░▒ ▒  ░ ▒▒   ▓▒█░░ ▒░   ▒ ▒ 
 ░ ▒  ▒ ░ ░▒ ▒░  ░▒ ░ ▒░░ ░▒  ░ ░  ░  ▒     ▒   ▒▒ ░░ ░░   ░ ▒░
 ░ ░  ░ ░ ░░ ░   ░░   ░ ░  ░  ░  ░          ░   ▒      ░   ░ ░ 
   ░    ░  ░      ░           ░  ░ ░            ░  ░         ░ 
 ░                               ░                             

shodan simple search 

  by Jonatas Fil (Dkr)
"""
        print 'Usage: %s <query>' % sys.argv[0]
        sys.exit(1)

try:
        # LOAD API
        api = shodan.Shodan(API_KEY)

        # SEARCH
        query = ' '.join(sys.argv[1:])
        result = api.search(query)
        
        # FILTER
        for service in result['matches']:
                 print service['ip_str']
except Exception as e:
        print 'Error: %s' % e
        sys.exit(1)
