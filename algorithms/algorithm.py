import math
import time
import random


class Algorithm(object):
    '''
    Abstract algorithm class.
    '''

    def run_iter(self, n_min, n_max, step=1):
        times = []
        for n in range(n_min, n_max, step):
            data_in = self._create_input(n)

            start = time.time()
            self.run(*data_in)
            t = time.time() - start
            times.append((n, t))

        return times

    def run_one(self, n):
        data_in = self._create_input(n)
        return self.run(*data_in)

    def run(self, data_in):
        raise NotImplementedError

    def create_input(self, data_in):
        raise NotImplementedError

    def _create_input(self, n):
        data_in = self.create_input(n)
        if not isinstance(data_in, tuple):
            data_in = (data_in,)
        return data_in

    @staticmethod
    def make_shuffled_sequence(n):
        arr = range(n)
        random.shuffle(arr)
        return arr

    @staticmethod
    def make_random_ints(n, x_min=0, x_max=1000):
        return [random.randint(x_min, x_max) for r in xrange(n)]

    @staticmethod
    def is_less_than(a, b, key):
        if key is None:
            return a <= b
        else:
            return a[key] <= b[key]

    @staticmethod
    def euclidean(p1, p2):
        deltas = [(p2[i] - p1[i]) ** 2 for i, _ in enumerate(p1)]
        return math.pow(sum(deltas), 0.5)

    @staticmethod
    def check_complexity(data_out, poly_expn, log_expn=0, log_base=2):
        constants = []

        for n, t in data_out:
            n_factor = math.pow(n, poly_expn)
            if log_expn:
                n_factor *= math.log(math.pow(n, log_expn), log_base)
            constants.append(t / n_factor)

        return constants
