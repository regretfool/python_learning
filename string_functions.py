# TYPES

name = "Johnny"
print(type(name))

age = 28
print(type(age))
print("Your age is:" + str(age)) # Doesn't change the data type
print(type(age))
age = str(age)  # Changes the type to str
print(type(age))
age = age + "5"
print(type(age))

# MATH

password = "12535f3a24  "
# len() Returns the number of items in a value/characters in string
# whitespace is also one characer
if len(password) < 8:
    print("Your password is too short!")
else:
    print(len(password))

# count() Returns how often a word appears in a string    
text = """ 
Python is easy to learn.
Python is powerful
Many people love python
"""
# we want to count occurences of "python". CASE-SENSITIVE!!
print(text.count("python"))

# Transformations

# replace()  (old value, new value)
date = "2025/04/09"
print(date.replace("/", "-"))

# We can transform strings to use them in code later, for example turn this into a float
price = "1234,56"
print(price.replace(",", "."))

phone = "123-4567-89"
print(phone.replace("-", ""))

# We can also use it a few times to remove different characters
cost = "$1,299.99"
print(price.replace("$", "").replace(",", ""))

# Challenge
# Remove all characters. Turn the messy phone number into a clean number with only digits
phone_number = "+49 (176) 123-4567"
print(phone_number.replace("+", "00").replace("(", "").replace(")", "").replace("-", "").replace(" ", ""))