import numpy as np
import scipy
import sys


def solve_problem(n, m, houses):
    houses.sort()
    total = 0
    for index, house in enumerate(houses):
        if total + house > m:
            return index
        else:
            total += house

    return len(houses)


def main():
    t = int(input())  # read a line with a single integer
    for i in range(1, t + 1):
        n, m = map(int, input().split())
        houses = np.array(list(map(int, input().split())))
        print("Case #{}: {}".format(i, solve_problem(n, m, houses)))


if __name__ == '__main__':
    main()


print(solve_problem(4, 50, np.array([100])))