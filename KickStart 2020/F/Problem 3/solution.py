def main():
    t = int(input())  # read a line with a single integer
    for i in range(1, t + 1):
        s, ra, pa, rb, pb, c = map(int, input().split())
        construction = []
        for j in range(c):
            construction.append(list(map(int, input().split())))
        print("Case #{}: {}".format(i, solve(s, ra, pa, rb, pb, c, construction)))


def solve(s, ra, pa, rb, pb, c, construction):
    if c == 2:
        return 0
    if [2,2] in construction:
        return 0
    if ra == 2 and pa == 2:
        return 1
    if rb == 2 and pb == 2:
        return -1
    if c == 1:
        return 1
    if c == 0:
        return 2


if __name__ == '__main__':
    main()
