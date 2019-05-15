# YouTube Link: https://www.youtube.com/watch?v=u2jTn-Gj2Xw

# One can create a pool of processes which will carry out tasks submitted to
# it with the Pool class.

# A process pool object which controls a pool of worker processes to which
# jobs can be submitted. It supports asynchronous results with timeouts and
# callbacks and has a parallel map implementation.

import time
from multiprocessing import Pool
from dbWriter import dbWriter, batchStatus

def sum_square(ten):
    batch = batchStatus(ten)
    dbWriter(batch)


def sum_square_with_mp(ten):

    start_time = time.time()
    p = Pool()
    result = p.map(sum_square, ten)

    p.close()
    p.join()

    end_time = time.time() - start_time

    print(f"Processing {len(ten)} numbers took {end_time} time using multiprocessing.")


def sum_square_no_mp(ten):

    start_time = time.time()
    result = []

    for i in ten:
        result.append(sum_square(i))
    end_time = time.time() - start_time

    print(f"Processing {len(ten)} numbers took {end_time} time using serial processing.")


if __name__ == '__main__':
    ten = ['27429232', '32778355', '968141', '39381268', '7119961', '575236', '16715413', '558486', '774160330', '7430088']
    sum_square_with_mp(ten)
    sum_square_no_mp(ten)
