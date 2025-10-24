# CLEANING
# Clean whitespaces
# only left             only right
# lstrip() -> " dog " <- rstrip()
# strip() - both left and right
# Use strip for user inputs since we don't know where they could enter spaces! Doesn't remove spaces inside
text = "  Engineering".lstrip()
print(text)

text = "Engineering  ".rstrip()
print(text)

text = "     Engineering  ".strip()
print(text
      )
# strip() Doesn't remove spaces inside
text = " Data Engineering ".strip()
print(text)

# We can also remove special characters
text = "###Abc###".strip("#")
print(text)

# We can check how many whitespaces we have
text = "  Engineering"
print(len(text))
print(len(text.strip()))

#
nr_of_spaces = len(text) - len(text.strip())  # 2 whitespaces
is_clean = len(text) == len(text.strip())  # False - so not equal to cleaned up string
print("Nr of spaces:", nr_of_spaces)
print("Is my data clean?", is_clean)

# Clean cases

text = "python PROGRAMMING"
print(text.lower())
print(text.upper())
print(text.capitalize())
print(text.swapcase())

# We can use this to compare data from database with what we want etc.
search = "Email ".lower().strip()
data = " emAil".lower().strip()

print(search == data)

# Challenge. Make it look like name:maria | role: data engineer | age: 27
text = "968-Maria, ( D@t@ Engineer );; 27y  "
text = text.replace("968-", "")
text = text.replace("@", "a")
text = text.replace(" ( ", "")
text = text.replace(" )", "")
text = text.replace(";; ", ",")
text = text.replace("y", "")
text = text.rstrip()
text = text.lower()
text = text.lstrip()
text = text.split(",")
# text[0] = text[0].replace(" ", "name: ")
# text[1] = text[1].replace(" ", "role: ")
# text[2] = text[2].replace(" ", "age: ")
print(f"name: {text[0]} | role: {text[1]} | age: {text[2]}")