def main():
    t = int(input())  # read a line with a single integer
    for i in range(1, t + 1):
        x, y = list(map(int, input().split()))

        print("Case #{}: {}".format(i, solve_problem(x, y, "")))


def solve_problem(x, y, acc):

    if x == 0 and y == 0:
        return acc

    if (abs(x) + abs(y)) % 2 == 0:
        return "IMPOSSIBLE"

    if x == 0:
        if y == 1:
            return acc + 'N'
        elif y == -1:
            return acc + 'S'
    elif y == 0:
        if x == 1:
            return acc + 'E'
        elif x == -1:
            return acc + 'W'

    if x % 2 == 1:
        if (abs((x - 1) // 2) + abs(y // 2)) % 2 == 1:
            return solve_problem((x - 1) // 2, y // 2, acc + "E")
        else:
            return solve_problem((x + 1) // 2, y // 2, acc + "W")
    else:
        if (abs(x // 2) + abs((y - 1) // 2)) % 2 == 1:
            return solve_problem(x // 2, (y - 1) // 2, acc + "N")
        else:
            return solve_problem(x // 2, (y + 1) // 2, acc + "S")


if __name__ == '__main__':
    main()
