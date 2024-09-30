import numpy as np
import matplotlib.pyplot as plt

# Load limits from values.tex using np.loadtxt
limits = np.loadtxt('values.tex')
lower_limit, upper_limit = limits[0], limits[1]

# Define the line equation
def line_eq(x):
    return (3/2) * x + 6

# Set up the x values and the corresponding y values
x_values = np.linspace(lower_limit, upper_limit, 100)
y_values = line_eq(x_values)

# Create the plot
plt.figure(figsize=(10, 6))
plt.plot(x_values, y_values, label='Line: $2y = 3x + 12$', color='blue')

# Shade the area under the curve
plt.fill_between(x_values, y_values, color='lightblue', alpha=0.5, where=(y_values >= 0))

# Add x-axis and y-axis
plt.axhline(0, color='black', linewidth=1.2)  # X-axis
plt.axvline(0, color='black', linewidth=1.2)  # Y-axis

# Add vertical lines for the limits
plt.axvline(lower_limit, color='red', linestyle='--', label=f'x={lower_limit}')
plt.axvline(upper_limit, color='red', linestyle='--', label=f'x={upper_limit}')

# Calculate intersection points
x_intercept = -12 / 3 * 2  # Where line crosses the x-axis (y=0)
y_intercept = 6            # Where line crosses the y-axis (x=0)

# Mark intersection points
plt.plot(x_intercept, 0, 'ro')  # Point on x-axis
plt.plot(0, y_intercept, 'ro')   # Point on y-axis
plt.text(x_intercept, 0, f'  ({x_intercept:.2f}, 0)', verticalalignment='bottom', horizontalalignment='right', color='red')
plt.text(0, y_intercept, f'  (0, {y_intercept})', verticalalignment='bottom', horizontalalignment='right', color='red')

# Add labels and title
plt.title('Area Bounded by the Line, X-axis, and Vertical Lines')
plt.xlabel('X-axis (x)')
plt.ylabel('Y-axis (y)')
plt.xlim(lower_limit - 1, upper_limit + 1)
plt.ylim(0, 20)
plt.grid()
plt.legend()

# Show the plot
plt.show()

