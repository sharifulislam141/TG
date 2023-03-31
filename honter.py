import time,requests,sys,random,re,string,concurrent.futures
banner = '''
 \u001b[31m__________   ___ .______    __        ______    __  .___________. _______ .______      
|   ____\  \ /  / |   _  \  |  |      /  __  \  |  | |           ||   ____||   _  \     
|  |__   \  V  /  |  |_)  | |  |     |  |  |  | |  | `---|  |----`|  |__   |  |_)  |    
|   __|   >   <   |   ___/  |  |     |  |  |  | |  |     |  |     |   __|  |      /     
|  |____ /  .  \  |  |      |  `----.|  `--'  | |  |     |  |     |  |____ |  |\  \----.
|_______/__/ \__\ | _|      |_______| \______/  |__|     |__|     |_______|| _| `._____|
                                                                                        
 \u001b[32mwp.txDEVELOPED BY TEAM BADS
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

def finder_1(url):
    # try with http
    url = 'http://' + URLdomain(url)
    # check = requests.get
    # if  
    # else:
        # url = 'https://' + URLdomain(url)
    
def finder_2(url):
    # try with http
    url = 'http://' + URLdomain(url)
    # check = requests.get
    # if  
    # else:
        # url = 'https://' + URLdomain(url)
    
def finder_3(url):
    # try with http
    url = 'http://' + URLdomain(url)
    # check = requests.get
    # if  
    # else:
        # url = 'https://' + URLdomain(url)
        







def run_code(site):
    try:
        finder_1(site)
        finder_2(site)
        finder_3(site)
    except:
        pass
    
        







animated(banner)
animated("\033[1;31mENTER FILE NAME \n")
filename = input("EXPLOITER > ")

animated("\033[1;31mENTER  THREAD \n")
th = int(input("EXPLOITER > "))

file = open(filename,encoding="utf-8").read().split()
myfile = set(file)
with concurrent.futures.ThreadPoolExecutor(max_workers=th) as executor:
    
    futures = [executor.submit(run_code, site) for site in myfile]

 
    concurrent.futures.wait(futures)
    