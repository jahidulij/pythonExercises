# Exercise 18: Print the following pattern
n = 5
ch1 = "*"


def pattern_printer(n, ch1):
    for i in range(0, n):
        for j in range(0, i + 1):
            print("*", end=" ")
        print()

    for i in range(n, 0, -1):
        for j in range(0, i - 1):
            print("*", end=" ")
        print()


pattern_printer(n, ch1)
