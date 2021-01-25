def swap_add(a, b):
    """
    version 1
    Swaps a and b in place
    Only works with numeric values
    """
    a = a + b
    b = a - b
    a = a - b
    return a, b

# def swap_or(a, b):
#     """
#     version 2
#     Swaps a and b in place
#     Works with different types - NOT IN PYTHON. We would have to convert to bits first
#     """
#     abyte = bytearray(a)
#     bbyte = bytearray(b)
#     abyte = bytes(x ^ y for (x, y) in zip(abyte, bbyte))
#     bbyte = bytes(x ^ y for (x, y) in zip(abyte, bbyte))
#     abyte = bytes(x ^ y for (x, y) in zip(abyte, bbyte))
#     return a, b

def swap_or(a, b):
    """
    version 2
    Swaps a and b in place
    Works with different types - NOT IN PYTHON. We would have to convert to bits first
    """
    a = a ^ b
    b = a ^ b
    a = a ^ b
    return a, b
    return a, b


def swap(a, b):
    return swap_or(a, b)