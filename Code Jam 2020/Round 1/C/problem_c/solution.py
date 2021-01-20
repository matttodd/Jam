def main():
    t = int(input())  # read a line with a single integer
    for i in range(1, t + 1):
        n, d = map(int, input().split())
        angles = list(map(int, input().split()))
        print(("Case #{}: " + solve_problem(n, d, angles)).format(i))


def solve_problem(n, d, angles):
    counts = []
    for i in range(n):
        counts.append(angles.count(angles[i]))
        if angles.count(angles[i]) == d:
            return "0"
    # print(angles)
    # print(counts)
    if n == 1:
        return str(d - 1)
    if d == 2:
        return "1"
    if d == 3:
        if (2 in counts) and (n > 2) and (angles[counts.index(2)] != max(angles)):
            return "1"
        else:
            for i in range(n):
                if (angles[i] / 2 in angles) or (angles[i] * 2 in angles):
                    return "1"
            return "2"


if __name__ == '__main__':
    main()
