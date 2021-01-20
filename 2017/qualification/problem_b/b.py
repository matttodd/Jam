def main():
    t = int(input())  # read a line with a single integer
    for i in range(1, t + 1):
        n = int(input())
        print(("Case #{}: " + solve_problem(n)).format(i))
        # print("Case #{}: {} {}".format(i, n + m, n * m))


def solve_problem(n):
    pass


if __name__ == '__main__':
    main()
