# Exercise 9: Check Palindrome Number case-insensitive
def palindrome_checker(str1):
    if str1.lower() == str1.lower()[::-1]:
        msg = "It's a palindrome"
        return msg
    else:
        msg = "It's not a palindrome"
        return msg


s1 = "madam"
res = palindrome_checker(s1)
print(res)
