# Exercise 6: Count the total number of digits in a number
number = int(input("Enter number: "))
count = 0

while number != 0:
    number = number // 10
    print(number)
    count += 1

print(f"Total digits are: {count}")
