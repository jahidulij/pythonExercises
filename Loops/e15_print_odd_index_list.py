# Exercise 15: Use a loop to display elements from a given list present at odd index positions
my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

for list in range(len(my_list)):
    if list % 2 == 0:
        continue
    else:
        print(my_list[list], end=" ")
