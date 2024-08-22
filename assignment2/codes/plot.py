import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Given vertices
A = np.array([3, -1, 2])
B = np.array([1, -2, 4])
C = np.array([-1, 1, 2])

# Calculate the fourth vertex D
# Midpoint of diagonal AC
mid_AC = (A + C) / 2

# Midpoint of diagonal BD should be equal to mid_AC
# Let D = [x, y, z]
# Midpoint of BD = (B + D) / 2 = mid_AC
# Thus, D = 2 * mid_AC - B
D = 2 * mid_AC - B

# Print the coordinates of D
print("Coordinates of the fourth vertex D:", D)

# Plotting the parallelogram
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plotting vertices
vertices = np.array([A, B, C, D, A])
ax.plot(vertices[:, 0], vertices[:, 1], vertices[:, 2], 'o-', label='Parallelogram ABCD')

# Annotate the vertices
for i, txt in enumerate(['A', 'B', 'C', 'D']):
    ax.text(vertices[i, 0], vertices[i, 1], vertices[i, 2], txt, color='red')

# Set labels and title
ax.set_xlabel('X axis')
ax.set_ylabel('Y axis')
ax.set_zlabel('Z axis')
ax.set_title('Parallelogram ABCD')

plt.legend()
plt.grid(True)
plt.savefig("Figure_1.png")
