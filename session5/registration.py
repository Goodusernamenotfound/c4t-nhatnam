while True:
    username = str(input("Enter username: "))
    email = str(input("Enter email: "))
    if "@" and "." in email:
        password = str(input("Enter password: "))
        if any(char.isdigit() for char in password) and len(password) >= 8 :
            retype = str(input("Retype password: "))
            if password == retype:
                print("Registration complete!")
                break
            else:
                print("Passwords do not match, please try again")
        else:
            print("Invalid: password must contain 8 characters including at least a number")
    else:
        print("Invalid email!")