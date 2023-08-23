# print("This will execute first")

# # This Block of code executed 3 times
# for _ in range(3):
#     print("This line will execute three times")
#     print("This line will also execute three times")

# print("Now we are outside of the for loop!")


# ================================================================
import turtle


background_color = input("Enter Background Color for window:")
turtle_color = input("Enter Turtle Color:")
pen_size = input("Enter Turtle pen size:")

window = turtle.Screen()
window.bgcolor(background_color)
window.delay(100)

arshad = turtle.Turtle()
arshad.color(turtle_color)
arshad.pensize(int(pen_size))
arshad.pencolor("red")
arshad.shape('turtle')

# for counter in range(40):
#     arshad.stamp()
#     arshad.left(15)
#     arshad.forward(25)


distance = 5
arshad.up()

for counter in range(30):
    arshad.stamp()                # leave an impression on the canvas
    arshad.forward(distance)          # move arshad along
    arshad.right(24)              # and turn his
    distance = distance + 2

window.exitonclick()
