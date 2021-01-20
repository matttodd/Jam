import sys


SWAP = {'0': '1', '1': '0'}


def main():
    t, b = list(map(int, input().split()))
    for i in range(1, t + 1):
        solve_problem(b)


def solve_problem(b):
    bits = [None] * b
    same_index = None  # None means unsure of swap rev or nothing
    different_index = None  # None means unsure of rev or nothing
    for i in range(5):
        print(i + 1)
        sys.stdout.flush()
        inp = input()
        bits[i] = inp

        print(b - i)
        sys.stdout.flush()
        inp = input()
        bits[b - i - 1] = inp

        if bits[i] == bits[b - i - 1]:
            same_index = i
        else:
            different_index = i

    processed = 4
    guess_count = 10
    while processed < ((b/2)-1):

        if guess_count % 10 == 0:
            if same_index is None or different_index is None:
                print(1)
                sys.stdout.flush()
                first = input()
                if same_index is None:
                    if first != bits[0]:
                        bits.reverse()
                elif different_index is None:
                    if first != bits[0]:
                        bits = [SWAP[bit] if bit is not None else None for bit in bits]
                print(1)
                sys.stdout.flush()
                _ = input()

            else:
                print(same_index + 1)
                sys.stdout.flush()
                first_same = input()
                print(different_index + 1)
                sys.stdout.flush()
                first_diff = input()

                if first_same == bits[same_index]:
                    if first_diff == bits[different_index]:
                        pass  # nothing case
                    else:
                        bits.reverse()  # rev case
                else:
                    if first_diff == bits[different_index]:
                        bits.reverse()  # swap rev case
                        bits = [SWAP[bit] if bit is not None else None for bit in bits]
                    else:
                        bits = [SWAP[bit] if bit is not None else None for bit in bits]  # swap case
        else:
            processed += 1

            print(processed + 1)
            sys.stdout.flush()
            inp = input()
            bits[processed] = inp

            print(b - processed)
            sys.stdout.flush()
            inp = input()
            bits[b - processed - 1] = inp

            if bits[processed] == bits[b - processed - 1]:
                same_index = processed
            else:
                different_index = processed

        guess_count += 2

    print("".join(bits))
    sys.stdout.flush()
    input()
    return


if __name__ == '__main__':
    main()
