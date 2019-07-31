while True:
    name = input("Enter your name: ")
    print(name)
    if any(char.isdigit() for char in name):
        print("Invalid!")
    else:
        break