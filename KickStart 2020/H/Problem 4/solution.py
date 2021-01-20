import math


def main():
    t = int(input())  # read a line with a single integer
    for i in range(1, t + 1):
        n = int(input())
        cards = list(map(int, input().split()))
        print("Case #{}: {}".format(i, solve_problem(n, cards)))


def solve_problem(n, cards):
    finals = 0
    queue = [(cards, 0)]
    for item in queue:
        if len(item[0]) == 1:
            finals+=item[1]
        else:
            for i in range(len(item[0])-1):
                cpy = item[0].copy()
                first = cpy.pop(i)
                cpy[i] += first
                queue.append((cpy, item[1] + cpy[i]))
    # print(finals)
    return finals / math.factorial(n-1)


if __name__ == '__main__':
    main()
