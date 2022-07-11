import requests
import re
from bs4 import BeautifulSoup
from colorama import Fore
from write_in_file import write_in_file as wr_file


def fix_link(link):
    if link.startswith('//'):
        return link.replace('//', 'https://')
    else:
        return link


def get_data(link, headers_br):
    res_link = fix_link(link)
    try:
        data = requests.get(res_link, headers=headers_br).content
    except Exception as e:
        print(e)
    else:
        return data


def host_request(address):
    headers_brows = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) "
                                   "AppleWebKit/537.36 (KHTML, like Gecko) "
                                   "Chrome/72.0.3626.119 Safari/537.36"}
    try:
        response = requests.get(address, headers=headers_brows,
                                timeout=1, allow_redirects=False)
    except Exception as e:
        print(e)
        return False
    else:
        if response.status_code == 200:
            print(f'{Fore.GREEN}GOOD! {Fore.RED}-->{Fore.RESET} {address}')
            soup = BeautifulSoup(response.text, 'html.parser')
            image_link = str(soup.
                             find('img', class_="no-click screenshot-image").
                             get('src'))
            extension = re.findall(r'.*/([\w-]+\.\w{3,4}$)', image_link)
            data = get_data(image_link, headers_brows)
            if res := wr_file(data, *extension):
                return res
        else:
            print(address)
        response.close()
        return False
