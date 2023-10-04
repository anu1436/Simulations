import turtle
import math

# Screen setup
wn = turtle.Screen()
wn.bgcolor("white")
wn.title("Wave Interference")
wn.tracer(0)  # Disable automatic screen updates

# Create turtles for two waves, interference, and labels
wave1 = turtle.Turtle()
wave1.color("blue")
wave1.speed(0)

wave2 = turtle.Turtle()
wave2.color("red")
wave2.speed(0)

interference = turtle.Turtle()
interference.color("green")
interference.speed(0)

labels = turtle.Turtle()
labels.color("black")
labels.speed(0)
labels.hideturtle()

# Function to draw wave
def draw_wave(turt, offset, color):
    turt.clear()
    turt.color(color)
    for i in range(400):
        x = i - 200
        y = 50 * math.sin((x + offset) / 10.0)
        turt.up()
        turt.goto(x, y)
        turt.down()
        turt.forward(1)

# Function to draw labels and legends
def draw_labels():
    labels.clear()
    labels.up()
    labels.goto(-200, 0)
    labels.down()
    labels.forward(400)  # Draw x-axis

    labels.up()
    labels.goto(0, -100)
    labels.down()
    labels.left(90)
    labels.forward(200)  # Draw y-axis

    labels.up()
    labels.goto(-180, 80)
    labels.down()
    labels.color("blue")
    labels.write("Wave 1", align="left", font=("Arial", 12, "normal"))

    labels.up()
    labels.goto(-180, 60)
    labels.down()
    labels.color("red")
    labels.write("Wave 2", align="left", font=("Arial", 12, "normal"))

    labels.up()
    labels.goto(-180, 40)
    labels.down()
    labels.color("green")
    labels.write("Interference", align="left", font=("Arial", 12, "normal"))

# Animation loop
offset = 0
draw_labels()
while True:
    draw_wave(wave1, offset, "blue")
    draw_wave(wave2, -offset, "red")

    # Draw interference pattern
    interference.clear()
    interference.color("green")
    for i in range(400):
        x = i - 200
        y1 = 50 * math.sin((x + offset) / 20.0)
        y2 = 50 * math.sin((x - offset) / 20.0)
        y = y1 + y2
        interference.up()
        interference.goto(x, y)
        interference.down()
        interference.forward(1)

    wn.update()  # Update screen
    offset += 1  # Increment offset for animation
