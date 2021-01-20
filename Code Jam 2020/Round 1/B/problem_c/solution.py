def main():
    t = int(input())  # read a line with a single integer
    for i in range(1, t + 1):
        r, s = list(map(int, input().split()))
        print(("Case #{}: {}".format(i, solve_problem(r, s))))


def solve_problem(r, s):
    bot_i = (r * s) - 2
    deck = [(_r, _s) for _s in range(1, s+1) for _r in range(1, r+1)]
    deck.reverse()
    top_i = bot_i - [x[0] for x in deck].index(1)
    deck.reverse()
    moves = []
    print(top_i, bot_i)
    print(deck)
    while top_i != bot_i:
        moves.append((top_i+1, bot_i-top_i))
        deck = deck[top_i+1:bot_i+1] + deck[:top_i+1]
        deck.reverse()
        top_i = len(deck) - [x[0] for x in deck].index(1)
        deck.reverse()
        if top_i == bot_i:
            break
        for i in range(len(deck)-1, top_i-1, -1):
            if i // deck[i][0] == s:
                bot_i = i
                break
        print(top_i, bot_i)
        print(deck)


def sorted(deck, r):
    for i in range(len(deck)):
        if i // r != deck[i][0]-1:
            return False
    return True


if __name__ == '__main__':
    main()
