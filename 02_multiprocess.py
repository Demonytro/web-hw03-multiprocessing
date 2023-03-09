from time import time
from multiprocessing import cpu_count, Pool
import logging

logger = logging.getLogger()
stream_handler = logging.StreamHandler()
logger.addHandler(stream_handler)
logger.setLevel(logging.DEBUG)


def factorize(*number):
    result_number = []
    for num in number:
        count = range(num + 1)[1:]
        res1 = []
        for i in count:
            if not num % i:
                res1.append(i)
        result_number.append(res1)
    return result_number


if __name__ == '__main__':
    count_cpu = cpu_count()
    number = [128, 255, 99999, 10651060]

    timer_start = time()

    with Pool(count_cpu) as pool:
        logger.debug(pool.map(factorize, number))

    timer_finish = time()
    print(f'Timer synchro - {timer_finish - timer_start}s ')
