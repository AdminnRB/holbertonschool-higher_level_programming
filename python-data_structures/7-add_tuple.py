#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    """Adds 2 tuples by evaluating their first two elements."""
    # Əgər element əskikdirsə, sonuna 0-lar əlavə edib ilk 2-sini götürürük
    a = tuple_a + (0, 0)
    b = tuple_b + (0, 0)

    return (a[0] + b[0], a[1] + b[1])
