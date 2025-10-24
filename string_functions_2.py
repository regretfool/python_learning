# TRANSFORMATIONS
# Concatenation
first_name = "John"
last_name = "Smith"
last_name = first_name + " " + last_name
print(last_name)

folder = "C:/Users/sasshin"
file = "report.csv"
path = folder + "/" + file
print(path)

# f-string
name = "Sam"
age = 34
is_student = False
print(f"My name is {name}, I am {age} years old and student status is {is_student}.")

print(f"2 + 3 = {2 + 3}")
print(f"{{This is a curly bracket}}")

# Splitting strings
stamp = "2026-09-20 14:30"
print(stamp.split(" "))
print(stamp.split(" ")[0].split("-"))

date = "2025-09-25"
print(date.split("-"))

# Useful for example with CSV(spreadsheet) files
csv_file = "1234,Max,USA,1970-10-05,M"
print(csv_file.split(","))

# Multiplier - useful for formatting output
print("ha" * 3)
print("=" * 20)

# Extraction (specific part of a string)
# [start(included) : end(not included) : step]
numbers = "0123456789"
print(numbers[::-1])
text = "Python"
# Extract first character
print(text[0])
print(text[-6])
# Extract last character
print(text[5])
print(text[-1])
# Extract "h"
print(text[3])
print(text[-3])
# Extract the year
print(date[0:4])
print(date[:4])
# Extract the month
print(date[5:7])
# Extract the day
print(date[8:])
print(date[-2:])
# Extract the "-"'s
print(date[4::3])
print(date[-3:3:-3])