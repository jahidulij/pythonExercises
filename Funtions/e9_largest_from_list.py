# Exercise 9: Find the largest item from a given list
x = [4, 6, 8, 24, 12, 2]

print(max(x))

# Using loop
my_list = [1, 5, 3, 9, 2, 8, 4]

largest_value = my_list[0]

for i in range(1, len(my_list)):
    if my_list[i] > largest_value:
        largest_value = my_list[i]

print(f"Largest value is: {largest_value}")
