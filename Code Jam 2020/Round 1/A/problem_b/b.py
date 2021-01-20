def main():
    t = int(input())  # read a line with a single integer
    for i in range(1, t + 1):
        n = int(input())
        solve_problem(n, i)
        # print(("Case #{}: " + solve_problem(n)).format(i))


def solve_problem(n, ii):
    curr = 1
    directions = []
    side = True
    max = min([30, n])
    directions.append([max, 1])
    for i in range(max, 1, -1):
        # if i == 1 and curr != n:
            # print("fhjisoeghadign")
        if n - curr >= ((2**(i-1)) + (i-2)):
            curr += 2**(i-1)
            if side:
                directions += [[i, k] for k in range(2, i+1)]
            else:
                directions += [[i, k] for k in range(i-1, 0, -1)]
            side = not side
        else:
            curr += 1
        if i != 1:
            if side:
                directions += [[i-1, 1]]
            else:
                directions += [[i-1, i-1]]
        # print(directions)
    # print(curr)
    print("Case #{}: ".format(ii))
    directions.reverse()
    for pair in directions:
        str_pair = list(map(str, pair))
        print(" ".join(str_pair))


# def solve_problem(n, ii):
#     curr = 1
#     directions = [[1, 1]]
#     side = True
#     # max = min([30, n])
#     # directions.append([max, 1])
#     for i in range(1, 30):
#         if n == curr:
#             break
#
#         if n - curr >= ((2**(i-1)) + (i-1)):
#             curr += 2**(i-1)
#             if side:
#                 directions += [[i, k] for k in range(2, i+1)]
#             else:
#                 directions += [[i, k] for k in range(i-1, 0, -1)]
#             side = not side
#         else:
#             curr += 1
#         if i != 1:
#             if side:
#                 directions += [[i-1, 1]]
#             else:
#                 directions += [[i-1, i-1]]
#         # print(directions)
#     print(curr)
#     print("Case #{}: ".format(ii))
#     directions.reverse()
#     for pair in directions:
#         str_pair = list(map(str, pair))
#         print(" ".join(str_pair))


if __name__ == '__main__':
    main()

