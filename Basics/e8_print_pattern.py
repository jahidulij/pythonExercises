# Exercise 8: Print the pattern
def print_pattern_upto_n(n):
    for num in range(n + 1):
        for i in range(num):
            print(num, end=" ")
        print()


print(print_pattern_upto_n(5))
