"""My 07-largest_number.py solution fails one of the tests.
I'll create a reference solution (slow, but guaranteed to be correct) and an infinite loop script,
that spits out random numbers and compares my solution to the reference solution until it finds
a disagreement.

----

The problem was: Correctly, "636" > "63", because "63663" > "63636". But my code put "63" > "636".

----

Solution: My weird_greater_than_or_equal was shitty. Found this online:

Another way to solve this is to note that in the best arrangement, for any two adjacent original
integers X and Y, the concatenation X followed by Y will be numerically greater than or equal to
the concatenation Y followed by X.
"""

import random
from itertools import permutations


def rfill(number, to_length):
    if len(number) < to_length:
        number = number + (number[0] * (to_length - len(number)))
    return number


def weird_greater_than_or_equal(x, y):
    x = str(x)
    y = str(y)
    strlen = max(len(x), len(y))

    # If one number is shorter, fill the right end up with the first digit
    x = rfill(x, strlen)
    y = rfill(y, strlen)

    # Now do string comparison (each character starting left)
    return x >= y


def largest_number(a):
    res = ""
    while a:
        largest = '0'
        for i in a:
            if weird_greater_than_or_equal(i, largest):
                largest = i
        res += largest
        a.remove(largest)

    return res


def reference_solution(a):
    answer = ""
    for pi in permutations(a):
        concat = ""
        for a_i in pi:
            concat += a_i
        answer = max(answer, concat)
    return answer


while True:
    # n = random.randint(1, 100)
    n = random.randint(1, 7)
    arr = [str(random.randint(1, 1000)) for _ in range(n)]

    ref = reference_solution(arr)
    my = largest_number(arr.copy())

    if ref != my:
        print(arr)
        print(ref)
        print(my)
        break