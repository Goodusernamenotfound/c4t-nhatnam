from turtle import *
colors = ["red", "blue", "green"]
for number, color in enumerate(colors):
    pencolor(color)
    forward(100)
mainloop()