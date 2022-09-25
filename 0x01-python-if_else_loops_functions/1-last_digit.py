#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
x = number % -10 if number < 0 else number % 10
if x > 5:
    result = "greater than 5"
elif x == 0:
    result = "0"
else:
    result = "less than 6 and not 0"
print(f"Last digit of {number:d}", f"is {x:d} and is", result)
