# Exercise 4: Remove first n characters from a string
def remove_n_char(str1, n):
    if n < len(str1):
        return str1[n:]
    else:
        msg = "n must be less than the length of the string"
        return msg


res = remove_n_char("pynative", 4)
print(res)
