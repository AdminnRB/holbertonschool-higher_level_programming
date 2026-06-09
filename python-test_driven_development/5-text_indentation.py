#!/usr/bin/python3
"""
This is the "5-text_indentation" module.
The module supplies one function, text_indentation(text).
"""


def text_indentation(text):
    """
    Prints a text with 2 new lines after each of these characters: ., ? and :
    There should be no space at the beginning or at the end of each printed line.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    # Mətnin əvvəlində və sonundakı lazımsız boşluqları başlanğıc üçün təmizləyirik
    c = 0
    while c < len(text) and text[c] == ' ':
        c += 1

    while c < len(text):
        print(text[c], end="")
        if text[c] in [".", "?", ":"]:
            print("\n")
            c += 1
            # İşarədən sonra gələn bütün boşluqları keçirik (skip edirik)
            while c < len(text) and text[c] == ' ':
                c += 1
            continue
        c += 1
