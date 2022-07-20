from multiprocessing import Pool
from . import host_request


def pool_operation(req, list_links):
    with Pool(req) as pool:
        try:
            result = pool.map(host_request.address_verification, list_links)
        except Exception as e:
            print(e)
    return result
