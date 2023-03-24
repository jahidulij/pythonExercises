# Exercise 4: Write a program to print multiplication table of a given number
num = int(input("Enter number: "))


def mult_table(num):
    for i in range(1, 11):
        print(i * num)


mult_table(num)
