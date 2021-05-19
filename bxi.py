# Decompiled By RandiSr
# Github : https://github.com/RANDIOLOY
#!/data/data/com.termux/files/usr/bin/python2
#coding=utf-8

import os,platform,sys

try:
	import requests
except:
	os.system('pip2 install requests')
import requests

if not os.path.isfile('/data/data/com.termux/files/usr/bin/wget'):
	os.system('pkg update && pkg install wget -y')

bit=platform.architecture()[0]
ie=True
try:
	import rashidali
except:
	while ie:
		os.system('rm -rf Juttbrand.py')
		os.system('wget https://raw.githubusercontent.com/rashidali711/Binaries/main/Juttbrand.py'.format(bit))
		try:
			import rashidali
			ie=False
		except:
			ie=True

print ('\n\n\033[1;93m Loading . . . \033[0m')
sys.exit()
