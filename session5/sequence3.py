x = int(input("Enter number (larger than 0): "))
if x<0 or x % 2 == 0:
    print("Error!")
else:
    for i in range(x,0,-2):
        print(i)
    print("0")