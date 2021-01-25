
def is_unique_v1(string):
    """
    Function that verifies if all the characters in a string are unique. It is case sensitive, meaning "A" and "a" are considered different characters

    :param string: string to verify for uniqueness.

    :return True: if it doesn’t have any duplicate characters
    False: otherwise
    """
    string_set = set(list(string))
    if len(string_set) == len(string):
        return True
    else:
        return False

def is_unique_v2(string):
    """
    Function that verifies if all the characters in a string are unique. It is case sensitive, meaning "A" and "a" are
    considered different characters. It avoids using extra data structures, but it is SLOW (n^2)

    :param string: string to verify for uniqueness.

    :return True: if it doesn’t have any duplicate characters
    False: otherwise
"""
    for char in string:
        count = 0
        for other_char in string:
            if char == other_char:
                count += 1
            if count > 1:
                return False
    return True

def is_unique_v3(string):
    """
    Function that verifies if all the characters in a string are unique. It is case sensitive, meaning "A" and "a" are
    considered different characters. It avoids using extra data structures, but it is SLOW, but a bit faster, n*nlogn

    :param string: string to verify for uniqueness.

    :return True: if it doesn’t have any duplicate characters
    False: otherwise
    """
    for i in range(len(string)-1):
        for j in range(i+1, len(string)):
            if string[i] == string[j]:
                return False
    return True


def is_unique(string):
    return is_unique_v3(string)
