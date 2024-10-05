#include <stdio.h>
#include <math.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <sys/socket.h>
#include <netinet/in.h>

#include "libs/matfun.h"
#include "libs/geofun.h"


// Function to represent the semicircle y = sqrt(4 - x^2)
double semicircle(double x) {
    return sqrt(4 - x * x);
}

// Function to represent the line y = sqrt(3) * x
double line(double x) {
    return sqrt(3) * x;
}

// Function to compute the area using trapezoidal rule
double compute_area(double a, double b, int n) {
    double h = (b - a) / n; // Step size
    double sum = 0.0;

    for (int i = 1; i < n; i++) {
        double x = a + i * h;
        sum += (semicircle(x) - line(x));
    }
    
    // Add the first and last terms
    sum += (semicircle(a) - line(a)) / 2.0;
    sum += (semicircle(b) - line(b)) / 2.0;

    return h * sum;
}

int main() {
    double a = 0.0;   // Lower limit
    double b = 1.0;   // Upper limit
    int n = 10000;    // Number of intervals for trapezoidal rule

    double area = compute_area(a, b, n);

    //write the result to a .tex file 
    FILE *file = fopen("values.tex","w");
    if(file==NULL){
	    printf("Error opening file!\n");
	    return 1;
    }

   
     fprintf(file, "A = %.4f\n",area);

     fclose(file);

   
    printf("Result written to values.tex\n");

    return 0;
}

