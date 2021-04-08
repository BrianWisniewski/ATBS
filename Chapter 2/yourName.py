name  = ""
while name.lower() != "your name":
    print("Please type your name.")
    name = input()
    if name.lower() == "brian":
        break
print("Thank You!")
