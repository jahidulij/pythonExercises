# Exercise 2: Create a function with variable length of arguments


def func1(*args):
    for arg in args:
        print(arg, end=", ")
    print()


# call function with 3 arguments
func1(20, 40, 60)

# call function with 2 arguments
func1(80, 100)
