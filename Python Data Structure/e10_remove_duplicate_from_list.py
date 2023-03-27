# Exercise 10: Remove duplicates from a list and create a tuple and find the minimum and maximum number
sample_list = [87, 45, 41, 65, 94, 41, 99, 94]
unique_list = []
for sample in sample_list:
    if sample in unique_list:
        unique_list.remove(sample)
        continue
    else:
        unique_list.append(sample)
print(unique_list)

unique_tuple = tuple(unique_list)
print(unique_tuple)

max_unique_tuple = max(unique_tuple)
min_unique_tuple = min(unique_tuple)

print(max(f"Max: {max_unique_tuple}"))
print(max(f"Min: {min_unique_tuple}"))

