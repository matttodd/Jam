from collections import deque
from itertools import permutations


def main():
    t = int(input())  # read a line with a single integer
    for i in range(1, t + 1):
        n, k = list(map(int, input().split()))
        solve_problem(i, n, k)


def solve_problem(i, n, k):

    if (k == n + 1) or (k == (n**2) - 1):
        print(("Case #{}: IMPOSSIBLE".format(i)))
        return

    latin_diagonal = []  # Values making up the trace
    small_val = k // n  # smaller of two main values along diagonal
    num_max = k % n  # number of larger numbers needed

    # Populate diagonal with starting values
    for ii in range(n):
        if ii < num_max:
            latin_diagonal.append(small_val + 1)
        else:
            latin_diagonal.append(small_val)

    # Check if a number is used in all cases but 1 and increment and decrement one accordingly
    if latin_diagonal.count(small_val) == 1:
        latin_diagonal[latin_diagonal.index(small_val + 1)] = small_val + 2
        latin_diagonal[latin_diagonal.index(small_val + 1)] = small_val
    elif latin_diagonal.count(small_val + 1) == 1:
        latin_diagonal[latin_diagonal.index(small_val)] = small_val + 1
        latin_diagonal[latin_diagonal.index(small_val)] = small_val - 1

    perms = list(map(list, permutations(range(1, n+1))))
    perms.reverse()

    for starting_combo in perms:
        # populate latin square with starting values
        latin_square = []  # Latin square matrix
        for index, val in enumerate(latin_diagonal):
            start_row = [0] * n
            start_row[index] = val
            latin_square.append(start_row)
        # Permute needed values and insert into latin square
        for index, row in enumerate(latin_square):
            values_to_use = starting_combo.copy()
            values_to_use.remove(row[index])

            for combo in permutations(values_to_use):
                for jj in range(n):
                    if jj < index:
                        row[jj] = combo[jj]
                    elif jj > index:
                        row[jj] = combo[jj - 1]
                    elif jj == index:
                        row[jj] = row[index]

                # Stop if row is valid
                if valid_square(n, latin_square):
                    break

        if valid_square(n, latin_square):
            break

    # :D
    if valid_square(n, latin_square):
        print(("Case #{}: POSSIBLE".format(i)))
        for row in latin_square:
            str_row = map(str, row)
            print(" ".join(str_row))
    else:
        print(("Case #{}: IMPOSSIBLE".format(i)))
        # for row in latin_square:
        #     str_row = map(str, row)
        #     print(" ".join(str_row))
    return


def valid_square(n, square):
    for i in range(n):
        for j in range(1, n + 1):
            if (square[i].count(j) > 1) or ([sub[i] for sub in square].count(j) > 1):
                return False
    return True


if __name__ == '__main__':
    main()
