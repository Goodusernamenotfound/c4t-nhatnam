from turtle import *
v = int(input("Enter number of sides: "))
if v<=0:
    print("Error: number can't be 0 or below")
else:
    shape("turtle")
    for i in range(v):
        forward(1000/v)
        left(360/v)