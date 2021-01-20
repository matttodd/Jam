def main():
    t = int(input())  # read a line with a single integer
    for i in range(1, t + 1):
        n, k = map(int, input().split())
        numbers = list(map(int, input().split()))
        print("Case #{}: {}".format(i, solve_problem(n, k, numbers)))


def solve_problem(n, k, numbers):
    count = 0
    streak = 0

    for number in numbers:
        if number == k:
            streak = 1
        elif number == k - streak:
            streak += 1
        else:
            streak = 0

        if streak == k:
            streak = 0
            count += 1

    return count


if __name__ == '__main__':
    main()
