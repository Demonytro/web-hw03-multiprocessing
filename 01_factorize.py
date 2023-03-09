from time import time
import logging


logger = logging.getLogger()
stream_handler = logging.StreamHandler()
logger.addHandler(stream_handler)
logger.setLevel(logging.DEBUG)


def factorize(*number):
    result_number = []
    for num in number:

        count = range(num+1)[1:]

        res1 = []
        for i in count:

            if not num % i:
                res1.append(i)

        result_number.append(res1)
    return result_number


if __name__ == '__main__':
    timer_start = time()

    a, b, c, d = factorize(128, 255, 99999, 10651060)

    timer_finish = time()
    logger.debug(f"{a}, {b}, {c}, {d}")
    print(f'Timer synchro - {timer_finish-timer_start}s ')

    assert a == [1, 2, 4, 8, 16, 32, 64, 128]
    assert b == [1, 3, 5, 15, 17, 51, 85, 255]
    assert c == [1, 3, 9, 41, 123, 271, 369, 813, 2439, 11111, 33333, 99999]
    assert d == [1, 2, 4, 5, 7, 10, 14, 20, 28, 35, 70, 140, 76079, 152158, 304316, 380395, 532553, 760790, 1065106, 1521580, 2130212, 2662765, 5325530, 10651060]
