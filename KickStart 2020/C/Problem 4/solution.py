def main():
    t = int(input())  # read a line with a single integer
    for i in range(1, t + 1):
        n, q = map(int, input().split())
        numbers = list(map(int, input().split()))
        print("Case #{}: {}".format(i, solve_problem(n, q, numbers)))


# Probably some super efficient query flattening
def solve_problem(n, q, numbers):
    running = 0
    for i in range(q):
        action, p1, p2 = input().split()
        p1, p2, = int(p1), int(p2)
        if action == 'U':
            numbers[p1 - 1] = p2
        else:
            cur = 1
            for j in range(p1-1, p2):
                running += (cur * (numbers[j] * (j-p1+2)))
                cur *= -1

    return running


if __name__ == '__main__':
    main()
