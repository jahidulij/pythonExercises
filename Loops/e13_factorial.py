# Exercise 13: Find the factorial of a given number
num = int(input("Enter number: "))
res = 1
for i in range(1, num + 1):
    res *= i

print(res)
