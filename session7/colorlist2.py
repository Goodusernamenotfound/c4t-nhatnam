colors = ["red", "blue", "green", "white"]
print("Current colors:")
for i, item in enumerate(colors):
    print (i+1,".",item)
delet = input("Item to delete: ")
if delet == "red" or delet == "blue" or delet == "green" or delet == "white":
    colors.remove(delet)
elif delet == "1" or delet == "2" or delet == "3" or delet == "4":
    colors.pop(int(delet)-1)
else:
    print("Invalid input, please try again")
print("Colors left:")
for i, item in enumerate(colors):
    print (i+1,".",item)


    