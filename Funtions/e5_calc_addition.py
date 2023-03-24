# Exercise 5: Create an inner function to calculate the addition in the following way
def calc_addition_outer(a, b):

    def calc_addition_inner(a, b):
        sum = a + b
        return sum

    sum = calc_addition_inner(a, b)
    return sum + 5


res = calc_addition_outer(5, 10)
print(res)
