from colorama import Fore


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
