import turtle
myPen = turtle.Pen()

import turtle

def draw_star(t, size, color):
    """Draws a five-pointed star with the given turtle, size, and color."""
    t.color(color)
    t.begin_fill()
    for _ in range(5):
        t.forward(size)
        t.right(144)
    t.end_fill()

# Set up the screen
screen = turtle.Screen()
screen.title("Five-Pointed Star")
screen.bgcolor("black")

# Create a turtle
star_turtle = turtle.Turtle()
star_turtle.shape("turtle")
star_turtle.color("yellow")
star_turtle.speed(2)

# Position the turtle
star_turtle.penup()
star_turtle.goto(0, -100)
star_turtle.pendown()

# Draw the star
draw_star(star_turtle, size=200, color="gold")

# Hide the turtle and display the window
star_turtle.hideturtle()
turtle.done()
