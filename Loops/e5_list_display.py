# Exercise 5: Display numbers from a list using loop
# Conditions:
# The number must be divisible by five
# If the number is greater than 150, then skip it and move to the next number
# If the number is greater than 500, then stop the loop
numbers = [12, 75, 150, 180, 145, 525, 50]

for number in numbers:
    if number > 500:
        break
    if number > 150:
        continue
    if number % 5 == 0 and number <= 150:
        print(number)
    else:
        continue

