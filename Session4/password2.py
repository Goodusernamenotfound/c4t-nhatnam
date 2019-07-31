while True:
    password = input("Enter new password: ")
    if any(char.isdigit() for char in password) or len(password) >= 8 : 
        print("New password accepted")
        break
    else:
        print("Invalid: password must contain at least one number or is 8 characters long")