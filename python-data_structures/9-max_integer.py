#!/usr/bin/python3
def max_integer(my_list=[]):
    """Finds the biggest integer of a list without using builtin max()."""
    if not my_list or len(my_list) == 0:
        return None

    biggest = my_list[0]
    for num in my_list:
        if num > biggest:
            biggest = num

    return biggest
