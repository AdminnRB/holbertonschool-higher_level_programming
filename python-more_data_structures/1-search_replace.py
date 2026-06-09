#!/usr/bin/python3
def search_replace(my_list, search, replace):
    """Replaces all occurrences of an element by another in a new list."""
    if my_list is None:
        return []
    return [replace if num == search else num for num in my_list]
