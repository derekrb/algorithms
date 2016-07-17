import random

import algorithm


class Algorithm(algorithm.Algorithm):
    '''
    Merge sort algorithm, O(nlogn) complexity.
    '''

    def run(self, arr, key=None):

        n = len(arr)

        # recursive call
        if n > 2:
            i = n / 2
            a = self.run(arr[:i], key=key)
            b = self.run(arr[i:], key=key)

        # base
        elif n == 2:
            return self.merge([arr[0]], [arr[1]], key)
        elif n == 1:
            return arr

        return self.merge(a, b, key)

    def create_input(self, n):
        arr = range(n)
        random.shuffle(arr)
        return arr

    def merge(self, a, b, key):
        c = []

        while a or b:

            if not a:
                c.extend(b)
                return c

            if not b:
                c.extend(a)
                return c

            if self.is_less_than(a[0], b[0], key):
                c.append(a.pop(0))
            else:
                c.append(b.pop(0))
