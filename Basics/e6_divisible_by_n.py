# Exercise 6: Display numbers divisible by 5 from a list
list1 = [10, 20, 33, 46, 55]


def divisible_by_n(l1, n):
    l2 = []
    for l in l1:
        if l % n == 0:
            l2.append(l)
        else:
            continue
    return l2


print(divisible_by_n(list1, 5))
