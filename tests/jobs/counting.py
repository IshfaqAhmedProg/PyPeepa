import time


def counting(n):
    start = time.time()
    while n > 0:
        n -= 1
    return time.time() - start
