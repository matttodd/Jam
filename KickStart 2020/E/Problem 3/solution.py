from functools import reduce
from copy import deepcopy


def main():
    t = int(input())  # read a line with a single integer
    for i in range(1, t + 1):
        n = int(input())
        toys = []
        for j in range(n):
            toys.append(list(map(int, input().split())))
        print("Case #{}: {} {}".format(i, *solve(n, toys)))


def solve(n, toys):
    removals = 0
    temp_removals = 0
    indef = False
    toys2 = deepcopy(toys)
    def_removals = remove_non_value(n, toys2)
    # print(toys2)
    enjoyment = total_enjoyment(n, toys2)
    for i in range(n):
        if not is_definite(toys):
            removals = temp_removals
            indef = True
            break
        remove_longest(n, toys)
        temp_removals += 1
    if indef:
        return removals, 'INDEFINITELY'
    else:
        return def_removals, enjoyment


def is_definite(toys):
    total_fun = reduce(lambda acc, x: acc + x[0], toys, 0)
    for toy in toys:
        if toy[1] > total_fun - toy[0]:
            return True
    return False


def remove_longest(n, toys):
    max = 0
    index = 0
    for i in range(n):
        if toys[i][1] > max:
            max = toys[i][1]
            index = i
    toys[index] = [0, 0]


def total_enjoyment(n, toys):
    total_fun = reduce(lambda acc, x: acc + x[0], toys, 0)
    target = 0
    for i in range(n):
        if toys[i][1] > total_fun - toys[i][0]:
            target = i
            break
    return total_fun + reduce(lambda acc, x: acc + x[0], toys[:target], 0)


def remove_non_value(n, toys):
    total_fun = reduce(lambda acc, x: acc + x[0], toys, 0)
    removals = 0
    for i in range(n):
        next_miss = 0
        for j in range(i+1, n):
            if toys[j][1] > total_fun - toys[j][0]:
                next_miss = j
                break
        if (toys[i][0] < reduce(lambda acc, x: acc + x[0], toys[i+1:next_miss-1], 0)) and (toys[i][1] > total_fun - toys[i][0]):
            toys[i] = [0, 0]
            removals += 1
    return removals


if __name__ == '__main__':
    main()
