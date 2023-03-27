# Exercise 15: Remove special symbols / punctuation from a string
import re

str1 = "/*Jon is @developer & musician"

res = re.sub(r'[^\w\s]', '', str1)

print(res)
