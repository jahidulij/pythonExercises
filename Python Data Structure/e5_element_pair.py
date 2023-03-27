# Exercise 5: Create a Python set such that it shows the element from both lists in a pair
first_list = [2, 3, 4, 5, 6, 7, 8, 10]
second_list = [4, 9, 16, 25, 36, 49, 64]

res = zip(first_list, second_list)
res_set = set(res)
print(res_set)

# Alternative
pairs_set = {(x, y) for x, y in zip(first_list, second_list)}
print(pairs_set)
