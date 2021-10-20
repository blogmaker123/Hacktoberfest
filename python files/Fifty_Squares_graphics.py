""" @jacktherock: https://github.com/jacktherock """

# importing libraries
import turtle

turtle.penup()
turtle.setpos(-100,250)
turtle.pendown()
turtle.pencolor('olive')
turtle.write('Fifty Shades of Grey',font=("Arial", 18, "bold"))
turtle.penup()
turtle.setpos(0,0)
turtle.pendown()
turtle.color("black", "white")
turtle.colormode(1.0)
SQUARES = 50
SIDE = 150
shade = 1.0
for count in range(SQUARES):
    turtle.fillcolor(shade, shade, shade)
    turtle.begin_fill()
    turtle.left(360 // SQUARES)
    for side in range(4):
        turtle.forward(SIDE)
        turtle.left(90)
        turtle.end_fill()
        shade -= turtle.colormode() / float(SQUARES)
turtle.penup()
turtle.setpos(150,-270)
turtle.pendown()
turtle.pencolor('blue')
turtle.write('@jacktherock',font=("Arial", 12, "normal"))
turtle.done()
