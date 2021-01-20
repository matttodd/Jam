def main():
    t = int(input())  # read a line with a single integer
    for i in range(1, t + 1):
        u = int(input())
        print("Case #{}: {}".format(i, solve_problem(u)))


def solve_problem(u):
    results = {x: set() for x in range(10)}
    saved = set()
    for j in range(10**4):
        q, r = input().split()
        if (len(q) + len(r)) != (2 * u):
            continue
        # for k in range(1, int(q[0]) + 1):
        results[int(q[0])].add(r[0])
        saved.add(r[len(r) - 1])
        # print(results)

    final_str = ""
    used = set()
    for k in range(1, 10):
        # print(final_str)
        val = list(filter(lambda x: x not in used, results[k]))[0]
        final_str += val
        used.add(val)
    final_str = saved.symmetric_difference(results[9]).pop() + final_str

    # for key in results:
    #     print(results[key])
    return final_str


if __name__ == '__main__':
    main()
