import random

import algorithm


class Algorithm(algorithm.Algorithm):
    '''
    Quicksort algorithm, O(nlogn) complexity. Sorts in-place.
    '''

    def run(self, arr, l=None, r=None, key=None):

        if l is None and r is None:
            l = 0
            r = len(arr) - 1

        if len(arr[l:r]) <= 1:
            return

        i = self.partition(arr, l, r, key)
        self.run(arr, l=l, r=i, key=key)
        self.run(arr, l=i, r=r, key=key)

        return arr

    def partition(self, arr, l, r, key):
        p = random.randrange(l, r)
        arr[l], arr[p] = arr[p], arr[l]

        i = l + 1

        for j in range(l + 1, r + 1):
            if self.is_less_than(arr[j], arr[l], key):
                arr[j], arr[i] = arr[i], arr[j]
                i += 1

        arr[l], arr[i - 1] = arr[i - 1], arr[l]

        return i - 1

    def create_input(self, n):
        return self.make_shuffled_sequence(n)
