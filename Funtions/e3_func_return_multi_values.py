# Exercise 3: Return multiple values from a function
def calculation(a, b):
    sum = a + b
    sub = a - b
    return sum, sub


res = calculation(40, 10)
print(res)
