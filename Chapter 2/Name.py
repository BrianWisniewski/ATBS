print("What is your first name?")
firstName = input()
print("Do you have a middle name?")
if input().lower() == "yes":
    print("What is your middle name?")
    middleName = input() + " "
else:
    middleName = ""
print("What is your last name?")
lastName = input()
print("Your full name is " + firstName + " " + middleName + lastName + ".")
