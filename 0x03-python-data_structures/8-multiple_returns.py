#!/usr/bin/python3
# 8-multiple_returns.py


def multiple_returns(sentence):
    """funtion that returns the length and 1st character of string."""
    if sentence == "":
        return (0, None)
    return (len(sentence), sentence[0])
