items = ['nice', 'lol', 'oof']
crud = str(input("Enter C, R, U or D (not case-sensitive) or type exit to exit: "))
while True:
    if crud == "C" or crud == "c":
        new_item = input("Enter new item: ")
        items.append(new_item)
        print("List appended!")
        break
    elif crud == "R" or crud == "r":
        if len(items) == 0:
            print("List is empty")
            break
        else:
            for i in range(len(items)):
                print(items[i])
            break
    elif crud == "U" or crud == "u":
        u1 = int(input("Enter index: "))
        u2 = str(input("Enter item: "))
        items[u1] = u2
        print("List updated!")
        break
    elif crud == "D" or crud == "d":
        delet = int(input("Where to delete?"))
        items.pop(delet)
        print("Item deleted!")
        break
    elif crud == "exit":
        print("Exiting...")
        break
    else:
        print("Invalid input, please try again")