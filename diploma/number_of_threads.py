from colorama import Fore
import os


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
