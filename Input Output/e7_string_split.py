# Exercise 7: Accept any three string from one input() call
names = input("Enter names here: ")
name_split = names.split()
i = 1
for name in name_split:
    print(f"Name {i}: {name}")
    i += 1
