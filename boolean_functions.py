# bool
print(True)
print(False)
print(type(True))
print(bool(123))
print(bool())  # False = empty or 0
print(bool(0))  # False = empty or 0
print(bool("0"))  # True - a string
print(bool("Hi"))
print(bool(None))  # None isn't empty - it's missing!
print("-------")

# all - returns True if all values are True
# any - returns True if at least one is True
email = "" # spacebar -> will make True (whitespace)
phone = "0234-23575"
username = "user1213"
# Allows registration if any field is filled
print(any([email, phone, username]))
# Allows registration if all fields are filled
print(all([email, phone, username]))
print("-------")

# isistance - checks if a value belongs to a certain data type
print(isinstance(123, int))
print(isinstance("123", int))
print(isinstance(True, str))
print(isinstance("True", bool))
print("-------")

# endswith/startswith
print("Hello".endswith("o"))
print(isinstance(("Hello".endswith("d")), str))