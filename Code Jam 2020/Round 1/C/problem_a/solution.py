def main():
    t = int(input())  # read a line with a single integer
    for i in range(1, t + 1):
        x, y, m = input().split()
        print(("Case #{}: " + solve_problem(int(x), int(y), m)).format(i))


def solve_problem(x, y, m):
    my_x = x
    my_y = y
    time = 0
    for direction in m:
        time += 1
        if direction == "S":
            my_y -= 1
        elif direction == "W":
            my_x -= 1
        elif direction == "N":
            my_y += 1
        elif direction == "E":
            my_x += 1
        if abs(my_x) + abs(my_y) <= time:
            return str(time)
    return "IMPOSSIBLE"


if __name__ == '__main__':
    main()
