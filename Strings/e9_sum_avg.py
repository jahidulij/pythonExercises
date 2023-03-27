# Exercise 9: Calculate the sum and average of the digits present in a string
str1 = "PYnative29@#8496"
total = 0
count = 0

for char in str1:
    if char.isdigit():
        total += int(char)
        count += 1

avg = float(total / count)
print(f"Sum: {total}, Average: {avg:.2f}")
