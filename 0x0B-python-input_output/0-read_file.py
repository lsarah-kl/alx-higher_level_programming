#!/usr/bin/python3
"""
Definition of the read_file function
"""


def read_file(filename=""):
    """""reads UTF8 text file and prints it to stdout"""
    with open(filename, "r", encoding="utf-8") as f:
        print(f.read(), end="")
