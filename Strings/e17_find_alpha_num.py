# Exercise 17: Find words with both alphabets and numbers
import re

str1 = "Emma25 is Data scientist50 and ab2c 5AI 25 Expert"

matches = re.findall(r'\b\w*\d+\w*\b', str1)

for match in matches:
    print(match)
