# Exercise 3: Calculate the sum of all numbers from 1 to a given number
n = int(input("Enter number: "))


def sum_calc(n):
    sum = 0
    for i in range(n + 1):
        sum += i

    return sum


res = sum_calc(n)
print(res)
