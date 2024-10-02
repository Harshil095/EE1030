#include <stdio.h>
#include <math.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <sys/socket.h>
#include <netinet/in.h>

#include "libs/matfun.h"
#include "libs/geofun.h"

// Function to compute the value of y given x
double f(double x) {
    return sqrt(x); // Since y^2 = x, y = sqrt(x)
}

// Trapezoidal rule for numerical integration
double trapezoidal_rule(double a, double b, int n) {
    double h = (b - a) / n; // Width of each small rectangle
    double area = 0.0;
    
    // Calculate area
    for (int i = 0; i < n; i++) {
        double x1 = a + i * h;        // Left endpoint
        double x2 = a + (i + 1) * h;  // Right endpoint
        area += (f(x1) + f(x2)) * h / 2; // Area of trapezoid
    }
    
    return area;
}

int main() {
    double a = 1.0; // Lower bound
    double b = 4.0; // Upper bound
    int n = 1000;   // Number of subintervals

    double area = trapezoidal_rule(a, b, n);

    // Write the result to a .tex file
    FILE *file = fopen("values.tex", "w");
    if (file == NULL) {
        printf("Error opening file!\n");
        return 1;
    }

   
    fprintf(file, "The area of the region bounded by the curve $y^2 = x$, the lines $x = 1$ and $x = 4$, and the axis in the first quadrant is: A \n");

  
    fprintf(file, "A = %.4f\n", area);
  

    fclose(file);

    printf("Area calculated: %.4f\n", area);
    printf("Result written to area.tex\n");

    return 0;
}

