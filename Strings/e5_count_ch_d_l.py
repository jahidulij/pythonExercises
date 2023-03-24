# Exercise 5: Count all letters, digits, and special symbols from a given string
str1 = "P@#yn26at^&i5ve"
dig_count = 0
char_count = 0
symbol_count = 0

for i in range(len(str1)):
    if str1[i].isdigit():
        dig_count += 1
    elif str1[i].isalpha():
        char_count += 1
    else:
        symbol_count += 1

print(f"Chars: {char_count}")
print(f"Digits: {dig_count}")
print(f"Symbols: {symbol_count}")
