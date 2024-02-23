# Importing dependencies
from turtle import *

# Setting up turtle
t = Turtle()
t.hideturtle()

# Function to draw a line
def draw_line(start_point, end_point, color):
    t.up()
    t.goto(start_point)
    t.pencolor(color)
    t.down()
    t.goto(end_point)

# Function to draw a rectangle
def draw_rectangle(top_left_point, bottom_right_point, color, pen_color):
    x_s, y_s = top_left_point
    x_e, y_e = bottom_right_point

    # Initialize
    t.up()
    t.goto(x_s, y_s)
    t.pencolor(pen_color)
    t.fillcolor(color)
    t.down()
    t.begin_fill()

    # Draw
    t.goto(x_e, y_s)
    t.goto(x_e, y_e)
    t.goto(x_s, y_e)
    t.goto(x_s, y_s)
    t.end_fill()

# Function to draw square
def draw_square(top_left, side_length, color, pen_color):
    x_s, y_s = top_left

    # Calculating the bottom right
    x_e = x_s + side_length
    y_e = y_s - side_length
    bottom_right = (x_e, y_e)

    # Draw using rectangle function
    draw_rectangle(top_left, bottom_right, color, pen_color)