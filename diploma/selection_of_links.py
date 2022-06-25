import re
import requests
import os
from re import findall, sub
from colorama import Fore
from multiprocessing import Pool
import itertools
import random
import string


DOMAIN = ""
DIRS = []
counter_all = 0
counter_now = 0
file_path = ''


def check_links():
    """Функция проверяет есть ли коннект с хостом"""
    headers_brows = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) "
                                   "AppleWebKit/537.36 (KHTML, like Gecko) "
                                   "Chrome/72.0.3626.119 Safari/537.36"}
    host_addres = 'prnt.sc'
    random.shuffle(symbols := list(string.digits + string.ascii_letters))
    for i in itertools.product(symbols, repeat=6):
        res = ''.join(i)
        check_domain = 'https://' + host_addres + '/' + str(res)
        try:
            response = requests.get(check_domain, headers=headers_brows,
                                    timeout=1, allow_redirects=False)
        except Exception as e:
            print(e)
        else:
            if (status := response.status_code) == 200:
                print(f'{Fore.GREEN}GOOD LINK!  {Fore.RED}--->{Fore.RESET}   '
                      f'{check_domain}  {status}')
                with open('links.txt', 'a') as links:
                    links.write(check_domain + '\n')
            else:
                print(check_domain)


# def result_file(text):
#     global file_path
#     with open((''.join(findall(r'(.+/).+$', file_path)) + 'fuzz.txt'),
#               'a') as append_txt:
#         append_txt.write(text + '\n')
#
#
# def start_threads(num_threads, args_w):
#     global DIRS, file_path
#     file_path = args_w
#     if num_threads is None:
#         num_threads = 1
#     with Pool(int(num_threads)) as pool:
#         pool.map(get_site_dirs, DIRS)


check_links()
