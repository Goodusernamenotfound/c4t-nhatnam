while True:
    password = input("Enter new password: ")
    if any(char.isdigit() for char in password): 
        print("New password accepted")
        break
    else:
        print("Invalid: password must contain at least one number")