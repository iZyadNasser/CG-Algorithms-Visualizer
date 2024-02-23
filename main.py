# Importing dependencies
from turtle import *
from PlottedScreen import *
import time
from UImaterials import *
from action import *

# Global Constants
WIDTH = 1500
HEIGHT = 750
PLOT_SCREEN_X = 10
PLOT_SCREEN_Y = HEIGHT / 2 - 10
PLOT_SCREEN_DEFAULT_SERIAL = 20
PLOT_SCREEN_LENGTH = 720
BG_COLOR = (0, 0.2, 0.2)
BUTTON_BG = (0.1, 0.3, 0.1)
BUTTON_PEN = (0.5, 0.5, 0.1)
TEXT_COLOR = "white"
DELAY = 0.3

# Setting up screen and settings
s = Screen()
s.setup(WIDTH, HEIGHT, 100, 10)
s.tracer(0)
s.title("CG Visualizer")
s.bgcolor(BG_COLOR)

# Making instances of the objects
plot = PlottedScreen("black", PLOT_SCREEN_X, PLOT_SCREEN_Y, PLOT_SCREEN_LENGTH, "yellow", PLOT_SCREEN_DEFAULT_SERIAL)
change_serial_button = Button(-100, HEIGHT/2 - 10, 100, 100, "press\nto change\nzoom ratio", BUTTON_BG, BUTTON_PEN, 12, "arial", TEXT_COLOR)
clear_points_button = Button(-100, HEIGHT/2 - 120, 100, 100, "press\nto clear\nall points", BUTTON_BG, BUTTON_PEN, 12, "arial", TEXT_COLOR)
line_dda_button = Button(-WIDTH/2 + 10, HEIGHT/2 - 80, 200, 100, "DDA", (0.5, 0.5, 0.5), BUTTON_PEN, 15, "arial", "white")
line_bresen_button = Button(-WIDTH/2 + 220, HEIGHT/2 - 80, 200, 100, "Bresenham's", (0.5, 0.5, 0.5), BUTTON_PEN, 15, "arial", "white")
circle_bresen_button = Button(-WIDTH/2 + 10, HEIGHT/2 - 300, 200, 100, "Bresenham's", (0.5, 0.5, 0.5), BUTTON_PEN, 15, "arial", "white")
circle_midpoint_button = Button(-WIDTH/2 + 220, HEIGHT/2 - 300, 200, 100, "Mid Point", (0.5, 0.5, 0.5), BUTTON_PEN, 15, "arial", "white")
translate_button = Button(-WIDTH/2 + 10, HEIGHT/2 - 525, 150, 100, "Translation", (0.5, 0.5, 0.5), BUTTON_PEN, 15, "arial", "white")
scale_button = Button(-WIDTH/2 + 170, HEIGHT/2 - 525, 150, 100, "Scaling", (0.5, 0.5, 0.5), BUTTON_PEN, 15, "arial", "white")
rotate_button = Button(-WIDTH/2 + 330, HEIGHT/2 - 525, 150, 100, "Rotation", (0.5, 0.5, 0.5), BUTTON_PEN, 15, "arial", "white")
shear_button = Button(-WIDTH/2 + 490, HEIGHT/2 - 525, 150, 100, "Shearing", (0.5, 0.5, 0.5), BUTTON_PEN, 15, "arial", "white")

# Test


# Drawing static layout
plot.draw_screen()
change_serial_button.draw_button()
clear_points_button.draw_button()
type_text(-WIDTH/2 + 90, HEIGHT/2 - 30, 0, 0, "Line Algorithms", 18, "arial", "white")
line_dda_button.draw_button()
line_bresen_button.draw_button()
type_text(-WIDTH/2 + 100, HEIGHT/2 - 250, 0, 0, "Circle Algorithms", 18, "arial", "white")
circle_bresen_button.draw_button()
circle_midpoint_button.draw_button()
type_text(-WIDTH/2 + 100, HEIGHT/2 - 470, 0, 0, "Transformations", 18, "arial", "white")
translate_button.draw_button()
scale_button.draw_button()
rotate_button.draw_button()
shear_button.draw_button()

# Function for handling the clicks
def click_handler(x, y):
    if check_clicked((x, y), change_serial_button.button_boundries()):
        change_zoom_ratio(plot)
        print(1111)
    elif check_clicked((x, y), clear_points_button.button_boundries()):
        plot.erase_points()
    elif check_clicked((x, y), line_dda_button.button_boundries()):
        handle_algo("dda", plot)
    elif check_clicked((x, y), line_bresen_button.button_boundries()):
        handle_algo("lin-bre", plot)
    elif check_clicked((x, y), circle_bresen_button.button_boundries()):
        handle_algo("cir-bre", plot)
    elif check_clicked((x, y), circle_midpoint_button.button_boundries()):
        handle_algo("cir-mid", plot)
    elif check_clicked((x, y), translate_button.button_boundries()):
        handle_transformation("trans", plot)
    elif check_clicked((x, y), scale_button.button_boundries()):
        handle_transformation("scale", plot)
    elif check_clicked((x, y), rotate_button.button_boundries()):
        handle_transformation("rot", plot)
    elif check_clicked((x, y), shear_button.button_boundries()):
        handle_transformation("sh", plot)


# Event listeners
s.listen()
s.onclick(click_handler, 1)

# Main Loop
while True:
    update()

    # Checking if there are points still to be plotted
    if plot.check_counter():
        plot.draw_points()


    time.sleep(DELAY)