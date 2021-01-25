from collections import Counter

def remove_duplicates(linked_list):
    """
    Function that, given a linked list (dequeue) will remove any duplicates from the list

    :param linked_list: list with duplicates. Will be modified.

    :return None
    """
    different_elements = Counter(linked_list)
    for element in different_elements:
        for i in range(different_elements[element]-1):
            linked_list.remove(element)
