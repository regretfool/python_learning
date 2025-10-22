print(2+3)
print("2"+"3")
a = 3  # Integer
b = 3.14  # Float
c = "3"  # String "" is a blank string not a None! " " is a white space, also string
d = False  # Boolean
e = None  # NoneType
f = ()  # Tuple
g = []  # List
h = {}  # Dictionary
print(type(a), type(b), type(c), type(d), type(e), type(f), type(g), type(h))

text = "hi"
number = 13
print(type(text))
print(len(text))
print(text.upper())
print(type(number))
#print(len(number))
#print(number.upper())
print(number.bit_length())

# Challenge 
age = int(input("Your age: "))
height = float(input("Your height (with decimals): "))
name = input("Your name: ")
student = bool(input("Are you a student? (True/False): "))
empty = None

print(age)
print(type(age))
#print(len(age))

print(height)
print(type(height))
#print(len(height))

print(name)
print(type(name))
print(len(name))

print(student)
print(type(student))
# print(len(student))

print(empty)
print(type(empty))
# print(len(empty))