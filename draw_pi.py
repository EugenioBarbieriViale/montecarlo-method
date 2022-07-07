from random import randint
from turtle import *

write = Turtle()
write.hideturtle()
write.penup()
write.goto(275,300)

write2 = Turtle()
write2.hideturtle()
write2.penup()
write2.goto(-275,300)

r = 100
count = 0

# draw circle
hideturtle()
dot()
penup()
goto(0,-r)
pendown()
circle(r)
left(90)

penup()
forward(r)
pendown()
for i in range(4):
    forward(r)
    right(90)

penup()
speed(0)
for i in range(r**2):
    x = randint(0,r)
    y = randint(0,r)
    if (x**2+y**2<=r**2):
        color("red")
        count+=1
    else:
        color("blue")
    goto(x,y)
    dot()
    write.clear()
    write.write(count*4/r**2, font=("Arial", 20, "normal"))
    write2.clear()
    write2.write(count, font=("Arial", 20, "normal"))

done()
