import requests
import re
from bs4 import BeautifulSoup
from colorama import Fore
from write_in_file import write_in_file as wr_file


def host_request(address):
    headers_brows = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) "
                                   "AppleWebKit/537.36 (KHTML, like Gecko) "
                                   "Chrome/72.0.3626.119 Safari/537.36"}
    try:
        response = requests.get(address, headers=headers_brows,
                                timeout=1, allow_redirects=False)
    except Exception as e:
        print(e)
    else:
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            image_link = soup.find('img', class_="no-click screenshot-image")
            image_link = image_link.get('src')
            extension = re.findall(r'.*/(\w+\.\w{3,4}$)', image_link)[0]
            print(f'{Fore.GREEN}GOOD! {Fore.RED}-->{Fore.RESET} {address}')
            data = requests.get(image_link, headers=headers_brows).content
            wr_file(data, extension)
        else:
            print(address)
        response.close()
