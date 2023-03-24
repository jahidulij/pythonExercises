# Exercise 3: Create a new string made of the first, middle, and last characters of each input string
def fml_giver(str1, str2):
    first_char = str1[0] + str2[0]
    mid_index_str1 = int(len(str1) / 2)
    mid_index_str2 = int(len(str2) / 2)
    mid_char = str1[mid_index_str1] + str2[mid_index_str2]
    last_char = str1[-1] + str2[-1]
    res = first_char + mid_char + last_char

    return res

s1 = "America"
s2 = "Japan"

result1 = fml_giver(s1, s2)
print(result1)
