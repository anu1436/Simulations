import turtle

# Initialize turtle
wn = turtle.Screen()
wn.bgcolor("white")
wn.title("Wave Interference Simulation")

wave = turtle.Turtle()
wave.color("blue")
wave.speed(0)

# Draw wave pattern
def draw_wave(x, y):
    wave.penup()
    wave.goto(x, y)
    wave.pendown()
    for _ in range(36):
        wave.circle(50, 10)
        wave.right(170)
    wave.right(10)

# Draw interference pattern
for x in range(-200, 200, 50):
    for y in range(-200, 200, 50):
        draw_wave(x, y)

turtle.done()
