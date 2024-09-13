import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

# Function definitions

def create_mat(m, n):
    return np.zeros((m, n))

def mat_add(a, b):
    return np.add(a, b)

def mat_scale(a, k):
    return np.multiply(a, k)

def mat_sub(a, b):
    return np.subtract(a, b)

def matmul(a, b):
    return np.matmul(a, b)

def rot_mat(theta):
    return np.array([[np.cos(theta), -np.sin(theta)], [np.sin(theta), np.cos(theta)]])

def norm_vec(a):
    # Assuming a is a 2D vector for rotation
    return matmul(rot_mat(np.pi / 2), a)

def matsec(a, b, k):
    temp = mat_add(a, mat_scale(b, k))
    return mat_scale(temp, 1 / (k + 1))

# Given vertices
A = np.array([3, -1, 2])
B = np.array([1, -2, 4])
C = np.array([-1, 1, 2])
D = np.array([1, 2, 0])  # Provided directly

# Define the vertices of the parallelogram
vertices = np.array([A, B, C, D, A])

# Define the edges of the parallelogram
edges = [
    [A, B],
    [B, C],
    [C, D],
    [D, A],
]

# Plotting the parallelogram
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plotting the vertices
ax.scatter(vertices[:, 0], vertices[:, 1], vertices[:, 2], color='r')

# Plotting the edges
for edge in edges:
    ax.plot([edge[0][0], edge[1][0]], 
            [edge[0][1], edge[1][1]], 
            [edge[0][2], edge[1][2]], 'b-')

# Adding labels to the vertices
for i, vertex in enumerate([A, B, C, D]):
    ax.text(vertex[0], vertex[1], vertex[2], f'{chr(65+i)}', color='black')

# Set the labels for axes
ax.set_xlabel('X axis')
ax.set_ylabel('Y axis')
ax.set_zlabel('Z axis')

# Set the title
ax.set_title('Parallelogram ABCD')
plt.grid()
plt.savefig("Figure_1.png")
plt.show()

