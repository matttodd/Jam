def main():
    t = int(input())  # read a line with a single integer
    for i in range(1, t + 1):
        s = input()
        print(("Case #{}: " + solve_problem(s)).format(i))


def solve_problem(s):
    ans = ""
    curr_depth = 0
    for char in s:
        char = int(char)
        if char > curr_depth:
            ans += "(" * (char - curr_depth)
            curr_depth += (char - curr_depth)
        elif char < curr_depth:
            ans += ")" * (curr_depth - char)
            curr_depth -= (curr_depth - char)
        ans += str(char)

    ans += ")" * curr_depth
    return ans


if __name__ == '__main__':
    main()
