import numpy as np
import matplotlib.pyplot as plt

 

# Create theta values for the full circle
theta = np.linspace(0, 2 * np.pi, 100)

# Parametric equations for the circle
x_values_circle = 2 * np.cos(theta)
y_values_circle = 2 * np.sin(theta)

# Create the line inclined at 30 degrees (pi/6) passing through the origin
# y = (tan(30 degrees)) * x = (1/sqrt(3)) * x
x_line_inclined = np.linspace(0, 2, 100)  # x values from 0 to 'a'
y_line_inclined = (1 / np.sqrt(3)) * x_line_inclined  # y = (1/sqrt(3)) * x

# Determine the intersection point of the line and the circle in the first quadrant
# Equation of the circle: x^2 + y^2 = a^2
# Equation of the line: y = (1/sqrt(3)) * x
# Substitute y = (1/sqrt(3)) * x into the circle equation:
# x^2 + (1/sqrt(3))^2 * x^2 = a^2
# x^2 (1 + 1/3) = a^2
# x^2 * 4/3 = a^2
# x^2 = 3a^2 / 4
# x = a * sqrt(3) / 2
x_intersection = 2 * np.sqrt(3) / 2
y_intersection = (1 / np.sqrt(3)) * x_intersection

# Create x values for shading from 0 to the intersection point
x_shade = np.linspace(0, x_intersection, 100)
y_shade_line = (1 / np.sqrt(3)) * x_shade  # y values for the line
y_shade_circle = np.sqrt(2**2 - x_shade**2)  # y values for the circle

# Create the plot
plt.figure(figsize=(10, 10))

# Plot the circle
plt.plot(x_values_circle, y_values_circle, label='$x^2 + y^2 = a^2$', color='blue')

# Plot the inclined line y = (1/sqrt(3)) * x
plt.plot(x_line_inclined, y_line_inclined, label='$y = \\frac{1}{\\sqrt{3}}x$', color='green', linestyle='--')

# Shade the region enclosed between the line, circle, and positive x-axis
plt.fill_between(x_shade, y_shade_line, y_shade_circle, color='lightgreen', alpha=0.5, label='Enclosed Shaded Region')

# Add x-axis and y-axis
plt.axhline(0, color='black', linewidth=1.2)  # X-axis
plt.axvline(0, color='black', linewidth=1.2)  # Y-axis

# Set the limits of the plot
plt.xlim(-2 - 1, 2 + 1)
plt.ylim(-2 - 1, 2 + 1)

# Add labels and title
plt.title('Region Enclosed between Circle, Line, and Positive X-axis')
plt.xlabel('X-axis (x)')
plt.ylabel('Y-axis (y)')
plt.grid()
plt.axis('equal')  # Set equal scaling for x and y axes

# Move the legend to the top-left corner
plt.legend(loc='upper left')

# Show the plot
plt.show()

