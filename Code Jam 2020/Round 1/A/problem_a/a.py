def main():
    t = int(input())  # read a line with a single integer
    for i in range(1, t + 1):
        n = int(input())
        matrix = []
        for j in range(n):
            matrix.append(list(map(int, input().split())))

        k, r, c = solve_problem(n, matrix)
        print("Case #{}: {} {} {}".format(i, k, r, c))


def solve_problem(n, matrix):
    trace = 0
    repeated_cols = 0
    repeated_rows = 0
    for i in range(n):
        trace += matrix[i][i]
        if len(set(matrix[i])) < n:
            repeated_rows += 1
        if len(set(row[i] for row in matrix)) < n:
            repeated_cols += 1

    return trace, repeated_rows, repeated_cols


if __name__ == '__main__':
    main()
