"""See week1_programming_challenges/week1_programming_challenges.pdf

Input: First line contains an integer specifying the number of digits
following in the second line.
Second line contains space-separated list of integers.
"""


def max_pairwise_product(n_numbers, numbers):
    max1 = 0  # highest no
    max2 = 0  # second-highest no

    for n in numbers:
        if n > max1:
            max2 = max1  # demote old first place
            max1 = n
        elif n > max2:
            max2 = n

    product = max2 * max1
    return product


if __name__ == '__main__':
    n_numbers = int(input())
    numbers = map(int, input().split(" "))
    print(max_pairwise_product(n_numbers, numbers))
