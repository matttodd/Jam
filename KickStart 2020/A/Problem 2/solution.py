import numpy as np
import scipy
import sys


def solve_problem(p, k, stacks):

    plates_used = []

    for stack_count, stack in enumerate(stacks):
        plates_used.append(0)
        for plate in stack:
            if p > sum(plates_used):
                plates_used[stack_count] += 1
            else:
                stack_subset = [stacks[:len(plates_used)][index][location - 1] for index, location in enumerate(plates_used)]
                least_value_index = stack_subset.index(min(stack_subset))
                print(plate)
                print(stack_subset)
                print(min(stack_subset))
                print(least_value_index)
                if plate <= min(stack_subset):
                    continue
                plates_used[least_value_index] -= 1
                plates_used[stack_count] += 1

    ans = 0
    for ii in range(len(plates_used)):
        ans += sum(stacks[ii][:plates_used[ii]])

    return ans




    # knapsack = [[0 for _ in range(p + 1)] for _ in range(k + 1)]
    #
    # for ii in range(k + 1):
    #     for jj in range(p + 1):
    #         print(knapsack)
    #         if ii == 0 or jj == 0:
    #             knapsack[ii][jj] = 0
    #         else:
    #             knapsack[ii][jj] = max(stacks[ii - 1][jj] + max([]), knapsack[ii - 1][jj])
    #
    # for bag in knapsack:
    #     print(bag)
    # return knapsack[k][p]






        # if p > (len(stack) + sum(plates_per_stack)):
        #     plates_per_stack.append(len(stack))
        # else:
        #     for plate in stack:
        #         for processed_stack, plates_taken in enumerate(plates_per_stack):







            # for index, plates in enumerate(plates_per_stack):
            #     for value in reversed(range(plates)):
            #         if stacks[index][value] < stack.




def main():
    t = int(input())  # read a line with a single integer
    for i in range(1, t + 1):
        n, k, p = map(int, input().split())
        stacks = np.array([list(map(int, input().split())) for _ in range(n)])
        print("Case #{}: {}".format(i, solve_problem(p, k, stacks)))


if __name__ == '__main__':
    main()