while True:
    txt = input("Enter year of birth:")
    print(txt)
    if txt.isdigit():
        print("A number")
        break
    else:
        print("Not a number")

print(2018 - int(txt))