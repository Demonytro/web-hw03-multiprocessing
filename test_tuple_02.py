from time import time
from multiprocessing import Process, cpu_count, Pool
import sys
import logging

logger = logging.getLogger()
stream_handler = logging.StreamHandler()
logger.addHandler(stream_handler)
logger.setLevel(logging.DEBUG)


def tpl(*number):
    print(number, type(number))
    result_number = []
    print(dict(enumerate(number)))
    for i, num in enumerate(number):
        print(i, num)
        count = range(num+1)[1:]
        print(count)
        res1 = []
        for i in count:
            try:
                if not num % i:
                    res1.append(i)
            except ZeroDivisionError:
                continue
        print(res1)
        result_number.append(res1)
    return result_number

if __name__ == '__main__':
    count_cpu = cpu_count()
    # processes = []
    number = [128, 255, 99999, 10651060]
    timer_start = time()
    with Pool(count_cpu) as pool:
        logger.debug(pool.map(tpl, number))

    timer_finish = time()

    print(f'Timer synchro - {timer_finish-timer_start}s ')

    # assert a == [1, 2, 4, 8, 16, 32, 64, 128]
    # assert b == [1, 3, 5, 15, 17, 51, 85, 255]
    # assert c == [1, 3, 9, 41, 123, 271, 369, 813, 2439, 11111, 33333, 99999]
    # assert d == [1, 2, 4, 5, 7, 10, 14, 20, 28, 35, 70, 140, 76079, 152158, 304316, 380395, 532553, 760790, 1065106, 1521580, 2130212, 2662765, 5325530, 10651060]
