# Exercise 8: Generate a Python list of all the even numbers between 4 to 30
start = 4
end = 30
new_list = []

for i in range(start, end):
    if i % 2 == 0:
        new_list.append(i)
    else:
        continue

print(new_list)
