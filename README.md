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
```
