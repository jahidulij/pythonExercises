# Exercise 12: Display Fibonacci series up to 10 terms
num1 = 0
num2 = 1

for i in range(1, 11):
    res = num1 + num2
    print(num1, end=" ")
    num1 = num2
    num2 = res
