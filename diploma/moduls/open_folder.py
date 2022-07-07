import os


def get_os():
    current_path = os.getcwd()
    return current_path


def open_folder():
    operating_system = get_os()
    if answer := (input('Do you want to open a folder with pictures?\n'
                        '"Y" - open folder with images\n'
                        '"N" - end program\n'
                        'Your choice: ')).upper() == 'Y':
        print('open')
