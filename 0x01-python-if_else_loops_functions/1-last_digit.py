#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
# check if + or - then use modulus to find the last digit
if number > 0:
    last_digit = number % 10
else:
    last_digit = number % -10
# write the print statement for the all cases (the similar part)
output = f"Last digit of {number:d} is {last_digit:d} "
# cases for different last digits
if last_digit > 5:
    output += "and is greater than 5"
elif last_digit == 0:
    output += "and is 0"
elif last_digit < 6 and last_digit != 0:
    output += "and is less than 6 and not 0"
print(output)
