#!/usr/bin/python3
"""
This module provides a function to print text with indentation.
"""


def text_indentation(text):
    """
    Prints text with 2 new lines after '.', '?' and ':'.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    current_line = ""
    for char in text:
        current_line += char
        if char in ".?:":
            print(current_line.strip())
            print()
            current_line = ""

    if current_line.strip():
        print(current_line.strip(), end="")
