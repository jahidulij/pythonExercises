# Exercise 15: Write a function called exponent(base, exp)
# that returns an int value of base raises to the power of exp.
import math


def exponent(base, exp):
    return math.pow(base, exp)


res = exponent(5, 4)
print(res)
