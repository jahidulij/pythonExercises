# Exercise 2: Remove and add item in a list
list1 = [54, 44, 27, 79, 91, 41]

# remove the item present at index 4 and add it to the 2nd position and at the end of the list
index_four = list1.pop(4)
list1.insert(2, index_four)
list1.append(index_four)
print(list1)
