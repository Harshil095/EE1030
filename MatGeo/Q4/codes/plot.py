import sys                                          # for path to external scripts
sys.path.insert(0, '/home/harshil-rathan/Desktop/matgeo/codes/CoordGeo')  # path to my scripts
import numpy as np
import numpy.linalg as LA
import matplotlib.pyplot as plt

# Read values from values.tex using np.loadtxt
data = np.loadtxt('values.tex')

# Assign side lengths
AB = data[0]  # Length from A to B
BC = data[1]  # Length from B to C
AC = data[2]  # Length from A to C

# Assume point B is at origin (0, 0)
B = np.array([0, 0])

# C is at (BC, 0)
C = np.array([BC, 0])

# Calculate coordinates of A using the law of cosines
cos_angle = (AB**2 + BC**2 - AC**2) / (2 * AB * BC)
angle_B = np.arccos(cos_angle)

# Calculate A's coordinates
A_x = AB * np.cos(angle_B)
A_y = AB * np.sin(angle_B)

# Final coordinates for A
A = np.array([A_x, A_y])

# Plotting
plt.figure()

# Generating all lines
x_AB = np.linspace(A[0], B[0], 100), np.linspace(A[1], B[1], 100)
x_BC = np.linspace(B[0], C[0], 100), np.linspace(B[1], C[1], 100)
x_CA = np.linspace(C[0], A[0], 100), np.linspace(C[1], A[1], 100)

# Plot the lines
plt.plot(x_AB[0], x_AB[1], label='$AB$')
plt.plot(x_BC[0], x_BC[1], label='$BC$')
plt.plot(x_CA[0], x_CA[1], label='$CA$')

# Label the coordinates
plt.scatter([A[0], B[0], C[0]], [A[1], B[1], C[1]], color='red')
plt.text(A[0], A[1], 'A', fontsize=12, ha='right')
plt.text(B[0], B[1], 'B', fontsize=12, ha='right')
plt.text(C[0], C[1], 'C', fontsize=12, ha='right')

# Labels and grid
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.grid(True)
plt.axis('equal')

# Display lengths in the legend
plt.legend([
    f'Side AB = {AB:.2f} cm',
    f'Side BC = {BC:.2f} cm',
    f'Side AC = {AC:.2f} cm'
], loc='upper right')

plt.show()

