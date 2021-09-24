import time
import numpy as np
from numpy import random


def timer_function(start, stop):
    elapsed = (stop - start)
    elapsed_output = "{:,}".format(elapsed)
    print(f"Elapsed time:\t{elapsed_output} ns")


def timed_code(t):
    print(f'\nRandom between 1 and {t}')
    tic = time.perf_counter_ns()  # start
    rand_num = np.random.randint(1, t, 1)
    print(f"Your random number: {rand_num}")
    toc = time.perf_counter_ns()  # stop
    timer_function(tic, toc)  # output


timed_code(100)
timed_code(20)
timed_code(10)
timed_code(5)