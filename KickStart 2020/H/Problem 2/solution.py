def main():
    t = int(input())  # read a line with a single integer
    for i in range(1, t + 1):
        l, r = list(map(int, input().split()))
        print("Case #{}: {}".format(i, solve_problem(l, r)))


# def solve_problem(l, r):
#     r = str(r+1)
#     l = str(l)
#     below_l = (0.5**(len(l) - 1)) * (10**(len(l) - 1)) if len(l) > 1 else 0
#     below_r = (0.5**(len(r) - 1)) * (10**(len(r) - 1)) if len(r) > 1 else 0
#     # print(below_l, below_r)
#     for i in range(1, len(l)+1):
#         for j in range(int(l[i - 1])):
#             if (j % 2) == (i % 2):
#                 mag = len(l) - i
#                 # print(i, j, (.5 ** mag) * (10 ** mag))
#                 below_l += (.5 ** mag) * (10 ** mag)
#         if (int(l[i - 1]) % 2) != (i % 2):
#             # print('broke l')
#             break
#
#     for i in range(1, len(r)+1):
#         for j in range(int(r[i - 1])):
#             if (j % 2) == (i % 2):
#                 mag = len(r) - i
#                 # print(i, j, (.5 ** mag) * (10 ** mag))
#                 below_r += (.5 ** mag) * (10 ** mag)
#         if (int(r[i - 1]) % 2) != (i % 2):
#             # print('broke r')
#             break
#
#     # print(below_l, below_r)
#     return int(below_r - below_l)


def solve_problem(l, r):
    count = 0
    for i in range(l, r+1):
        s = str(i)
        good = True
        for j in range(1, len(s)+1):
            if j % 2 != int(s[j-1]) % 2:
                good = False
        if good:
            count += 1

    return count


if __name__ == '__main__':
    main()
