# Importing dependencies
from shapes import *

# Class for the ploted screen
class PlottedScreen():
    # A list of all plotted points
    ploted_points = []

    # Attributes
    layout_color = (0.4, 0.4, 0.4)
    main_axies_color = (1, 1, 1)
    margin = 4
    counter = 0

    # Class constructor
    def __init__(self, background_color, x, y, length, draw_color, absolute_serial):
        self.bg = background_color
        self.x = x
        self.y = y
        self.color = draw_color
        self.serial = absolute_serial * 2
        self.length = length

    # Method to calculate the side length of individual point
    def calculate_cell_length(self):
        return (self.length / self.serial)

    # Method to convert from plot screen pixels to general pixels
    def convert_plot_to_pixel(self, point):
        # Extracting the coordinates
        x, y = point

        # Calculating the pixel
        pixel_x = x + self.x + self.length / 2 + 2
        pixel_y = y + 3# - (self.window_height / 2 - self.length / 2)

        # Returning pixel point
        pixel = (pixel_x, pixel_y)
        return pixel

    # Method to draw the plot screen
    def draw_screen(self):
        # Drawing the window
        draw_square((self.x, self.y), self.length, self.bg, self.bg)

        # Calculating the cell length
        cell_length = self.calculate_cell_length()

        # Drawing the vertical coordinate lines
        x = self.x
        cnt = 0
        while x <= (self.x + self.length):
            cnt += 1
            # Checking if it's main axies
            if cnt == (self.serial / 2) + 1:
                draw_line((x, self.y), (x, self.y - self.length), self.main_axies_color)
            else:
                draw_line((x, self.y), (x, self.y - self.length), self.layout_color)
            x += cell_length

        # Drawing the horizontal coordinate lines
        y = self.y
        cnt = 0
        while y >= (self.y - self.length):
            cnt += 1
            # Checking if it's main axies
            if cnt == (self.serial / 2) + 1:
                draw_line((self.x, y), (self.x + self.length, y), self.main_axies_color)
            else:
                draw_line((self.x, y), (self.x + self.length, y), self.layout_color)
            y -= cell_length

    # Method that adds a new point to the ploted points list
    def add_point(self, x, y):
        point = (x, y)
        self.ploted_points.append(point)

    # Method to draw a single point
    def draw_point(self, x, y):
        # Checking if point if in bounds
        if not self.in_bound(x, y):
            return

        # Calculating cell length
        cell_length = self.calculate_cell_length()

        # Calculating the relative pixels of the points on plot screen
        x = x * cell_length
        y = (y + 1) * cell_length

        # Converting to general window pixels
        x, y = self.convert_plot_to_pixel((x, y))

        # Drawing the pixel
        draw_square((x, y), cell_length - self.margin, self.color, self.color)
    
    # Method to draw ploted points on screen
    def draw_points(self):
        self.draw_point(self.ploted_points[self.counter][0], self.ploted_points[self.counter][1])
        self.counter += 1

    # Method to check if the counter is done
    def check_counter(self):
        return (self.counter < len(self.ploted_points))

    # Method to change the serialing of the plot screen
    def change_serial(self, new_serial):
        self.serial = new_serial * 2
        self.refresh_plot()

    # Method to clear the ploted points
    def clear_points(self):
        self.ploted_points.clear()

    # Method to erase a single point from screen
    def erase_point(self, x, y):
        # Check if point is drawn
        if not self.in_bound(x, y):
            return
        
        # Calculating cell length
        cell_length = self.calculate_cell_length()

        # Calculating the relative pixels of the points on plot screen
        x = x * cell_length
        y = (y + 1) * cell_length

        # Converting to general window pixels
        x, y = self.convert_plot_to_pixel((x, y))

        # Drawing the pixel
        draw_square((x, y), cell_length - self.margin, self.bg, self.bg)

    # Method to erase drawed points
    def erase_points(self):
        self.draw_screen()

        self.clear_points()
        self.counter = 0

    # Method to refresh points
    def refresh_plot(self):
        buffer = [i for i in self.ploted_points]
        self.erase_points()
        for i in buffer:
            self.add_point(i)

    # Method to check if a point is in bounds
    def in_bound(self, x, y):
        s = self.serial // 2
        if x < s * -1:
            return False
        if x >= s:
            return False
        if y < s * -1:
            return False
        if y > s:
            return False
        
        return True