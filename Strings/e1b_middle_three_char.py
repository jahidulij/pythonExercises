# Exercise 1B: Create a string made of the middle three characters
def middle_three_char_finder(str1):
    middle_index = int(len(str1) / 2)

    res = str1[middle_index - 1] + str1[middle_index] + str1[middle_index + 1]
    # print(str1[middle_index - 1], end="")
    # print(str1[middle_index], end="")
    # print(str1[middle_index + 1])
    return res

s1 = middle_three_char_finder("JhonDipPeta")
print(s1)

s2 = middle_three_char_finder("JaSonA")
print(s2)
