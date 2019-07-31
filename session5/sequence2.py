x = int(input("Enter number (larger than 0): "))
if x<0:
    print("Error!")
else:
    for i in range(-1,x):
        print(i+1)