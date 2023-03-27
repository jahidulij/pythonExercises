# Exercise 14: Remove empty strings from a list of strings
str_list = ["Emma", "Jon", "", "Kelly", None, "Eric", ""]

# new_str_list = []
#
# for s in str_list:
#     if s:
#         new_str_list.append(s)
#
# print(new_str_list)

# Alternative method using filter() function
new_list = list(filter(None, str_list))

print(new_list)
