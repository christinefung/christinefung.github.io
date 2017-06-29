from turtle import *
import math
t = Turtle()
setup(500,500)
x_pos = 0
y_pos = 0
penup()
setx(-100)
sety(350)
pendown()
sides = input("How many sides do you want?")
sides = int(sides)
color = input("What color do you want your shape in?")
pencolor(color)
fillcolor(color)
begin_fill()
pendown()
for i in range(sides):
    forward(150)
    right(360/sides)
end_fill()
penup ()
exitonclick()
