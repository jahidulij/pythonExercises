# Exercise 16: Calculate the cube of all numbers from 1 to a given number
num = int(input("Enter number: "))

for i in range(1, num + 1):
    cube = pow(i, 3)
    print(f"Current Number: {i} and Cube: {cube}")
