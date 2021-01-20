import sys
import logging
logging.basicConfig(filename='log.log')
with open('log.log', 'w'):
    pass


def main():
    t, a, b = list(map(int, input().split()))  # read a line with a single integer
    for i in range(1, t + 1):
        logging.error(i)
        solve_problem(a, b)


def solve_problem(a, b):
    for tupl in [(-5 * (10 ** 8), -5 * (10 ** 8)), (-5 * (10 ** 8), 5 * (10 ** 8)),
                 (5 * (10 ** 8), -5 * (10 ** 8)), (5 * (10 ** 8), 5 * (10 ** 8)), (0, 0)]:
        print(str(tupl[0]) + " " + str(tupl[1]))
        sys.stdout.flush()
        n = input()
        if n == "CENTER":
            return
        if n == "HIT":
            hit = tupl


    logging.error(hit)


if __name__ == '__main__':
    main()

