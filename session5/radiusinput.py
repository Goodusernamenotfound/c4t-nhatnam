from turtle import *
r = float(input("Enter radius: "))
if r<=0:
    print("Invalid: radius must be larger than 0")
else:
    shape("turtle")
    circle(r)
    mainloop()