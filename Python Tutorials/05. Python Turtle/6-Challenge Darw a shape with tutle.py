from turtle import *

window = Screen()
window.bgcolor("white")

arshad = Turtle()
arshad.color('green')
arshad.fillcolor('red')
arshad.pencolor('SlateGray')
arshad.pensize(1)


# ! one
arshad.hideturtle()  # make the turtle invisible
arshad.penup()  # don't draw when turtle moves
arshad.goto(0, -60)  # move the turtle to a location
arshad.showturtle()  # make the turtle visible
arshad.pendown()  # draw when the turtle moves

arshad.forward(80)
arshad.left(90)
arshad.forward(150)
arshad.left(90)
arshad.forward(80)
arshad.left(90)
arshad.forward(150)

# ! Two

arshad.hideturtle()  # make the turtle invisible
arshad.penup()  # don't draw when turtle moves
arshad.goto(-300, -230)  # move the turtle to a location
arshad.showturtle()  # make the turtle visible
arshad.pendown()  # draw when the turtle moves


arshad.left(90)
arshad.forward(600)
arshad.left(90)
arshad.forward(500)
arshad.left(90)
arshad.forward(600)
arshad.left(90)
arshad.forward(500)

# ! Three

arshad.hideturtle()
arshad.penup()
arshad.goto(250, 0)
arshad.showturtle()
arshad.pendown()


arshad.left(90)
arshad.forward(100)
arshad.left(90)
arshad.forward(150)
arshad.left(90)
arshad.forward(100)
arshad.left(90)
arshad.forward(150)

arshad.right(90)    # table one foot
arshad.forward(100)
arshad.left(90)
arshad.forward(100)
arshad.left(90)
arshad.forward(100)
arshad.left(90)
arshad.forward(100)
arshad.right(90)
arshad.forward(100)

# ! Four Bed

arshad.hideturtle()
arshad.penup()
arshad.goto(-300, 270)
arshad.showturtle()
arshad.pendown()

arshad.right(90)
arshad.forward(300)
arshad.left(90)
arshad.forward(300)
arshad.left(90)
arshad.forward(300)
arshad.left(90)
arshad.forward(300)

window.exitonclick()
