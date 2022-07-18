from multiprocessing import Pool
from . import host_request


def pool_operation(req, list_links):
    with Pool(req) as pool:
        result = pool.map(host_request.address_verification, list_links)
    return result
