def main():
    t = int(input())  # read a line with a single integer
    for i in range(1, t + 1):
        n, x = map(int, input().split())
        numbers = list(map(int, input().split()))
        print("Case #{}: {}".format(i, solve_problem(n, x, numbers)))


def solve_problem(n, x, numbers):
    order_left = []

    while len(order_left) != len(numbers):
        for number in range(1, n+1):
            # print(order_left)
            val = numbers[number - 1]
            if val > 0 and val <= x:
                order_left.append(str(number))
            numbers[number - 1] -= x

    return " ".join(order_left)


if __name__ == '__main__':
    main()
