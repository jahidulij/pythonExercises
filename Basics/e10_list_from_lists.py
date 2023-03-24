# Exercise 10: Create a new list from a two list using the following condition
# New list = Combination of odd number from list1 & even number from list2
list1 = [10, 20, 25, 30, 35]
list2 = [40, 45, 60, 75, 90]

list3 = []
for l in list1:
    if l % 2 == 1:
        list3.append(l)
    else:
        continue

for l in list2:
    if l % 2 == 0:
        list3.append(l)
    else:
        continue

print(list3)
