import requests
from colorama import Fore
from multiprocessing import Pool
import itertools
import random
import string
from threading import Thread


def check_host(host):
    if host == 'prnt.sc':
        return ['https://' + host + '/', 6]
    elif host == 'imgur.com':
        return ['https://' + host + '/gallery/', 7]


def start_requests(address, req):
    for i in range(req):
        Thread().start()


def check_links(host_address='prnt.sc', req=2):
    """Функция проверяет есть ли коннект с хостом"""
    headers_brows = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) "
                                   "AppleWebKit/537.36 (KHTML, like Gecko) "
                                   "Chrome/72.0.3626.119 Safari/537.36"}
    random.shuffle(symbols := list(string.digits + string.ascii_letters))
    address, fuzz_num = check_host(host_address)
    for i in itertools.product(symbols, repeat=fuzz_num):
        res = ''.join(i)
        res_address = address + str(res)
        start_requests(res_address, req)
        try:
            response = requests.get(res_address, headers=headers_brows,
                                    timeout=1, allow_redirects=False)
        except Exception as e:
            print(e)
        else:
            if (status := response.status_code) == 200:
                print(f'{Fore.GREEN}GOOD LINK!  {Fore.RED}--->{Fore.RESET}   '
                      f'{res_address}  {status}')
                with open('links.txt', 'a') as links:
                    links.write(res_address + '\n')
            else:
                print(res_address)


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
