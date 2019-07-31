while True:
    n = input("Enter a number: ")
    if n.isdigit():
        print("Your number has", len(n), "digits")
        break
    else:
        print("Invalid: not a number.")