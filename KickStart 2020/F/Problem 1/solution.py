def main():
    t = int(input())  # read a line with a single integer
    for i in range(1, t + 1):
        n, x = map(int, input().split())
        numbers = list(map(int, input().split()))
        print("Case #{}: {}".format(i, solve_problem(n, x, numbers)))


def solve_problem(n, x, numbers):
    maximum = max(numbers)//x
    order_left = []
    indicies = [0 for _ in range(maximum+1)]

    for number in range(1, n+1):
        # print(order_left)
        order_left.insert(indicies[(numbers[number - 1]-1) // x], str(number))
        for i in range(((numbers[number - 1]-1) // x), len(indicies)):
            indicies[i] += 1

    return " ".join(order_left)


if __name__ == '__main__':
    main()
