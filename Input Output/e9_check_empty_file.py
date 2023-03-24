# Exercise 9: Check file is empty or not
import os

size = os.stat("new_file.txt").st_size

if size == 0:
    print("File is empty")
else:
    print(f"File size is: {size}")
