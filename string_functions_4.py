# SEARCHING
# startswith() -> checks if string starts with given string, returns True/False
# endswith() -> checks if string ends with given string, returns True/False
# in -> to search for a value anywhere in the string, returns True/False
# find() -> returns the STARTING POSITION of the searched value
phone = "+47-176-12345"
print(phone.startswith("+49"))

file = "data_backup.csv"
print(file.endswith(".csv"))
# Check if user is giving real email
email = "asdasd@gmail.com"
print(email.endswith("gmail.com"))
print("@" in email)

url = "https://api.company.com/v1/data"
print("/api" in url)

phone1 = "+48-123-64364"
phone2 = "48-3563-2464"
phone3 = "0048-163-94744"
# Extract only phone number without country code. This is too tedious \/
print(phone1[4:])
print(phone2[3:])
# Returns starting position of a word so the "-". We need the one AFTER that (+1)
print(phone1.find("-"))
print(phone1[phone1.find("-") + 1: ])
print(phone2[phone2.find("-") + 1: ])
print(phone3[phone3.find("-") + 1: ])
