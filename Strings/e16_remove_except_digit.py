# Exercise 16: Removal all characters from a string except integers
import re
str1 = 'I am 25 years and 10 months old'

# integers = re.sub(r'\D', '', str1)

# Alternative using isdigit() function
integers = ""
for char in str1:
    if char.isdigit():
        integers += char

print(integers)
