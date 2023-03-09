from time import time
from multiprocessing import cpu_count
import logging
import concurrent.futures

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

    with concurrent.futures.ProcessPoolExecutor(count_cpu) as executor:
        logger.debug(executor.map(factorize, number))

    timer_finish = time()

    print(f'Timer asynchro (concurrent.futures) - {timer_finish - timer_start}s ')
