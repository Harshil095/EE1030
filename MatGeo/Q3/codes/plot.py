import numpy as np
import matplotlib.pyplot as plt

# Define side lengths
def calculate_sides():
    # Simplify the expression for side lengths
    denominator = np.sqrt(6) + 2 * np.sqrt(2) + 2 * np.sqrt(3)
    factor = 48 / denominator

    ab = factor * (np.sqrt(6) + np.sqrt(2)) / 4
    bc = factor * (np.sqrt(3)) / 2
    ca = factor * (1 / np.sqrt(2))
    
    return ab, bc, ca

# Function to compute the vertices of the triangle
def compute_vertices(ab, bc, ca):
    # Place B at the origin
    B = np.array([0, 0])
    
    # Place C at (bc, 0)
    C = np.array([bc, 0])
    
    # Use law of cosines to find the coordinates of A
    angle_A_rad = np.arccos((ab**2 + ca**2 - bc**2) / (2 * ab * ca))
    x = (ca**2 - ab**2 - bc**2) / (-2 * bc)
    y = np.sqrt(ca**2 - x**2)
    
    A = np.array([x, y])
    
    return A, B, C

# Function to plot the triangle
def plot_triangle(vertices):
    A, B, C = vertices
    triangle = np.array([A, B, C, A])  # Close the triangle

    plt.figure(figsize=(8, 8))
    plt.plot(triangle[:, 0], triangle[:, 1], 'b-o')
    plt.fill(triangle[:, 0], triangle[:, 1], 'lightblue', alpha=0.5)
    plt.text(A[0], A[1], 'A', fontsize=12, ha='right')
    plt.text(B[0], B[1], 'B', fontsize=12, ha='right')
    plt.text(C[0], C[1], 'C', fontsize=12, ha='right')
    
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.axhline(0, color='black',linewidth=0.5)
    plt.axvline(0, color='black',linewidth=0.5)
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.gca().set_aspect('equal', adjustable='box')
    plt.title('Triangle ABC')
    plt.show()

# Calculate side lengths
ab, bc, ca = calculate_sides()

# Compute the vertices of the triangle
vertices = compute_vertices(ab, bc, ca)

# Plot the triangle
plot_triangle(vertices)

