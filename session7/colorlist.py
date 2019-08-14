colors = ["red", "blue", "green", "white"]
print("Our color list:")
print(*colors, sep=(", "))
newcolor = str(input("Enter a new color: "))
colors.append(newcolor)
print("Our new color list:")
print(*colors, sep=(", "))
