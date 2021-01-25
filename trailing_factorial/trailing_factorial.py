def factorial(n):
    if n < 1:
        raise ArithmeticError()
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)


def count_trailing_zeros(n):
    return len(str(n)) - len( str(n).rstrip('0'))


def count_trailing_zeros_factorial(n):
    count = 0
    for y in range(1, n+1):
        while y >= 5 and y % 5 == 0:
            y = y / 5
            count += 1
    return count
