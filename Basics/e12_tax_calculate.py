# Exercise 12: Calculate income tax for the given income by adhering to the below rules
# For first 10000 rate 0%, next 10000 rate 10%, remaining 20%
income = 45000
tax_payable = 0

if income <= 10000:
    tax_payable = 0
elif income > 10000 and income <= 20000:
    tax = (income * 10) / 100
    tax_payable += tax
else:
    tax = (10000 * 10) / 100
    income -= 20000
    tax_payable = tax + ((income * 20) / 100)

print(tax_payable)
