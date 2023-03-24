# Exercise 10: Read line number 4 from the following file
with open("new_file.txt", "r") as f:
    lines = f.readlines()
    print(lines[3])
