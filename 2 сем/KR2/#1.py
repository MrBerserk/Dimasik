from os import makedirs
from os.path import join
import requests
from concurrent.futures import ThreadPoolExecutor

r = requests.get('https://api.ipify.org/?format=json')
ip = r.json()['ip']
ip_info = requests.get(f'https://ipinfo.io/{ip}/geo')

dir = f'user_data/{ip}/'
makedirs(dir, exist_ok=True)

with open(join(dir, 'user_info.txt'), 'w', encoding='utf-8') as file:
    file.write(ip_info.text)


def download_doge():
    s = requests.Session()
    r = s.get('https://dog.ceo/api/breeds/image/random')
    img_url = r.json()['message']
    r = s.get(img_url)
    with open(join(dir, r.url.split('/')[-1]), 'wb') as f:
        f.write(r.content)

with ThreadPoolExecutor(4) as pool:
    for _ in range(12):
        pool.submit(download_doge)