def main():
    t = int(input())  # read a line with a single integer
    for i in range(1, t + 1):
        n = int(input())
        tasks = []
        for j in range(n):
            task = list(map(int, input().split()))
            task.append(j)
            tasks.append(task)
        print(("Case #{}: " + solve_problem(sorted(tasks))).format(i))


def solve_problem(tasks):
    ans = list("X" * len(tasks))
    c_available = 0
    j_available = 0

    for task in tasks:
        if task[0] >= c_available:
            ans[task[2]] = "C"
            c_available = task[1]
        elif task[0] >= j_available:
            ans[task[2]] = "J"
            j_available = task[1]
        else:
            return "IMPOSSIBLE"

    return "".join(ans)


if __name__ == '__main__':
    main()
