# This is where all the algorithms for the transformations are impelemented

import math

# Translation
def translate(point, tx, ty):
    x, y = point
    x += tx
    y += ty
    point = (x, y)
    return point

# Scaling
def scale(point, sx, sy, fixed):
    xx, yy = fixed
    xx *= -1
    yy *= -1
    point = translate(point, xx, yy)

    x, y = point
    x *= sx
    y *= sy
    point = (x, y)
    point = translate(point, xx * -1, yy * -1)

    return point

# Rotation
def rotate(point, angle, fixed):
    x, y = point
    xx, yy = fixed
    x -= xx
    y -= yy

    angle = math.radians(angle)

    x_n = x * math.cos(angle) - y * math.sin(angle)
    y_n = x * math.sin(angle) + y * math.cos(angle)

    point = (x_n + xx, y_n + yy)
    return point

# Shearing
def shear(point, shx, shy):
    x, y = point
    x += (shy * y)
    y += (shx * x)
    point = (x, y)
    return point