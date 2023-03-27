# Exercise 8: Find all occurrences of a substring in a given string by ignoring the case
str1 = "Welcome to USA. usa awesome, isn't it?"
sub_string = "USA"

temp_str = str1.lower()
temp_sub_str = sub_string.lower()

count = temp_str.count(temp_sub_str)
print(f"The {sub_string} count in the string is: {count}")
