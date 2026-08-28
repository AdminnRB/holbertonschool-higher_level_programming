#!/usr/bin/python3
def uniq_add(my_list=[]):
    """Adds all unique integers in a list (only once for each integer)."""
    if not my_list:
        return 0
    return sum(set(my_list))
