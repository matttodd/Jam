import math


def main():
    t = int(input())  # read a line with a single integer
    for i in range(1, t + 1):
        n = int(input())
        numbers = list(map(int, input().split()))
        print("Case #{}: {}".format(i, solve(n, numbers)))


def solve(n, numbers):
    count = 0
    for j in range(len(numbers) + 1):
        _sum = 0
        for k in range(j + 1, len(numbers) + 1):
            _sum += numbers[k-1]
            if _sum >= 0:
                square = math.sqrt(_sum)
                if math.floor(square) == math.ceil(square):
                    count += 1

    return count


if __name__ == '__main__':
    main()
