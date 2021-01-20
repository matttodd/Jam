def main():
    t = int(input())  # read a line with a single integer
    for i in range(1, t + 1):
        n, a, b, c = map(int, input().split())
        print("Case #{}: {}".format(i, solve_problem(n, a, b, c)))


def solve_problem(n, a, b, c):
    if a == b == 1 != n:
        return 'IMPOSSIBLE'
    ans = [n] * c
    for i in range(a-c):
        ans.insert(0, n-1)
    for j in range(b-c):
        ans.append(n-1)
    for k in range(n - len(ans)):
        ans.insert(1, 1)
    if len(ans) > n:
        return 'IMPOSSIBLE'
    else:
        return " ".join(list(map(str, ans)))


if __name__ == '__main__':
    main()
