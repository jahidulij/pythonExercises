# Exercise 1: Create a list by picking an odd-index items from the first list and even index items from the second
l1 = [3, 6, 9, 12, 15, 18, 21]
l2 = [4, 8, 12, 16, 20, 24, 28]
l3 = []

for l in range(0, len(l1)):
    if l % 2 == 0:
        continue
    else:
        l3.append(l1[l])

for l in range(0, len(l2)):
    if l % 2 == 0:
        l3.append(l2[l])
    else:
        continue

print(l3)
