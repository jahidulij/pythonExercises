# Exercise 14: Print downward Half-Pyramid Pattern with Star (asterisk)
def down_print(n, ch):
    for i in range(n, 0, -1):
        for j in range(0, i):
            print(ch, end="")
        print()


res = down_print(10, "*")
