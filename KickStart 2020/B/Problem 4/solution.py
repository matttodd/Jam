import math


def solve_problem(w, h, l, u, r, d):
    n1 = (d + l - 2)
    n2 = (r + u - 2)
    print(n1, n2)
    d1 = (l - 1) * (math.factorial(n1)/(math.factorial(d)*math.factorial(n1 - d))) if n1 - d >= 0 else 0
    d2 = (u - 1) * (math.factorial(n2)/(math.factorial(r)*math.factorial(n2 - r))) if n2 - r >= 0 else 0

    return d1*((1/2)**d) + d2*((1/2)**r)


def main():
    t = int(input())  # read a line with a single integer
    for i in range(1, t + 1):
        w, h, l, u, r, d = map(int, input().split())
        print("Case #{}: {}".format(i, solve_problem(w, h, l, u, r, d)))


if __name__ == '__main__':
    main()
