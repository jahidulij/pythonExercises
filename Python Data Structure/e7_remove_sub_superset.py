# Exercise 7: Checks if one set is a subset or superset of another set. If found, delete all elements from that set
first_set = {57, 83, 29}
second_set = {57, 83, 29, 67, 73, 43, 48}

print(f"First set is subset of second set: {first_set.issubset(second_set)}")
print(f"Second set is subset of first set: {second_set.issubset(first_set)}")

print(f"First set is superset of second set: {first_set.issuperset(second_set)}")
print(f"Second set is superset of first set: {second_set.issuperset(first_set)}")

if first_set.issubset(second_set):
    first_set.clear()

if second_set.issubset(first_set):
    second_set.clear()

print(f"First set: {first_set}")
print(f"Second set: {second_set}")
