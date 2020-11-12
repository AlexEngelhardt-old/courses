"""The stress test will run an infinite loop and:

- generate a random problem input
- compare the results of a naive (slow, but "surely" correct) solution
  with your fast but maybe wrong implementation
- break and output the results if they don't agree (i.e. you found a bug)
"""

import random
from a00_maximum_pairwise_product import max_pairwise_product


def max_pw_pr_naive(n_numbers, numbers):

    max_prod = 0
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            if numbers[i] * numbers[j] > max_prod:
                max_prod = numbers[i] * numbers[j]
    return max_prod


if __name__ == '__main__':
    while True:
        n = random.randrange(start=2, stop=100)
        numbers = [random.randrange(start=0, stop=100000) for i in range(n)]

        mp = max_pairwise_product(n, numbers)
        mp_naive = max_pw_pr_naive(n, numbers)

        if mp != mp_naive:
            print('corner case found')
            print(numbers)
            print(mp)
            print(mp_naive)
            break
