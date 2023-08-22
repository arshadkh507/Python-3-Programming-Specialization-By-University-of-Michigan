# Use for loops to make a turtle draw these regular polygons (regular means all sides the same lengths, all angles the same):
# An equilateral triangle
# A square
# A hexagon (six sides)
# An octagon (eight sides)


# ! draw an equilateral triangle
'''
import turtle

wn = turtle.Screen()
norvig = turtle.Turtle()

for i in range(3):
    norvig.forward(100)

    # the angle of each vertice of a regular polygon
    # is 360 divided by the number of sides
    norvig.left(360/3)

wn.exitonclick()
'''


# ! 1 draw a square
'''
import turtle

wn = turtle.Screen()
kurzweil = turtle.Turtle()

for i in range(4):
    kurzweil.forward(100)
    kurzweil.left(360/4)

wn.exitonclick()
'''


# ! draw a hexagon
'''
import turtle

wn = turtle.Screen()
dijkstra = turtle.Turtle()

for i in range(6):
    dijkstra.forward(100)
    dijkstra.left(360/6)

wn.exitonclick()
'''

# ! draw an octogon
'''
import turtle

wn = turtle.Screen()
knuth = turtle.Turtle()

for i in range(8):
    knuth.forward(75)
    knuth.left(360/8)

wn.exitonclick()
'''


#  Write a program to draw a shape like this:
'''
import turtle

window = turtle.Screen()

star = turtle.Turtle()
for i in range(5):
    star.forward(110)
    star.left(216)

  '''
# Write a program to draw a face of a clock that looks something like this:
# https://fopp.umsi.education/books/published/fopp/PythonTurtle/Exercises.html


# Write a program to draw some kind of picture. Be creative and experiment with the turtle methods.


# Create a turtle and assign it to a variable. When you print its type, what do you get?
'''
import turtle
window = turtle.Screen()

t = turtle.Turtle()
print(type(t))   # <class 'turtle.Turtle'>
'''
