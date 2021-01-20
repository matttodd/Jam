def main():
    t = int(input())  # read a line with a single integer
    for i in range(1, t + 1):
        n = int(input())
        players = []
        for i in range(n):
            players.append(list(map(int, input().split())))
        print("Case #{}: {}".format(i, solve(n, players)))


def solve(n, players):
    players = sorted(players)
    x = 0
    y = 0
    dist = 0
    for i in range(n):
        x += players[i][0]
        y += players[i][1]
    x = round((x/n)-(n/2))
    y = round(y/n)
    for player in players:
        dist += abs(player[0] - x)
        dist += abs(player[1] - y)
        x += 1

    return dist


if __name__ == '__main__':
    main()
