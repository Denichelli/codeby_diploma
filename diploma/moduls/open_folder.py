import os


def opening(folder):
    if (op_sys := operation_system()) == 'posix':
        os.system(f'nautilus {folder}')
    elif op_sys == 'nt':
        os.system(f'explorer "{folder}"')


def operation_system():
    return os.name


def opening_folder():
    target_folder = os.path.join(os.getcwd(), 'images')
    while True:
        try:
            req_open = input('Do you want to open a folder with pictures?\n'
                             '"Y" - open folder with images\n'
                             '"N" - end program\n'
                             'Your choice: ').upper()
        except Exception as e:
            print(e)
        else:
            if req_open == 'Y':
                if os.path.isdir(target_folder):
                    opening(target_folder)
            break
