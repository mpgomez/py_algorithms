

def solution(args):
    first = None
    last = None
    ranges_string = ""
    is_range = False
    for number in args:
        number = int(number)
        # We are processing the next non consecutive number
        if first == None:
            first = number
        # We have the first element of a possible range, now we need to check if...
        elif last == None:
            # The next number is consecutive, we start a range
            if number == first+1:
                last = number
            # Otherwise, we have an isolated number
            else:
                ranges_string+=",{}".format(first)
                first = number
        # If we are already processing a range
        else:
            # We may increase the range if the numbers are consecutive
            if number == last+1:
                last = number
                is_range = True
            # Or this number doesn't belong to the range
            else:
                ranges_string+=get_range_string(first, last, is_range)
                first = number
                last = None
                is_range = False
    # Process the last elements
    if last:
        ranges_string+=get_range_string(first, last, is_range)
    elif first:
        ranges_string+=",{}".format(first)
    return ranges_string[1:]


def get_range_string(first, last, is_range):
    range_string = ""
    if is_range:
        range_string+=",{}-{}".format(first, last)
    else:
        range_string+=",{}".format(first)
        range_string+=",{}".format(last)
    return range_string