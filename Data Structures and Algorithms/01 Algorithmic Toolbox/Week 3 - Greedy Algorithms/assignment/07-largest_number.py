import sys


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


if __name__ == '__main__':
    input = sys.stdin.read()
    data = input.split()
    a = data[1:]
    print(largest_number(a))
