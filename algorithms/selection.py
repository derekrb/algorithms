import random

import quicksort


class Algorithm(quicksort.Algorithm):
    '''
    Randomized selection of ith order statistic, O(n) time.
    '''

    def run(self, arr, i, l=None, r=None, key=None):

        if l is None and r is None:
            l = 0
            r = len(arr) - 1

        if r - l == 1:
            return arr[r]

        j = self.partition(arr, l, r, key)

        if j == i:
            return arr[j]
        elif j > i:
            return self.run(arr, i, l=l, r=j, key=key)
        else:
            return self.run(arr, i, l=j, r=r, key=key)

    def create_input(self, n):
        arr = self.make_shuffled_sequence(n)
        i = random.randint(0, n - 1)
        return arr, i
