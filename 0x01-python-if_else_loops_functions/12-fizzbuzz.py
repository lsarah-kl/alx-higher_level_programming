#!/usr/bin/python3
# 12-fizzbuzz.py


def fizzbuzz():
    """Print the nums from 1 to 100 separated by a space.

    if multiples of three, print Fizz instead.
    if multiples of five, print Buzz instead.
    if multiples of three and five, print FizzBuzz instead.
    """
    for number in range(1, 101):
        if number % 3 == 0 and number % 5 == 0:
            print("FizzBuzz ", end="")
        elif number % 3 == 0:
            print("Fizz ", end="")
        elif number % 5 == 0:
            print("Buzz ", end="")
        else:
            print("{} ".format(number), end="")
