# Exercise 6: Create a mixed String using the following rules
# Given two strings. Make new one where first char of s1 then last char of s2 and so on
s1 = "Abcde"
s2 = "Xyzrnqfl"


def mixed_string(s1, s2):
    len_s1, len_s2 = len(s1), len(s2)
    s3 = ""

    for i in range(max(len_s1, len_s2)):
        if i < len_s1:
            s3 += s1[i]
        if i < len_s2:
            s3 += s2[len_s2 - i - 1]
    return s3


mixed_string_s3 = mixed_string(s1, s2)
print(mixed_string_s3)
