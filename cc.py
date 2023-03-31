import requests

url = 'http://www.insecam.org/en/bycountry/BD/'
response = requests.get(url, headers=headers)

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.5481.178 Safari/537.36',
    'Referer': 'http://www.insecam.org/en/byrating/',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'en-US,en;q=0.9',
    'Cookie': '_ga=GA1.1.1735221176.1680239229; __gads=ID=e3b3c93897d4982b-22bfa773e0dc003f:T=1680239235:RT=1680239235:S=ALNI_MZi-LDpBr_Di7IJjsw6VZrlMtUOuw; __gpi=UID=00000be92b768460:T=1680239235:RT=1680239235:S=ALNI_MajvfG9vkU6W_aHVsnD8x6TSEDSig; _ym_uid=1680239231358721373; _ym_d=1680239231; _ym_isad=2; _ga_F7ZM4QYVCB=GS1.1.1680239228.1.1.1680239252.0.0.0'
}

response = requests.get(url, headers=headers)

print(response.iter_content)
