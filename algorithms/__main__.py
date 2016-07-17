#!/usr/bin/env python

import argparse
import logging

FORMAT = '%(asctime)s %(levelname)s: %(message)s'


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--algorithm', type=str, default=None,
                        help='Name of algorithm module to run')
    parser.add_argument('--n', type=int, default=None,
                        help='Integer size of input for algorithm')
    parser.add_argument('--n_max', type=int, default=None,
                        help='Maximum input size for iterative run')
    parser.add_argument('--step', type=int, default=1,
                        help='Input step size for iterative runs')
    parser.add_argument('--poly', type=int, default=1,
                        help='Polynomial exponent for complexity check')
    parser.add_argument('--log', type=int, default=0,
                        help='Log exponent for complexity check')
    args = parser.parse_args()
    logging.basicConfig(format=FORMAT, level=logging.DEBUG)

    algorithm = __import__(args.algorithm).Algorithm()

    if not args.n_max:
        logging.info('Running algorithm {} with n={}'.format(
            args.algorithm, args.n)
        )
        output = algorithm.run_one(args.n)
        logging.info('Completed with output: {}'.format(output))
        return

    logging.info('Iterating algorithm {} from n={} to n={} '
                 '(step={})'.format(args.algorithm, args.n, args.n_max,
                                    args.step)
    )
    times = algorithm.run_iter(args.n, args.n_max, args.step)
    constants = algorithm.check_complexity(times, args.poly, args.log)

    logging.info('Constants for complexity n^{} * log(n^{}): {}'.format(
        args.poly, args.log, constants)
    )


if __name__ == '__main__':
    main()
