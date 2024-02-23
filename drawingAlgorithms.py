# This is where all the drawing algorithms are written

# DDA Line Drawing Algorithm
def dda(x_s, y_s, x_e, y_e):
    points = []
    dx = abs(x_e - x_s)
    dy = abs(y_e - y_s)

    if dx == 0:
        for i in range(min(y_s, y_e), max(y_s, y_e) + 1):
            point = (x_s, i)
            points.append(point)
        return points
        
    slope = dy / dx

    if dx > dy:
        steps = dx
        if x_e > x_s:
            x_inc = 1
        elif x_s > x_e:
            x_inc = -1
        else:
            x_inc = 0

        if y_e > y_s:
            y_inc = slope
        elif y_s > y_e:
            y_inc = -slope
        else:
            y_inc = 0
    else:
        steps = dy
        slope = 1 / slope

        if x_e > x_s:
            x_inc = slope
        elif x_s > x_e:
            x_inc = -slope
        else:
            x_inc = 0

        if y_e > y_s:
            y_inc = 1
        elif y_s > y_e:
            y_inc = -1
        else:
            y_inc = 0

    x = x_s
    y = y_s

    for _ in range(steps + 1):
        points.append((round(x), round(y)))
        x += x_inc
        y += y_inc

    return points

# Bresenham's Line Drawing Algorithm
def lin_bre(x_s, y_s, x_e, y_e):
    # Normalize line
    mode = "r"
    if x_e < x_s:
        x_s, x_e = x_e, x_s
        y_s, y_e = y_e, y_s

    if y_e < y_s:
        mode = "i"
        shift = (2 * (y_s - y_e))
        y_e += shift

    # Start Algorithm
    points = [(x_s, y_s)]

    dx = x_e - x_s
    dy = y_e - y_s

    x = x_s
    y = y_s

    pk = 2 * dy - dx

    while x < x_e:
        x += 1
        if pk >= 0:
            y += 1
            pk = pk + 2 * dy - 2 * dx
        else:
            pk = pk + 2 * dy

        if mode == "i":
            shift = y - y_s
            shift *= 2
            yy = y - shift
        else:
            yy = y

        point = (x, yy)
        points.append(point)

    return points

# Helper function for circle drawing
def get_all_pixels(x_c, y_c, x, y):
    return [(x_c + x, y_c + y), (x_c - x, y_c + y), (x_c + x, y_c - y), (x_c - x, y_c - y),
              (x_c + y, y_c + x), (x_c - y, y_c + x), (x_c + y, y_c - x), (x_c - y, y_c - x)]

# Bresenham's Circle Drawing Algorithm
def cir_bre(x_c, y_c, r):
    x = 0
    y = r
    d = 3 - 2 * r

    points = get_all_pixels(x_c, y_c, x, y)

    while y >= x:
        x += 1

        if d > 0:
            y -= 1
            d = d + 4 * (x - y) + 10
        else:
            d = d + 4 * x + 6

        points += get_all_pixels(x_c, y_c, x, y)

    return points

# Mid-point Circle Drawing Algorithm
def cir_mid(x_c, y_c, r):
    x = r
    y = 0
    d = 1 - r

    points = get_all_pixels(x_c, y_c, x, y)

    while x > y:
        y += 1

        if d > 0:
            x -= 1
            d = d + 2 * y - 2 * x + 1
        else:
            d = d + 2 * y + 1

        points += get_all_pixels(x_c, y_c, x, y)

    return points