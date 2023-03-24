# Exercise 14: Reverse a given integer number
num = 76542

while num > 0:
    reminder = num % 10
    print(reminder, end="")
    num = num // 10
    