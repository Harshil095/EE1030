#Program to plot  the tangent of a parabola
#Code by GVV Sharma
#Released under GNU GPL
#August 10, 2020
#Revised July 31, 2024
import numpy as np
import matplotlib.pyplot as plt
from numpy import linalg as LA

import sys
sys.path.insert(0, '/home/harshil-rathan/Desktop/matgeo/codes/CoordGeo')
#local imports
from line.funcs import *
from triangle.funcs import *
from conics.funcs import *

#if using termux
import subprocess
import shlex
#end if

# Main plotting code
fig = plt.figure()
ax = fig.add_subplot(111, aspect='equal')
len = 100
y = np.linspace(-8, 8, len)

# Conic parameters
V = np.array(([0, 0], [0, 1]))
u = -1/2*e1  # Assuming e1 is [1, 0]
f = 0

n, c, F, O, lam, P, e = conic_param(V, u, f)

# Eigenvalues and eigenvectors
flen = parab_param(lam, P, u)

# Standard parabola generation
x = parab_gen(y, flen)

# Directrix
k1 = -10
k2 = 10

# Latus rectum
cl = (n.T @ F).flatten()


xStandard = np.block([[x], [y]])

# Affine conic generation
Of = O.flatten()
xActual = P @ xStandard + Of[:, np.newaxis]

# Plotting
plt.plot(xActual[0, :], xActual[1, :], label='Parabola', color='r')


# Add vertical lines at x = 1 and x = 4
x_line1 = 1
x_line2 = 4
plt.axvline(x=x_line1, color='blue', linestyle='--', label='$x = 1$')
plt.axvline(x=x_line2, color='cyan', linestyle='--', label='$x = 4$')

# Shade the region between the parabola and x-axis
x_fill = np.linspace(x_line1, x_line2, 100)
y_fill = np.sqrt(x_fill)  # Upper boundary (y = sqrt(x))
y1_fill= -np.sqrt(x_fill)

# Fill the region above the x-axis (under the parabola)
plt.fill_between(x_fill, y_fill, 0, color='blue', alpha=0.5, )

plt.fill_between(x_fill,y1_fill,0, color='blue', alpha=0.5, )

# Labeling the coordinates
tri_coords = np.block([O, F])
plt.scatter(tri_coords[0, :], tri_coords[1, :], c='black')
vert_labels = ['O', 'F']
for i, txt in enumerate(vert_labels):
    plt.annotate(f'{txt}\n({tri_coords[0, i]:.0f}, {tri_coords[1, i]:.0f})',
                 (tri_coords[0, i], tri_coords[1, i]),  # point to label
                 textcoords="offset points",  # position text
                 xytext=(-20, 5),  # offset
                 ha='center')  # horizontal alignment

# Adjusting the plot
ax = plt.gca()
ax.spines['top'].set_color('none')
ax.spines['left'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['bottom'].set_position('zero')

plt.legend(loc='best')
plt.grid()  # minor
plt.axis('equal')
plt.xlim(-1, 5)
plt.ylim(-1, 4)
plt.xlabel('$x$')
plt.ylabel('$y$')

# Show the plot
plt.show()

