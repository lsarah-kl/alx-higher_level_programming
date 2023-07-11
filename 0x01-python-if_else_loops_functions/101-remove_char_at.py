#!/usr/bin/python3
# 101-remove_char_at.py


def remove_char_at(str, n):
    """Create  copy of the str without the char positioned at n."""
    if n < 0:
        return (str)
    return (str[:n] + str[n+1:])
