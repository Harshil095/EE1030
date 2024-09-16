import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Define the vectors
a = np.array([1, 1, 1])
b = np.array([2, 4, -5])
lambda_val = 1
c = np.array([lambda_val, 2, 3])

# Compute b + c
b_plus_c = b + c

# Compute the unit vector along b + c
magnitude_b_plus_c = np.linalg.norm(b_plus_c)
unit_vector = b_plus_c / magnitude_b_plus_c

# Plotting
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot vectors a, b, c, and b + c
ax.quiver(0, 0, 0, a[0], a[1], a[2], color='r', label='a (1, 1, 1)')
ax.quiver(0, 0, 0, b[0], b[1], b[2], color='g', label='b (2, 4, -5)')
ax.quiver(0, 0, 0, c[0], c[1], c[2], color='b', label='c (1, 2, 3)')
ax.quiver(0, 0, 0, b_plus_c[0], b_plus_c[1], b_plus_c[2], color='m', label='b + c')

# Plot the unit vector in the direction of b + c
ax.quiver(0, 0, 0, unit_vector[0], unit_vector[1], unit_vector[2], color='k', linestyle='--', label='Unit vector of (b + c)')

# Set labels
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('Vectors a, b, c, and b + c')

# Set limits
ax.set_xlim([-10, 10])
ax.set_ylim([-10, 10])
ax.set_zlim([-10, 10])

# Add a legend
ax.legend()

# Show plot
plt.show()

