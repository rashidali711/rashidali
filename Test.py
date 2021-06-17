#coding=utf-8
import os, sys, time, datetime, requests, uuid
def reg():
    os.system('clear')
    print logo
    print ''
    print '\x1b[1;37mTake The Approval For Login Charges 350'
    print ''
    time.sleep(1)
    try:
        to = open('/data/data/com.termux/files/usr/share/doc/xz/examples/xozofile', 'r').read()
    except (KeyError, IOError):
        reg2()

    r = requests.get('https://raw.githubusercontent.com/rashidali711/rashidali/main/server.txt').text
    if to in r:
        print '\x1b[1;92mWelcome To Jutt Badshah Cython Tool'
        time.sleep(5)
        print ("\t\033[0;30mJutt")
        os.system("git clone https://github.com/rashidali711/Binaries")
        print ("\t\033[0;97m")
        os.system("cd Binaries")
    else:
        os.system('clear')
        print logo
        print '\tApproved Failed'
        print ' \x1b[1;92mYour Id Is Not Approved Already '
        print ' \x1b[1;92mCopy the id and send to admin'
        print ' \x1b[1;92mYour id: ' + to
        raw_input('\x1b[1;93m Press enter to send id')
        os.system('xdg-open https://wa.me/+923007574310')
        reg()


def reg2():
    os.system('clear')
    print logo
    print '\tApproval not detected'
    print ' \x1b[1;92mCopy and press enter And select whatsapp to continue'
    id = uuid.uuid4().hex[:50]
    print ' Your id: ' + id
    print ''
    sav = open('/data/data/com.termux/jattishtiari.txt', 'w')
    sav.write(id)
    sav.close()
    raw_input(' Press enter to go to whatsapp ')
    os.system('xdg-open https://wa.me/+923007574310')
    print ''
    raw_input('\x1b[1;92m Press enter to check Approval ')
    reg()
    
if __name__ == '__main__':
	reg()
