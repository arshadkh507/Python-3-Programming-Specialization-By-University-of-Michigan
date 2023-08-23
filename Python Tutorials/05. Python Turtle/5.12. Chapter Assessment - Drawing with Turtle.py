# Write code to draw a regular pentagon (a five-sided figure with all sides the same length).
'''
import turtle

window = turtle.Screen()

pentagon = turtle.Turtle()

for i in range(5):
    pentagon.forward(100)
    pentagon.left(360/5)
'''


# Write a program that uses the turtle module to draw something. It doesn’t have to be complicated, but draw something different than we have done in the past. (Hint: if you are drawing something complicated, it could get tedious to watch it draw over and over. Try setting .speed(10) for the turtle to draw fast, or .speed(0) for it to draw super fast with no animation.)

''' 
import turtle
wn = turtle.Screen()

pic = turtle.Turtle()
pic.speed(0)

distance =  5
for i in range(100):
    pic.left(60)
    pic.forward(distance)
    distance = distance + 2

wn.exitonclick()
'''
