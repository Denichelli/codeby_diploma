import os


def writing_in_file(data, extension):
    folder_path = os.path.join(os.getcwd(), 'images')
    file_path = os.path.join(os.getcwd(), 'images', f'{extension}')
    if os.path.isdir(folder_path):
        with open(file_path, 'wb') as f:
            try:
                f.write(data)
            except Exception as e:
                print(e)
                return False
            else:
                return os.path.getsize(file_path)
    else:
        for i in range(1):
            try:
                os.mkdir('images')
            except Exception as e:
                print(e)
                return False
            else:
                if res := writing_in_file(data, extension):
                    return res
