

def solve_problem(n, d, routes):
    ans = d
    routes.reverse()
    for route in routes:
        ans = ans - (ans % route)
    return ans


def main():
    t = int(input())  # read a line with a single integer
    for i in range(1, t + 1):
        n, d = map(int, input().split())
        routes = list(map(int, input().split()))
        print("Case #{}: {}".format(i, solve_problem(n, d, routes)))


if __name__ == '__main__':
    main()
