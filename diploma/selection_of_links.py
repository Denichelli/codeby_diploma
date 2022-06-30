import requests
from colorama import Fore
from multiprocessing import Pool
import itertools
import random
import string
import os
from multiprocessing import Pool
from time import time


star_time = time()
links = 0
size = 0


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
        if (status := response.status_code) == 200:
            global links
            print(f'{Fore.GREEN}GOOD! {Fore.RED}-->{Fore.RESET} {address}')
            links += 1
            with open(os.path.join(
                    os.getcwd(), 'images', f'image{links}.png'),
                    'wb') as f:
                print(os.path.join(os.getcwd(), 'images', f'image{links}.png'))
                f.write(response.content)
        else:
            print(address)


def do_host_name(host):
    if host == 'prnt.sc':
        return ['https://' + host + '/', 6]
    elif host == 'imgur.com':
        return ['https://' + host + '/gallery/', 7]


def start_pool(address, req, limit_links):
    random.shuffle(symbols := list(string.digits + string.ascii_letters))
    address, fuzz_num = do_host_name(address)
    res_address = []
    for i in itertools.product(symbols, repeat=fuzz_num):
        global links
        res = ''.join(i)
        res_address.append(address + str(res))
        if links >= limit_links:
            break
        if len(res_address) == req:
            with Pool(req) as pool:
                pool.map(host_request, res_address)
            res_address = []


def check_links(host_address='prnt.sc', req=2, set_links=20):
    start_pool(host_address, req, set_links)


check_links()
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
