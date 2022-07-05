import os


def write_in_file(data, extension):
    folder_path = os.path.join(os.getcwd(), 'images', f'{extension}')
    if os.path.isdir(folder_path):
        with open(folder_path, 'wb') as f:
            try:
                f.write(data)
            except Exception as e:
                print(e)
                return False
            else:
                return True
    else:
        for i in range(1):
            os.mkdir('images')
            write_in_file(data, extension)
        print('There is no folder for saving files')
        return False
