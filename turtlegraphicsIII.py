import turtle

# Set up the screen
screen = turtle.Screen()
screen.title("Smiley Face using Turtle Graphics")
screen.bgcolor("white")

# Create a turtle named myPen
myPen = turtle.Turtle()
myPen.speed(10)

# Draw the face (large circle)
myPen.penup()
myPen.goto(0, -200)  # Move to the bottom of the face circle
myPen.pendown()
myPen.begin_fill()
myPen.fillcolor("pink")  # Face color
myPen.circle(200)  # Face radius
myPen.end_fill()

# Draw the left eye
myPen.penup()
myPen.goto(-80, 50)  # Position for the left eye
myPen.pendown()
myPen.begin_fill()
myPen.fillcolor("black")  # Eye color
myPen.circle(25)  # Left eye size
myPen.end_fill()

# Draw the right eye
myPen.penup()
myPen.goto(80, 50)  # Position for the right eye
myPen.pendown()
myPen.begin_fill()
myPen.circle(25)  # Right eye size
myPen.end_fill()

# Draw the mouth (semi-circle for a smile)
myPen.penup()
myPen.goto(-100, -70)  # Move to starting point for the smile
myPen.setheading(-60)  # Set orientation to start drawing the smile
myPen.width(5)
myPen.pendown()
myPen.circle(120, 120)  # Draw a 120-degree arc of a circle

# Hide the turtle when drawing is complete
myPen.hideturtle()

# Keep the window open
turtle.done()
