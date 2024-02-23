# This is where important actions are done

# Importing dependencies
from PlottedScreen import *
from UImaterials import *
from turtle import *
from drawingAlgorithms import *
from transformations import *

# Function to check what button was clicked
def check_clicked(point, button_boundries):
    # Extracting values
    p, c = button_boundries
    x_s, y_s = p
    x_e, y_e = c
    x, y = point

    # Checking collision
    if (x_s <= x <= x_e) and ((y_s >= y >= y_e)):
        return True
    
    return False

# Function to execute the change zoom ratio command
def change_zoom_ratio(plot):
    # Getting input
    absolute_length = int(textinput("Zoom ratio", "How many points do you want in each direction?"))

    # Updating the plot
    buffer = [i for i in plot.ploted_points]
    plot.erase_points()
    plot.change_serial(absolute_length)
    plot.draw_screen()
    for i, j in buffer:
        plot.add_point(i, j)
        plot.draw_points()

# Function to handle all algorithms calls
def handle_algo(algo, plot):
    # Checking the algorithm needed
    if algo == "dda":
        # Getting the points as input
        x_s = int(textinput("Point input", "Enter the x coordinate for the start point:"))
        y_s = int(textinput("Point input", "Enter the y coordinate for the start point:"))
        x_e = int(textinput("Point input", "Enter the x coordinate for the end point:"))
        y_e = int(textinput("Point input", "Enter the y coordinate for the end point:"))

        # Getting the points
        points = [i for i in dda(x_s, y_s, x_e, y_e)]

        # Adding the points to the plot
        for i, j in points:
            plot.add_point(i, j)
    elif algo == "lin-bre":
        # Getting the points as input
        x_s = int(textinput("Point input", "Enter the x coordinate for the start point:"))
        y_s = int(textinput("Point input", "Enter the y coordinate for the start point:"))
        x_e = int(textinput("Point input", "Enter the x coordinate for the end point:"))
        y_e = int(textinput("Point input", "Enter the y coordinate for the end point:"))

        # Getting the points
        points = [i for i in lin_bre(x_s, y_s, x_e, y_e)]

        # Adding the points to the plot
        for i, j in points:
            plot.add_point(i, j)
    elif algo == "cir-bre":
        # Getting the center and radius as input
        x_c = int(textinput("Point input", "Enter the x coordinate for the center point:"))
        y_c = int(textinput("Point input", "Enter the y coordinate for the center point:"))
        r = int(textinput("Point input", "Enter the radius:"))

        # Getting the points
        points = [i for i in cir_bre(x_c, y_c, r)]

        # Adding the points to the plot
        for i, j in points:
            plot.add_point(i, j)
    else:
        # Getting the center and radius as input
        x_c = int(textinput("Point input", "Enter the x coordinate for the center point:"))
        y_c = int(textinput("Point input", "Enter the y coordinate for the center point:"))
        r = int(textinput("Point input", "Enter the radius:"))

        # Getting the points
        points = [i for i in cir_mid(x_c, y_c, r)]

        # Adding the points to the plot
        for i, j in points:
            plot.add_point(i, j)

def handle_transformation(type, plot):
    points = []
    if type == "trans":
        tx = int(textinput("Translate", "What is the value of tx?"))
        ty = int(textinput("Translate", "What is the value of ty?"))
        for i in plot.ploted_points:
            points.append(translate(i, tx, ty))
    elif type == "scale":
        sx = int(textinput("Scale", "What is the value of sx?"))
        sy = int(textinput("Scale", "What is the value of sy?"))
        fixed = (float(textinput("scale around what point?", "x: ")), int(textinput("scale around what point?", "y: ")))
        for i in plot.ploted_points:
            points.append(scale(i, sx, sy, fixed))
    elif type == "rot":
        angle = int(textinput("Rotate", "What is the value of the angle?"))
        fixed = (int(textinput("rotate around what point?", "x: ")), int(textinput("rotate around what point?", "y: ")))
        for i in plot.ploted_points:
            points.append(rotate(i, angle, fixed))
    else:
        shx = float(textinput("Shear", "What is the value of shx?"))
        shy = float(textinput("Shear", "What is the value of shy?"))
        for i in plot.ploted_points:
            points.append(shear(i, shx, shy))

    plot.erase_points()

    for i, j in points:
        plot.add_point(i, j)
        plot.draw_points()