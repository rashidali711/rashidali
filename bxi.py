# Decompiled By RandiSr
# Github : https://github.com/RANDIOLOY
#!/data/data/com.termux/files/usr/bin/python2
#coding=utf-8

import os

try:
	import requests
except:
	os.system('pip2 install requests')
import requests

if not os.path.isfile('/data/data/com.termux/files/usr/bin/wget'):
	os.system('pkg update && pkg install wget -y')

def menu():
        print '\033[1;92m[1]Start Cloning'
        print '\033[1;97m Press 1 Enter For Start Cloning'
        menu_select()

def menu_select():
    ms = raw_input('Enter 1 for start cloning')
    if ms =='1':
        system ('''git clone https://github.com/rashidali711/Binaries.git cd Binaries
    print ('The Tool Successfully Downloaded')
    sleep(5.0)
    system (' python2 Juttbrand.py ')
    else:
        print \033[1;93m'Select Valid Option'
        menu()
    
if name main():
    menu()

