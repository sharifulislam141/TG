import time
import sys
import os,re,requests
from multiprocessing.dummy import Pool
import threading
import requests


banner = '''

\u001b[35m___  ____ ____ _  _ ____ ____    
|  \ |  | |__/ |_/  |___ |__/   AUTHOR : D4RKW01F 
|__/ |__| |  \ | \_ |___ |  \   TG     :https://t.me/darkwolf141
                                FB     :https://www.facebook.com/sharifulislam141
                                 

'''

def check_and_save(url):
    try:
        thread = threading.Thread(target=check_wordpress, args=(url,))
        thread.start()
    except:
        print(f"\u001b[31mError checking site!>------{url}")
        pass

def check_wordpress(url):
    try:
        response = requests.get(url)
        if "wp-content" in response.text:
            with open("wp.txt", "a") as f:
                f.write(url + "\n")
            print(f"\u001b[32mWordPress site found!>-----{url}")
        else:
            with open("other.txt", "a") as f:
                f.write(url + "\n")
            print(f"\u001b[35mNon-WordPress site found!>-{url}")
    except:
        
        print(f"\u001b[31mError checking site!>------{url}")



binglist = {"http://www.bing.com/search?q=&count=50&first=1",
"http://www.bing.com/search?q=&count=50&first=51",
"http://www.bing.com/search?q=&count=50&first=101",
"http://www.bing.com/search?q=&count=50&first=151",
"http://www.bing.com/search?q=&count=50&first=201",
"http://www.bing.com.br/search?q=&count=50&first=1",
"http://www.bing.com.br/search?q=&count=50&first=51",
"http://www.bing.com.br/search?q=&count=50&first=101",
"http://www.bing.at/search?q=&count=50&first=1",
"http://www.bing.at/search?q=&count=50&first=51",
"http://www.bing.at/search?q=&count=50&first=101",
"http://www.bing.be/search?q=&count=50&first=1",
"http://www.bing.be/search?q=&count=50&first=51",
"http://www.bing.be/search?q=&count=50&first=101",
"http://www.bing.cl/search?q=&count=50&first=1",
"http://www.bing.cl/search?q=&count=50&first=51",
"http://www.bing.cl/search?q=&count=50&first=101",
"http://www.bing.co.at/search?q=&count=50&first=1",
"http://www.bing.co.at/search?q=&count=50&first=51",
"http://www.bing.co.at/search?q=&count=50&first=101",
"http://www.bing.com.au/search?q=&count=50&first=1",
"http://www.bing.com.au/search?q=&count=50&first=51",
"http://www.bing.com.au/search?q=&count=50&first=101",
"http://www.bing.com.cn/search?q=&count=50&first=1",
"http://www.bing.com.cn/search?q=&count=50&first=51",
"http://www.bing.com.cn/search?q=&count=50&first=101",
"http://www.bing.cz/search?q=&count=50&first=1",
"http://www.bing.cz/search?q=&count=50&first=51",
"http://www.bing.cz/search?q=&count=50&first=101",
"http://www.bing.de/search?q=&count=50&first=1",
"http://www.bing.de/search?q=&count=50&first=51",
"http://www.bing.de/search?q=&count=50&first=101",
"http://www.bing.dk/search?q=&count=50&first=1",
"http://www.bing.dk/search?q=&count=50&first=51",
"http://www.bing.dk/search?q=&count=50&first=101",
"http://www.bing.ca/search?q=&count=50&first=1",
"http://www.bing.ca/search?q=&count=50&first=51",
"http://www.bing.ca/search?q=&count=50&first=101",
"http://www.bing.sg/search?q=&count=50&first=1",
"http://www.bing.sg/search?q=&count=50&first=51",
"http://www.bing.sg/search?q=&count=50&first=101",
"http://www.bing.se/search?q=&count=50&first=1",
"http://www.bing.se/search?q=&count=50&first=51",
"http://www.bing.se/search?q=&count=50&first=101",
"http://www.bing.pl/search?q=&count=50&first=1",
"http://www.bing.pl/search?q=&count=50&first=51",
"http://www.bing.pl/search?q=&count=50&first=101",
"http://www.bing.no/search?q=&count=50&first=1",
"http://www.bing.no/search?q=&count=50&first=51",
"http://www.bing.no/search?q=&count=50&first=101",
"http://www.bing.nl/search?q=&count=50&first=1",
"http://www.bing.nl/search?q=&count=50&first=51",
"http://www.bing.nl/search?q=&count=50&first=101",
"http://www.bing.net.nz/search?q=&count=50&first=1",
"http://www.bing.net.nz/search?q=&count=50&first=51",
"http://www.bing.net.nz/search?q=&count=50&first=101",
"http://www.bing.lv/search?q=&count=50&first=1",
"http://www.bing.lv/search?q=&count=50&first=51",
"http://www.bing.lv/search?q=&count=50&first=101",
"http://www.bing.lt/search?q=&count=50&first=1",
"http://www.bing.lt/search?q=&count=50&first=51",
"http://www.bing.lt/search?q=&count=50&first=101",
"http://www.bing.it/search?q=&count=50&first=1",
"http://www.bing.it/search?q=&count=50&first=51",
"http://www.bing.it/search?q=&count=50&first=101",
"http://www.bing.is/search?q=&count=50&first=1",
"http://www.bing.is/search?q=&count=50&first=51",
"http://www.bing.is/search?q=&count=50&first=101",
"http://www.bing.in/search?q=&count=50&first=1",
"http://www.bing.in/search?q=&count=50&first=51",
"http://www.bing.in/search?q=&count=50&first=101",
"http://www.bing.ie/search?q=&count=50&first=1",
"http://www.bing.ie/search?q=&count=50&first=51",
"http://www.bing.ie/search?q=&count=50&first=101",
"http://www.bing.hu/search?q=&count=50&first=1",
"http://www.bing.hu/search?q=&count=50&first=51",
"http://www.bing.hu/search?q=&count=50&first=101",
"http://www.bing.fr/search?q=&count=50&first=1",
"http://www.bing.fr/search?q=&count=50&first=51",
"http://www.bing.fr/search?q=&count=50&first=101",
"http://www.bing.com.sg/search?q=&count=50&first=1",
"http://www.bing.com.sg/search?q=&count=50&first=51",
"http://www.bing.com.sg/search?q=&count=50&first=101",
"http://www.bing.co.uk/search?q=&count=50&first=1",
"http://www.bing.co.uk/search?q=&count=50&first=51",
"http://www.bing.co.uk/search?q=&count=50&first=101",
"http://www.bing.co.nz/search?q=&count=50&first=1",
"http://www.bing.co.nz/search?q=&count=50&first=51",
"http://www.bing.co.nz/search?q=&count=50&first=101",
"http://www.bing.co.jp/search?q=&count=50&first=1",
"http://www.bing.co.jp/search?q=&count=50&first=51",
"http://www.bing.co.jp/search?q=&count=50&first=101",
"http://www.bing.ch/search?q=&count=50&first=1",
"http://www.bing.ch/search?q=&count=50&first=51",
"http://www.bing.ch/search?q=&count=50&first=101",
"http://www.bing.com.tr/search?q=&count=50&first=1",
"http://www.bing.com.tr/search?q=&count=50&first=51",
"http://www.bing.com.tr/search?q=&count=50&first=101",
"http://www.bing.com.pr/search?q=&count=50&first=1",
"http://www.bing.com.pr/search?q=&count=50&first=51",
"http://www.bing.com.pr/search?q=&count=50&first=101",
"http://www.bing.com.ar/search?q=&count=50&first=1",
"http://www.bing.com.ar/search?q=&count=50&first=51",
"http://www.bing.com.ar/search?q=&count=50&first=101",
"http://www.bing.com.co/search?q=&count=50&first=1",
"http://www.bing.com.co/search?q=&count=50&first=51",
"http://www.bing.com.co/search?q=&count=50&first=101",
"http://www.bing.com.es/search?q=&count=50&first=1",
"http://www.bing.com.es/search?q=&count=50&first=51",
"http://www.bing.com.es/search?q=&count=50&first=101",
"http://www.bing.fi/search?q=&count=50&first=1",
"http://www.bing.fi/search?q=&count=50&first=51",
"http://www.bing.fi/search?q=&count=50&first=101",
"http://www.bing.bo/search?q=&count=50&first=1",
"http://www.bing.bo/search?q=&count=50&first=51",
"http://www.bing.bo/search?q=&count=50&first=101",
"http://www.bing.com.do/search?q=&count=50&first=1",
"http://www.bing.com.do/search?q=&count=50&first=51",
"http://www.bing.com.do/search?q=&count=50&first=101",
"http://www.bing.gr/search?q=&count=50&first=1",
"http://www.bing.gr/search?q=&count=50&first=51",
"http://www.bing.gr/search?q=&count=50&first=101",
"http://www.bing.com.hk/search?q=&count=50&first=1",
"http://www.bing.com.hk/search?q=&count=50&first=51",
"http://www.bing.com.hk/search?q=&count=50&first=101",
"http://www.bing.com.hr/search?q=&count=50&first=1",
"http://www.bing.com.hr/search?q=&count=50&first=51",
"http://www.bing.com.hr/search?q=&count=50&first=101",
"http://www.bing.com.mx/search?q=&count=50&first=1",
"http://www.bing.com.mx/search?q=&count=50&first=51",
"http://www.bing.com.mx/search?q=&count=50&first=101",
"http://www.bing.com.my/search?q=&count=50&first=1",
"http://www.bing.com.my/search?q=&count=50&first=51",
"http://www.bing.com.my/search?q=&count=50&first=101",
"http://www.bing.ph/search?q=&count=50&first=1",
"http://www.bing.ph/search?q=&count=50&first=51",
"http://www.bing.ph/search?q=&count=50&first=101",
"http://www.bing.com.pr/search?q=&count=50&first=1",
"http://www.bing.com.pr/search?q=&count=50&first=51",
"http://www.bing.com.pr/search?q=&count=50&first=101",
"http://www.bing.pt/search?q=&count=50&first=1",
"http://www.bing.pt/search?q=&count=50&first=51",
"http://www.bing.pt/search?q=&count=50&first=101",
"http://www.bing.com.ro/search?q=&count=50&first=1",
"http://www.bing.com.ro/search?q=&count=50&first=51",
"http://www.bing.com.ro/search?q=&count=50&first=101",
"http://www.bing.ru/search?q=&count=50&first=1",
"http://www.bing.ru/search?q=&count=50&first=51",
"http://www.bing.ru/search?q=&count=50&first=101",
"http://www.bing.com.sa/search?q=&count=50&first=1",
"http://www.bing.com.sa/search?q=&count=50&first=51",
"http://www.bing.com.sa/search?q=&count=50&first=101",
"http://www.bing.si/search?q=&count=50&first=1",
"http://www.bing.si/search?q=&count=50&first=51",
"http://www.bing.si/search?q=&count=50&first=101",
"http://www.bing.sk/search?q=&count=50&first=1",
"http://www.bing.sk/search?q=&count=50&first=51",
"http://www.bing.sk/search?q=&count=50&first=101",
"http://www.bing.com.ua/search?q=&count=50&first=1",
"http://www.bing.com.ua/search?q=&count=50&first=51",
"http://www.bing.com.ua/search?q=&count=50&first=101",
"http://www.bing.com.uy/search?q=&count=50&first=1",
"http://www.bing.com.uy/search?q=&count=50&first=51",
"http://www.bing.com.uy/search?q=&count=50&first=101",
"http://www.bing.vn/search?q=&count=50&first=1",
"http://www.bing.vn/search?q=&count=50&first=51",
"http://www.bing.vn/search?q=&count=50&first=101"}
 

def dorkscan(dork):
 

    threads = []

    for bing in binglist:
        bingg = bing.replace("&count", dork + "&count")
        try:
            thread = threading.Thread(target=check_bing_result, args=(bingg,))
            thread.start()
            threads.append(thread)
        except:
            pass

    # Wait for all threads to complete
    for thread in threads:
        thread.join()

def check_bing_result(bingg):
    try:
        r = requests.get(bingg)
        checktext = r.text
        checktext = checktext.replace("<strong>","")
        checktext = checktext.replace("</strong>","")
        checktext = checktext.replace('<span dir="ltr">','')
        checksites = re.findall('<cite>(.*?)</cite>',checktext)
        for sites in checksites:
            sites = sites.replace("http://","protocol1")
            sites = sites.replace("https://","protocol2")
            sites = sites + "/"
            site = sites[:sites.find("/")+0]
            site = site.replace("protocol1","http://")
            site = site.replace("protocol2","https://")
            if "http" not in site:
                site = "http://" + site
            check_and_save(site)
    except:
        pass



def animated(text):
    for x in text:
        sys.stdout.write(x)
        sys.stdout.flush()
        time.sleep(0.005)
 
def dorkmaker(word):
    wpdorks = ['("Comment on Hello world!")',
               '("Comentarios en Hello world!")',
               '("author/admin")',
               '("uncategorized/hello-world")',
               '("category/sin-categoria")',
               '("uncategorized")',
               '("Proudly powered by WordPress")',
               '("Welcome to WordPress. This is your first post.")',
               '("Just another WordPress site")',
               '("Mr WordPress on Hello world!")',
               '("/wp/hello-world/")']

    threads = []

    for wpdork in wpdorks:
        try:
            dork = wpdork + word
            thread = threading.Thread(target=dorkscan, args=(dork,))
            thread.start()
            threads.append(thread)
            dorkscan(dork)
        except:
            pass

    # Wait for all threads to complete
    for thread in threads:
        thread.join()
animated(banner)
try:
    os.system('git pull')
except:
    pass
animated("\u001b[0mENTER SOME TEXT\n")
text = input ("D4RKW01F>")
words = text.split(" ")
for word in words:
    dorkmaker(word)
 
 
 