# Exercise 5: Check if the first and last number of a list is the same
list1 = [10, 20, 30, 40, 10]
list2 = [75, 65, 35, 75, 30]


def first_last_item_checker(l1):
    if l1[0] == l1[-1]:
        msg = "First and last number of the list are same"
        return msg
    else:
        msg = "First and last number of the list are not same"
        return msg


print(first_last_item_checker(list1))
print(first_last_item_checker(list2))
