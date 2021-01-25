import sys


def max_number(a, b):
    """
    Return the max of two numbers, without using if/else or comparision.
    En caso de igualdad, se devolvera 0
    :param a: first integer
    :param b: second integer
    :return: a if a > b, b if b >a
    """
    # I want an integer with all zeros except the first bit (the sign), something like 10000...000
    int_length = sys.getsizeof(int()) * 8
    sign_mask = 1 << int_length - 1
    a_sign = (a - b) & sign_mask
    a_sign = a_sign >> (int_length - 1)
    b_sign = (b - a) & sign_mask
    b_sign = b_sign >> (int_length - 1)
    return a * b_sign + b * a_sign