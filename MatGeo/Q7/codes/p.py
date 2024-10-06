# Program to plot and shade the region between a circle and a line y = sqrt(3) * x
# Code by GVV Sharma
# Released under GNU GPL
# August 21, 2024

import numpy as np
import matplotlib.pyplot as plt
from numpy import linalg as LA

import sys  # for path to external scripts
sys.path.insert(0, '/home/harshil-rathan/Desktop/matgeo/codes/CoordGeo')  # path to your scripts

# Local imports
from line.funcs import *
from triangle.funcs import *
from conics.funcs import *

# Setting up the plot
fig = plt.figure()
ax = fig.add_subplot(111, aspect='equal')
num = 100

# Circle parameters
u = np.array(([0, 0])).reshape(-1, 1)  # Center of the circle
f = -4                                 # Circle equation: x^2 + y^2 = 4
O, r = circ_param(u, f)                 # Extract center and radius
x_circ = circ_gen_num(O, r, num)        # Generate circle points

# Generate points for the line y = sqrt(3) * x
x_line = np.linspace(0, 2, num)         # x values for the line from 0 to 2 (first quadrant)
y_line = np.sqrt(3) * x_line            # y values calculated as y = sqrt(3) * x

# Intersection point between line and circle in the first quadrant
x_intersection = 1
y_intersection = np.sqrt(3)

# Define the region for shading: x values from 0 to intersection point
x_shade = np.linspace(0, x_intersection, num)
y_shade_line = np.sqrt(3) * x_shade       # y values for the line y = sqrt(3) * x
y_shade_circle = np.sqrt(4 - x_shade**2)  # y values for the circle y = sqrt(4 - x^2)

# Plot the circle
plt.plot(x_circ[0, :], x_circ[1, :], label='Circle: $x^2 + y^2 = 4$', color='blue')

# Plot the line y = sqrt(3) * x
plt.plot(x_line, y_line, label='$y = \\sqrt{3}x$', linestyle='--', color='green')

# Shade the region between the line, circle, and x-axis in the first quadrant
plt.fill_between(x_shade, y_shade_line, y_shade_circle, color='lightgreen', alpha=0.5, label='Shaded Region')

# Circle center and point labels
plt.scatter(u[0], u[1], color='red')
plt.text(u[0] + 0.1, u[1] + 0.1, 'Center (0, 0)', fontsize=12, color='red')

# Mark the intersection point
plt.scatter(x_intersection, y_intersection, color='purple')
plt.text(x_intersection + 0.1, y_intersection + 0.1, f'({x_intersection}, {y_intersection:.2f})', fontsize=12, color='purple')

# Setting up the plot limits
plt.xlim(-0.5, 2.5)
plt.ylim(-0.5, 2.5)

# Customizing the axes and labels
ax.spines['top'].set_color('none')
ax.spines['left'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['bottom'].set_position('zero')

# Add labels and legend
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.title('Region Enclosed by Circle, Line $y = \\sqrt{3}x$, and X-axis')
plt.legend(loc='best')
plt.grid()
plt.axis('equal')

# Show the plot
plt.show()

