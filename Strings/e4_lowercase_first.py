# Exercise 4: Arrange string characters such that lowercase letters should come first
str1 = "PyNaTive"
lc = ""
uc = ""

for s in range(len(str1)):
    if str1[s].islower():
        lc = lc + str1[s]
    else:
        uc = uc + str1[s]

new_str = lc + uc
print(new_str)
