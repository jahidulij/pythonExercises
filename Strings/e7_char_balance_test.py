# Exercise 7: String characters balance Test
# If all chars of s1 is present in s2. Chars position doesn't matter
s1 = "Yn"
s2 = "PYnative"
s3 = "Ynf"
s4 = "PYnative"

def char_balance_test(s1, s2):
    flag = True

    for char in s1:
        if char in s2:
            continue
        else:
            flag = False
    return flag


char_balance = char_balance_test(s1, s2)
print(char_balance)

char_balance2 = char_balance_test(s3, s4)
print(char_balance2)
