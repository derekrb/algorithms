# TODO

import time
import numpy as np



def main():

    for n in range(4, 10, 10):

        # define input array
        mat = np.random.rand(n, n) * 10
        print mat


if __name__ == '__main__':
    main()
