#!/usr/bin/python3
def no_c(my_string):
    """Removes all characters c and C from a string."""
    new_string = [char for char in my_string if char not in ('c', 'C')]
    return "".join(new_string)
