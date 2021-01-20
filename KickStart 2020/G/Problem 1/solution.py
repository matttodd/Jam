def main():
    t = int(input())  # read a line with a single integer
    for i in range(1, t + 1):
        s = input()
        print("Case #{}: {}".format(i, solve_problem(s)))


def solve_problem(s):
    kicks = 0
    total = 0
    for i in range(len(s)-4):
        # print(s[i:i+5])
        if s[i:i+4] == 'KICK':
            kicks += 1
        elif s[i:i+5] == 'START':
            total += kicks

    return total


if __name__ == '__main__':
    main()
