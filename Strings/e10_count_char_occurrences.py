# Exercise 10: Write a program to count occurrences of all characters within a string
str1 = "hello world"

char_dict = dict()

for char in str1:
    count = str1.count(char)
    char_dict[char] = count
print(f"Result: {char_dict}")
