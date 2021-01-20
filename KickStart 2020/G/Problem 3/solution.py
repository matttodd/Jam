def main():
    t = int(input())  # read a line with a single integer
    for i in range(1, t + 1):
        w, n = map(int, input().split())
        codes = list(map(int, input().split()))
        print("Case #{}: {}".format(i, solve(w, n, codes)))


def solve(w, n, codes):
    min_moves = w*n/2
    for code in codes:
        running_moves = 0
        for j in range(w):
            diff = abs(codes[j] - code)
            running_moves += min(diff, n-diff)
        min_moves = running_moves if running_moves < min_moves else min_moves

    return min_moves


if __name__ == '__main__':
    main()
