rows = int(input("Nhập số hàng: "))
if rows<=0:
    print("Invalid!")
else:
    for i in range (0,4):
        for j in range(0, i + 1):
            print("*", end=' ')
        print()
    for i in range (4,0,-1):
        for j in range(0, i -1):
            print("*", end=' ')
        print()