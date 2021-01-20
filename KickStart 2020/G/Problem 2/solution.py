def main():
    t = int(input())  # read a line with a single integer
    for i in range(1, t + 1):
        n = int(input())
        coins = []
        for j in range(n):
            coins.append(list(map(int, input().split())))
        print("Case #{}: {}".format(i, solve_problem(n, coins)))


def solve_problem(n, coins):
    cur_max = 0
    for i in range(n):
        cur_sum = sum([coins[j][i+j] for j in range(n-i)])
        cur_max = cur_sum if cur_sum > cur_max else cur_max
    for i in range(n):
        cur_sum = sum([coins[i+j][j] for j in range(n-i)])
        cur_max = cur_sum if cur_sum > cur_max else cur_max
    return cur_max


if __name__ == '__main__':
    main()
