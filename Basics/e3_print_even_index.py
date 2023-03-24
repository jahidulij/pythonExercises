# Exercise 3: Print characters from a string that are present at an even index number
user_input = str(input("Enter your string: "))

for i in range(len(user_input)):
    if i % 2 == 0:
        print(user_input[i])
    else:
        continue
