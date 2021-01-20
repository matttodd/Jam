from functools import reduce
import math

def main():
    t = int(input())  # read a line with a single integer
    for i in range(1, t + 1):
        n, k = map(int, input().split())
        times = []
        for j in range(n):
            times.append(list(map(int, input().split())))
        print("Case #{}: {}".format(i, solve_problem(n, k, times)))


def solve_problem(n, k, times):
    times = sorted(times)
    broad_times = [times[0]]
    for time in times[1:]:
        s, e = time[0], time[1]
        processed = False
        for i in range(len(broad_times)):
            btime = broad_times[i]
            if should_merge(s, e, btime[0], btime[1], k):
                broad_times[i] = merge_times(s, e, btime[0], btime[1])
                processed = True
                break
        if not processed:
            broad_times.append(time)

    # print(broad_times)
    final = reduce(lambda x, y: math.ceil((y[1] - y[0])/k) + x, broad_times, 0)
    return final


def merge_times(s1, e1, s2, e2):
    return [min(s1, s2), max(e1, e2)]


def should_merge(s1, e1, s2, e2, k):
    delta1 = e1 - s1
    delta2 = e2 - s2
    excess1 = delta1//k
    excess2 = delta2//k
    if k >= (max(s1, s2) - min(e1, e2) + min(excess1, excess2)):
        return True
    return False


if __name__ == '__main__':
    main()
