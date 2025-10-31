# NUMERIC TYPES
x = 5
y = 5.7
z = 2 + 3j

print(type(x))
print(type(y))
print(type(z))

print(int(y))  # Removes decimal without rounding
print(float(x))  # Converts into float, adds a .0 decimal
a = 3  # Real
b = 4  # Complex
print(complex(a, b))

# MATH OPERATORS
print(2 + 3)
print(5 - 3)
print(4 * 2)
print(7 / 2)
print(7 // 2)  # Rounded division (floor), int output
print(7 % 2)  # Remainder. Prints leftover. Good to check if even or odd (0/1)
print(2 ** 3)  # Exponentation. Base to power of exponent

# OPERATOR SHORTCUTS
x = 2
x = x + 3
x += 3
print(x)
x -= 1
print(x)
x *= 2
x /= 2

# ROUNDING
# Measure distance between points/size of something
print(abs(2 - 10))  # We need absolute value. abs()
# Need to import math module for rounding
import math

print("Rounding")
price = 35.664278995
print(math.floor(price)) # Floor rounds everything down
print(math.ceil(price)) # Ceiling rounds everything up
print(round(price)) # Round rounds everything down or up TO THE EVEN NUMBER!
print(round(2.5))
print(round(3.5))
print(round(1.5))
print(round(0.5))
# Specifying decimal spaces works only for round()
print(round(price, 2))  # 2 decimal spaces
print(round(price, 1))  # 1 decimal space
# Just removing decimals without rounding with trunc()
print(math.trunc(price))
print(int(price))  # Or just use int() if you're not importing math

# RANDOM NUMBERS
import random

print("Random")
print(random.random())  # random Float
print(random.randint(1, 6))  # Generates a random int in range from 1 to 6. Like rolling a dice
# Can for example generate a random sized list with random elements
rlist = []
for x in range(random.randint(1,10)):
    rlist.append(random.randint(20,50))
print(rlist)

# NUMBER VALIDATION
x = 7.0
print(x.is_integer())  # We can check if a number is an int
y = 7.3
print(y.is_integer())

x = 70.63
print(isinstance(x, int))  # We cancheck if value is an int
print(isinstance(x, float))  # or a float


# Challenge
# Generate a random integer between 1 and 100 and check if the result is an even number
number = random.randint(1, 100)
if number % 2 == 0:
    print(f"{number} is an even number")
else:
    print(f"{number} is an odd number")