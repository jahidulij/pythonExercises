# Exercise 7: Print the following pattern
num = int(input("Enter number: "))

for i in range(num, 0, -1):
    for j in range(i, 0, -1):
        print(j, end=" ")
    print()
