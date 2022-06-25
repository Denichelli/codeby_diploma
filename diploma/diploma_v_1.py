import pyfiglet
import requests
import os
from colorama import Fore
from choose_method import choose_method as ch_met


def available_target():
    dict_targets = {'1': 'rghost.net', '2': 'imgur.com', '3': 'prnt.sc'}
    while True:
        print(f'{Fore.GREEN}Available targets:{Fore.RESET}')
        for num, targ in dict_targets.items():
            print(num, ') ', targ, sep='')
        if (choice := input('Your choice: ')) not in dict_targets.keys():
            print('Error: Acceptable values for input "1", "2", "3".\n')
        else:
            print(f'Using {dict_targets[choice]}\n')
            return dict_targets[choice]


def select_threads():
    your_threads = os.cpu_count()
    while True:
        try:
            sel_thr = int(input(f'{Fore.GREEN}Select threads: {Fore.RESET}'))
        except Exception as e:
            print(e, '\n', f'Enter a number from "1" to "{your_threads}"\n',
                  sep='')
        else:
            if sel_thr not in range(1, your_threads + 1):
                print(f'Enter a number from "1" to "{your_threads}"\n')
            else:
                return sel_thr


def calling_site(site):
    try:
        page = requests.get(f'https://{site}', allow_redirects=False)
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
    method = ch_met()

    print(f'Target: {Fore.LIGHTBLUE_EX}{target}{Fore.RESET} '
          f'with {Fore.LIGHTBLUE_EX}{threads} threads{Fore.RESET} '
          f'for {Fore.LIGHTBLUE_EX}{method}{Fore.RESET}')

    if calling_site(target):
        print('Next code...')
    else:
        print('EXIT')

# if (sel_ti := sel_ti.lower().replace(' ', '')).endswith('h'):
#     return int(sel_ti[:-1]) * 3600
# elif sel_ti.endswith('m'):
#     return int(sel_ti[:-1]) * 60
# return int(sel_ti[:-1])

