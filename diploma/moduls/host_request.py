import requests
from colorama import Fore
from . import write_in_file


def address_verification(address):
    headers_brows = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) "
                                   "AppleWebKit/537.36 (KHTML, like Gecko) "
                                   "Chrome/72.0.3626.119 Safari/537.36"}
    try:
        response = requests.get(address, headers=headers_brows,
                                timeout=1, allow_redirects=False)
    except Exception as e:
        print(e)
        return False
    else:
        if response.status_code == 200:
            print(f'{Fore.GREEN}GOOD! {Fore.RED}-->{Fore.RESET} {address}')
            file_name = address[-12:-4]
            if (slice_for_extension := response.text[:15]).count('GIF'):
                file_name += 'gif'
            elif slice_for_extension.count('JFIF'):
                file_name += 'jpg'
            elif slice_for_extension.count('PNG'):
                file_name += 'png'
            else:
                file_name = address[-12:]
            data = response.content
            if res := write_in_file.writing_in_file(data, file_name):
                return res
        else:
            print(address)
        response.close()
        return False
