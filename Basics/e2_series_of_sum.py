# Exercise 2: Print the sum of the current number and the previous number upto 10
previous_number = 0
current_number = 0

for i in range(10):
    sum_of_both = previous_number + current_number
    print("Previous Number: ", previous_number, " Current Number: ", current_number, " Sum: ", sum_of_both)
    previous_number = current_number
    current_number += 1

