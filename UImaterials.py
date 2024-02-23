# This where the classes of the ui elements are implemented

# Importing dependencies
from shapes import *
from turtle import *

# General functions
# Function to write text in the center of the element
def type_text(x, y, width, height, text, font_size, font_family, type_color):
    # Initialize turtle
    t = Turtle()
    t.hideturtle()
    t.up()
    t.color(type_color)

    # Calculate the position of the anchor
    x += (width / 2)
    y -= (height / 2 + 20)
    t.goto(x, y)
    t.write(text, align="center", font=(font_family, font_size, "normal"))

# Button class
class Button():
    # Class constructor
    def __init__(self, x, y, width, height, text, color, pencolor, font_size, font_family, type_color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.color = color
        self.pencolor = pencolor
        self.font_size = font_size
        self.font_family = font_family
        self.type_color = type_color

    # Method to write text on button
    def write_text(self):
        type_text(self.x, self.y, self.width, self.height, self.text, self.font_size, self.font_family, self.type_color)

    # Method to draw the button on screen
    def draw_button(self):
        # Calculate the bottom right
        x_e = self.x + self.width
        y_e = self.y - self.height
        bottom_right = (x_e, y_e)

        # Draw the button rectangle
        draw_rectangle((self.x, self.y), bottom_right, self.color, self.pencolor)

        # Calling the method that writes the text on the button
        self.write_text()

    # Method to return the boundreis of the button
    def button_boundries(self):
        x_e = self.x + self.width
        y_e = self.y - self.height
        bottom_right = (x_e, y_e)

        return (self.x, self.y), bottom_right