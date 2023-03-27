# Exercise 12: Find the last position of a given substring
str1 = "Hello Emma is a data scientist who knows Python. Emma works at google."
sub_string = "Emma"

temp_str1 = str1.lower()
temp_sub_string = sub_string.lower()

first_index = temp_str1.index(temp_sub_string)
last_index = temp_str1.rfind(temp_sub_string)

print(f"First position of {sub_string} in str1 is: {first_index}")
print(f"Last position of {sub_string} in str1 is: {last_index}")
