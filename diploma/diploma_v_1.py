import pyfiglet
import requests
from colorama import Fore
from moduls.choose_method import choose_method
from moduls.number_of_threads import select_threads
from moduls.goal_selection import available_target
from moduls.selection_of_links import convert_args


def calling_site(site):
    headers_brows = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) "
                                   "AppleWebKit/537.36 (KHTML, like Gecko) "
                                   "Chrome/72.0.3626.119 Safari/537.36"}
    try:
        page = requests.get(f'https://{site}/', headers=headers_brows,
                            timeout=1, allow_redirects=False)
    except Exception as e:
        print(e)
        return False
    else:
        if page.status_code == 200:
            print(f'\n.....site avaliable. '
                  f'{Fore.RED}Starting stalking!{Fore.RESET}')
            return True
        else:
            print(f'It was not possible to connect to the site "{site}"')
            return False


if __name__ == '__main__':
    pyfiglet.print_figlet('My NetStalker', 'big')

    target = available_target()
    threads = select_threads()
    method = ''
    for i in (list_methods := choose_method()):
        if i != 0:
            method = i

    print(f'Target: {Fore.LIGHTBLUE_EX}{target}{Fore.RESET} '
          f'with {Fore.LIGHTBLUE_EX}{threads} threads{Fore.RESET} '
          f'for {Fore.LIGHTBLUE_EX}{method}{Fore.RESET}')

    if calling_site(target):
        convert_args(target, threads, list_methods)
    else:
        print('EXIT')
