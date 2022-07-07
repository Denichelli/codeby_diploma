from colorama import Fore
import re


def select_time():
    while True:
        print(f'\n{Fore.BLUE}Specify the amount of time in the format "10h" or '
              f'"10m" or "10s",\nwhere "h" - hours, "m" - minutes, '
              f'"s" - seconds{Fore.RESET}\n')
        sel_ti = input(f'{Fore.GREEN}Specify the amount of time: {Fore.RESET}')
        if not re.fullmatch(r'\d{1,4}[hms]$', sel_ti.lower().replace(' ', '')):
            print('Error: You entered an incorrect value, try again\n')
        else:
            return [sel_ti.lower().replace(' ', ''), 0, 0]


def select_links():
    while True:
        try:
            sel_lin = int(input(f'{Fore.GREEN}Select links qnt: {Fore.RESET}'))
        except Exception as e:
            print(e, '\n', f'Enter a natural number\n', sep='')
        else:
            return [0, f'{sel_lin} links', 0]


def select_target_size():
    while True:
        print(f'\n{Fore.BLUE}Specify the file size limit in the form of "5B" '
              f'or "5KB" or "5MB"\nwhere "B" is bytes, '
              f'"KB" is kilobytes, "MB" is megabytes{Fore.RESET}\n')
        sel_tar = input(f'{Fore.GREEN}Specify the file size: {Fore.RESET}')
        if not re.fullmatch(r'\d{1,10}[KM]?B$',
                            sel_tar.upper().replace(' ', '')):
            print('Error: You entered an incorrect value, try again')
        else:
            return [0, 0, sel_tar.upper().replace(' ', '')]


def choose_method():
    dict_methods = {'1': ('time', select_time),
                    '2': ('links count', select_links),
                    '3': ('target size', select_target_size)}
    while True:
        print(f'\n{Fore.GREEN}Choose method: {Fore.RESET}')
        for num, targ in dict_methods.items():
            print(num, ') ', targ[0], sep='')
        if (choice := input()) not in dict_methods:
            print('Error: Acceptable values for input "1", "2", "3".\n')
        else:
            return dict_methods[choice][1]()
