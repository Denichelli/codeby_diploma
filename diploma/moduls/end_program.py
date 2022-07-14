from colorama import Fore


def ending(res_time, res_links, res_file_size):
    result_time = f'{int(res_time // 3600)} hours ' \
               f'{int((res_time % 3600) // 60)} minutes ' \
               f'{int((res_time % 3600) % 60)} seconds'
    result_links = res_links
    if res_file_size >= 1024:
        result_file_size = f'{str(res_file_size // 1024)}kb'
    else:
        result_file_size = str(res_file_size)
    print('=' * 20, '\n\n')
    print(f'{Fore.LIGHTMAGENTA_EX}Ready for: {result_time:<16}')
    print(f'Found links: {result_links:<16}')
    print(f'Folder size: {result_file_size:<16}{Fore.RESET}\n')
