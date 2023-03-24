# Exercise 1: Calculate the multiplication and sum of two numbers
def multiplication_of_two(num1, num2):
    return num1 * num2


def sum_of_two(num1, num2):
    return num1 + num2


num1 = int(input("Enter number 1: "))
num2 = int(input("Enter number 2: "))

mult_res = multiplication_of_two(num1, num2)
sum_res = sum_of_two(num1, num2)
print("Multiplication result is: ", str(mult_res))
print("Sum result is: ", str(sum_res))
