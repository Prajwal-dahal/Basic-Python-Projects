import math
from turtle import *
import random

# Heart shape functions
def hearta(k):
    return 15 * math.sin(k) ** 3

def heartb(k):
    return 12 * math.cos(k) - 5 * math.cos(2 * k) - 2 * math.cos(3 * k) - math.cos(4 * k)

# Function to draw a star at the current position
def draw_star(x, y, size):
    penup()
    goto(x, y)
    pendown()
    color("yellow")  # Color for stars
    begin_fill()
    for _ in range(5):
        forward(size)
        right(144)
    end_fill()

# Setup the canvas
speed(0)  # Maximum speed
bgcolor("black")  # Set background color
hideturtle()  # Hide the turtle cursor
penup()

# Draw the heart outline
color("#FF6347")  # Tomato red
for i in range(600):
    x = hearta(i / 100) * 20
    y = heartb(i / 100) * 20
    penup()
    goto(x, y)
    pendown()
    dot(2)  # Use a dot to create the outline smoothly

# Draw stars inside the heart
num_stars = 50  # Number of stars inside the heart
for _ in range(num_stars):
    while True:
        # Generate random points
        x = random.uniform(-15, 15)
        y = random.uniform(-12, 10)
        # Check if the point is inside the heart
        if y < heartb(x):  # Check y against the heart curve
            draw_star(x * 20, y * 20, random.randint(10, 20))  # Random star size
            break

done()
