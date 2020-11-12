def evalt(a, b, op):
    a = int(a)
    b = int(b)
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    else:
        assert False


def minmax(expr1, expr2, op):
    pass


def get_maximum_value(expression):
    digits = list(expression[::2])
    n = len(digits)
    operators = list(expression[1::2])

    min_table = [[float("inf") for _ in range(len(digits))] for _ in range(len(digits))]
    max_table = [[float("-inf") for _ in range(len(digits))] for _ in range(len(digits))]

    # - We don't care about the lower triangle in these two matrices
    # - The order of execution here is diagonal: We first fill the main diagonal,
    #   then the one above it, etc.
    #   That is, we fill it in increasing (j-i)

    for i in range(n):
        min_table[i][i] = max_table[i][i] = digits[i]

    for j_minus_i in range(1, len(digits)):
        for i in range(n - j_minus_i):
            j = i + j_minus_i
            assert j <= n
            assert j >= i
            max_table[i][j] = max([max(
                evalt(max_table[i][k], max_table[k+1][j], operators[k]),
                evalt(max_table[i][k], min_table[k+1][j], operators[k]),
                evalt(min_table[i][k], max_table[k+1][j], operators[k]),
                evalt(min_table[i][k], min_table[k+1][j], operators[k])
            ) for k in range(i, j)])

            min_table[i][j] = min([min(
                evalt(max_table[i][k], max_table[k + 1][j], operators[k]),
                evalt(max_table[i][k], min_table[k + 1][j], operators[k]),
                evalt(min_table[i][k], max_table[k + 1][j], operators[k]),
                evalt(min_table[i][k], min_table[k + 1][j], operators[k])
            ) for k in range(i, j)])

    return max_table[0][n-1]


if __name__ == "__main__":
    print(get_maximum_value(input()))
