# VALIDATION
# Check if country has only letters
country = "USA2"
print(country.isalpha())
# Check if phone number is only numeric. DOESN'T ALLOW FLOAT NUMBERS "." is a char
phone = "297319312"
number = "3.245"
print(phone.isnumeric())