# All my Python learning files
### Course followed for Python fundamentals: https://www.youtube.com/playlist?list=PLNcg_FV9n7qZGfFl2ANI_zISzNp257Lwn
###### Also first time using and learning markdown 😊

### PRINT, INPUT, SPECIAL CHARACTERS, VARIABLES
```
print()
print(f"{variable}")
\n \t \b \\ \' \" {{ }}
[special character] * x  -> "=" * 10
> input()
to_variable = input("Prompt")
// rounded division
```
### DATA TYPES
```
int, float, string, bool, NoneType, tuple, list, dict
>type(var)  # returns data type of var
> bit_length()  # how many bits in binary
> conversions: int(var), str(), float(), bool()
```
### STRING FUNCTIONS
```
# MATH

> len(string)
> count(string)  # counts occurences of string in target string
"""block
string"""  # allows for multiline string without \n

# EXAMPLE

text = """ 
Python is easy to learn.
Python is powerful
Many people love python
"""
print(text.count("python"))

# TRANSFORMATION

> replace("old_string", "new_string")

# CONCATENATION
" " + string_value

# STRING SPLITTING
> split()  # splits string on given character and turns it into a list
date.split("-")

# INDEXING / STRING EXTRACTION
[start(included) : end(not included) : step]
-5 -4 -3 -2 -1 -> negative indexing
 h  e  l  l  o
 0  1  2  3  4 -> positive indexing

# CLEANING WHITESPACES
only left             only right
> lstrip() -> " dog " <- rstrip()
> strip() - both left and right
Use strip for user inputs since we don't know where they could enter spaces!
DOESN'T REMOVE SPACES INSIDE STRING

# CLEANING CASES
> lower()
> upper()
> capitalize()
> swapcase()

# SEARCHING
> startswith()  # checks if string starts with given string, returns True/False
> endswith()  # checks if string ends with given string, returns True/False
> in  # searches value in value, returns True/False
> find()  # returns the STARTING POSITION of the searched value

# VALIDATION
> isalpha()  # checks if string contains only letters
> isnumeric()  # checks if string contains only numbers. float numbers (".") are not allowed, "." is a char
# both return True/False
```
### NUMERIC FUNCTIONS
```
# NUMERIC TYPES
> int()
> float()
> complex(a, b)  -> eg. 2 + 5j

# MATH OPERATORS
+
-
*
/
//  -> rounded division (floor). int output
%  -> remainder. prints leftover. useful for checking if number is even or odd
**  -> exponentation. base to power of exponent

# OPERATOR SHORTCUTS
x += 3  --is short for -->  x = x + 3
+=
-=
*=
/=

# ROUNDING
> abs()  # useful for measuring distance/size. always positive value

to use the functions below:

import math    

> floor()  # rounds EVERYTHING down
> ceil()  # rounds everything up
> round()  # rounds everything up OR down TO THE NEAREST EVEN VALUE. round(1.5) is 2 etc.
we can also set amount of decimal spaces for round()
round(value, 3)  # 3 decimal spaces
> trunc()  # removes decimal spaces without rounding. equivalent of int()

# RANDOM NUMBERS
requires importing random module

import random

> random.random()  # generates a random float number
> random.randint(from, to)  # generates a random int number in range from to to

# NUMBER VALIDATION
> x.isinteger()  # checks if value(of x object) is an int. returns True/False. is a !!class method!!
> isinstance(value, float)  # we can check if value is an int or float etc
```
