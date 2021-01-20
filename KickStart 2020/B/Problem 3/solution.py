

def solve(s, index):
    solved = ""
    while index < len(s):
        if s[index] in ['N', 'S', 'E', 'W']:
            solved += s[index]
            index += 1
        elif s[index] is ')':
            return solved
        else:
            sub = get_paren(s[index+1:])
            to_add = solve(sub, 0)
            solved += int(s[index]) * to_add
            index += len(sub)+3
    return solved


def get_paren(s):
    paren = 0
    for i in range(len(s)):
        if s[i] == '(':
            paren += 1
        elif s[i] == ')':
            paren -= 1
        if paren == 0:
            return s[1:i]


def count(dir):
    NS = dir.count('S') - dir.count('N')
    WE = dir.count('E') - dir.count('W')
    if NS < 0:
        NS = 10**9 + NS
    NS += 1
    if WE < 0:
        WE = 10**9 + WE
    WE += 1
    return WE, NS


def main():
    t = int(input())  # read a line with a single integer
    for i in range(1, t + 1):
        s = input()
        w, h = count(solve(s, 0))
        print("Case #{}: {} {}".format(i, w, h))


if __name__ == '__main__':
    main()
