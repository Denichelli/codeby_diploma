import random
import re
import string
from time import time
from . import end_program
from . import open_folder
from . import multiprocessor_operation

start_time = 0
set_time = 0
links = 0
file_size = 0


def do_host_name(host):
    if host == 'imgur.com':
        return [f'https://i.{host}/', 7]


def start_find_data(address, req, limit_time, limit_links, limit_file_size):
    global links, file_size, start_time, set_time
    start_time = time()
    symbols = list(string.ascii_uppercase + string.ascii_lowercase +
                   string.digits)
    address, fuzz_num = do_host_name(address)
    res_address = []
    while True:
        gen_piece = ''.join(random.choice(symbols) for i in range(fuzz_num))
        for current_reading, limit in ((links, limit_links),
                                       (file_size, limit_file_size),
                                       (set_time, limit_time)):
            if current_reading >= limit != 0:
                end_program.ending(set_time, links, file_size)
                open_folder.opening_folder()
                return False
        if len(res_address) < req:
            res_address.append(f'{address}{gen_piece}.jpeg')
            continue
        elif len(res_address) == req:
            for res in multiprocessor_operation.\
                    pool_operation(req, res_address):
                if res:
                    links += 1
                    file_size += res
            res_address = []
        set_time += (time() - start_time)
        start_time = time()


def convert_args(address, req, limit_args):
    limit_time, limit_links, limit_file_size = limit_args
    if limit_time != 0:
        time_digits = int(re.findall(r'(^\d+)', limit_time)[0])
        if str(limit_time).endswith('h'):
            limit_time = time_digits * 3600
        elif str(limit_time).endswith('m'):
            limit_time = time_digits * 60
        else:
            limit_time = time_digits
        start_find_data(address, req, limit_time, limit_links, limit_file_size)
    elif limit_links != 0:
        limit_links = int(re.findall(r'(^\d+)', limit_links)[0])
        # print(limit_links)
        start_find_data(address, req, limit_time, limit_links, limit_file_size)
    elif limit_file_size != 0:
        file_size_digits = int(re.findall(r'(^\d+)', limit_file_size)[0])
        if str(limit_file_size).endswith('MB'):
            limit_file_size = file_size_digits * (1024 ** 2)
        elif str(limit_file_size).endswith('KB'):
            limit_file_size = file_size_digits * 1024
        else:
            limit_file_size = file_size_digits
        start_find_data(address, req, limit_time, limit_links, limit_file_size)
