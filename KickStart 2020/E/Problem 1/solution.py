def main():
    t = int(input())  # read a line with a single integer
    for i in range(1, t + 1):
        n = int(input())
        numbers = list(map(int, input().split()))
        print("Case #{}: {}".format(i, solve_problem(n, numbers)))


def solve_problem(n, numbers):
    ans = 2
    curr = numbers[1] - numbers[0]
    count = 1

    for number in range(1, n):
        # print(numbers[number], numbers[number-1], curr, count)
        if numbers[number] - numbers[number-1] == curr:
            count += 1
            if count > ans:
                ans = count
        else:
            count = 2
            curr = numbers[number] - numbers[number-1]
    return ans


if __name__ == '__main__':
    main()
