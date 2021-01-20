def main():
    t = int(input())  # read a line with a single integer
    for i in range(1, t + 1):
        r, c = map(int, input().split())
        matrix = []
        for j in range(r):
            matrix.append(input())
        print("Case #{}: {}".format(i, str(solve_problem(r, c, matrix))))


def solve_problem(r, c, matrix):
    required_order = []
    char_set = []
    execution_order = ''
    for i in range(c):
        working_order = []
        for j in range(r-1, -1, -1):
            if matrix[j][i] not in char_set:
                char_set.append(matrix[j][i])
            if len(working_order) == 0:
                working_order.append(matrix[j][i])
            elif (matrix[j][i] != working_order[-1]) and (matrix[j][i] in working_order):
                return -1
            elif matrix[j][i] != working_order[-1]:
                working_order.append(matrix[j][i])
        required_order.append(working_order)

    for k in range(len(char_set)):
        target = list(filter(lambda x: sum([column.index(x) for column in required_order if x in column]) == 0, char_set))[0]
        execution_order += target
        char_set.remove(target)
        for _column in required_order:
            if target in _column:
                _column.remove(target)

    return execution_order


if __name__ == '__main__':
    main()
