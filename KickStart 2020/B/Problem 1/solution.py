

def solve_problem(n, checkpoints):
    total = 0
    for i in range(1, len(checkpoints) - 1):
        if (checkpoints[i] > checkpoints[i-1]) and (checkpoints[i] > checkpoints[i+1]):
            total += 1

    return total


def main():
    t = int(input())  # read a line with a single integer
    for i in range(1, t + 1):
        n = int(input())
        checkpoints = list(map(int, input().split()))
        print("Case #{}: {}".format(i, solve_problem(n, checkpoints)))


if __name__ == '__main__':
    main()
