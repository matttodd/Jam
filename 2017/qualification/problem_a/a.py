def main():
    t = int(input())  # read a line with a single integer
    for i in range(1, t + 1):
        inputs = input().split(" ")
        s = inputs[0]
        k = int(inputs[1])  # read a list of integers, 2 in this case
        print(("Case #{}: " + solve_problem(s, k)).format(i))
        # print("Case #{}: {} {}".format(i, n + m, n * m))


def solve_problem(s, k):
    grill = [-1 if pancake is '-' else 1 for pancake in s]
    count = 0
    while True:
        if is_done(grill):
            return str(count)
        elif is_impossible(grill, k):
            return 'IMPOSSIBLE'
        grill = grill[grill.index(-1):]
        if is_done(grill):
            return str(count)
        elif is_impossible(grill, k):
            return 'IMPOSSIBLE'
        grill = list(map(lambda a: a * -1, grill[:k])) + grill[k:]
        count += 1


def is_done(grill):
    return True if grill.count(1) == len(grill) else False


def is_impossible(grill, k):
    return len(grill) < k


if __name__ == '__main__':
    main()
