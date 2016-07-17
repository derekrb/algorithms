# TODO

import random
import time
import math


def sort_count(arr, inv):

    n = len(arr)

    # recursive call
    if n > 2:
        i = n / 2
        a, inv_a = sort_count(arr[:i], inv)
        b, inv_b = sort_count(arr[i:], inv)

    # base
    elif n == 2:
        return merge_count([arr[0]], [arr[1]], inv)
    elif n == 1:
        return arr, 0
    return merge_count(a, b, inv_a + inv_b)


def merge_count(a, b, inv):

    c = []

    while a or b:
        if not a:
            c.extend(b)
            return c, inv
        if not b:
            c.extend(a)
            return c, inv

        if a[0] <= b[0]:
            c.append(a.pop(0))
        else:
            c.append(b.pop(0))
            inv += len(a)


def nlogn(time, n):
    return time / (n * math.log(n, 2))


def choose(n, r):
    return math.factorial(n) / math.factorial(r) / math.factorial(n - r)


def main():

    for n in range(2, 10, 1):

        # define input array
        arr = range(n)
        random.shuffle(arr)

        # let's go!
        start = time.time()
        print sort_count(arr, 0), choose(n, 2)
        end = time.time()

        print n, end - start, nlogn(end - start, n)


if __name__ == '__main__':
    main()
