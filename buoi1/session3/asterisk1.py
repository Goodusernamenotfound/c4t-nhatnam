rows = int(input("Nhập số hàng: "))
if rows<=0:
    print("Invalid!")
else:
    for i in range (0, rows):
        for j in range(0, i + 1):
            print("*", end=' ')