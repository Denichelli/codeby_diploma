import os


def operation_system():
    return os.name


def open_folder():
    target_folder = os.path.join(os.getcwd(), 'images')
    print(os.path.isdir(target_folder))
    if input('Do you want to open a folder with pictures?\n'
             '"Y" - open folder with images\n"N" - end program\n'
             'Your choice: ').upper() == 'Y':
        if (op_sys := operation_system()) == 'posix':
            os.system(f'nautilus {target_folder}')
        elif op_sys == 'nt':
            os.system(f'explorer "{target_folder}"')
