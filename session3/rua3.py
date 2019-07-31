from turtle import *
shape("triangle")
speed(0)
pencolor("green")
for i in range(6):
    for i in range(360):
        forward(1.5)
        left(1)
    left(60)
mainloop()