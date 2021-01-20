def main():
    t = int(input())  # read a line with a single integer
    for i in range(1, t + 1):
        n, k, s = list(map(int, input().split()))
        print("Case #{}: {}".format(i, solve_problem(n,k,s)))


def solve_problem(n,k,s):
    leave = (k - 1) + n + 1
    go_back = (k - 1) + (k - s) + (n - s + 1)
    return min(leave, go_back)


if __name__ == '__main__':
    main()
