# Exercise 2: Append new string in the middle of a given string
def append_str_in_middle(str1, val):
    middle_index = int(len(str1) / 2)

    res = str1[:middle_index] + val + str1[middle_index:]
    return res

s1 = append_str_in_middle("JoeDipPeta", "Tintin")
print(s1)

s2 = append_str_in_middle("Ault", "Kelly")
print(s2)
