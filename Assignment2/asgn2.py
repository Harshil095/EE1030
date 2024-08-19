import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

# Define the vertices of the parallelogram
A = np.array([3, -1, 2])
B = np.array([1, -2, 4])
C = np.array([-1, 1, 2])
D = np.array([1, 2, 0])

# Stack vertices in a matrix
vertices = np.array([A, B, C, D, A])

# Plotting
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot the parallelogram using the vertices matrix
ax.add_collection3d(Poly3DCollection([vertices[:4]], facecolors='cyan', linewidths=1, edgecolors='r', alpha=.25))

# Plot the vertices
ax.scatter(vertices[:, 0], vertices[:, 1], vertices[:, 2], color='black')

# Annotate the vertices
for i, txt in enumerate(['A', 'B', 'C', 'D']):
    ax.text(vertices[i, 0], vertices[i, 1], vertices[i, 2], txt, size=20, zorder=1, color='k')

# Set plot limits
ax.set_xlim([min(vertices[:, 0])-1, max(vertices[:, 0])+1])
ax.set_ylim([min(vertices[:, 1])-1, max(vertices[:, 1])+1])
ax.set_zlim([min(vertices[:, 2])-1, max(vertices[:, 2])+1])

# Set labels
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

plt.show()

