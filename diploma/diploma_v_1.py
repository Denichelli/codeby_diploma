import pyfiglet
import requests
from colorama import Fore
from choose_method import choose_method as ch_met
from number_of_threads import select_threads as sel_thr
from goal_selection import available_target as av_tar


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

    target = av_tar()
    threads = sel_thr()
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

