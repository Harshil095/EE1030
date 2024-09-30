#include <stdio.h>
#include <math.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <sys/socket.h>
#include <netinet/in.h>

#include "libs/matfun.h"
#include "libs/geofun.h"

double f(double x) {
    return (3.0 / 2.0) * x + 6;  
}

double integrate(double (*func)(double), double a, double b, int n) {
    double delta_x = (b - a) / n;
    double area = 0.0;

    for (int i = 0; i < n; i++) {
        double x_i = a + i * delta_x;
        area += func(x_i) * delta_x;  // Rectangle method (Riemann sum)
    }

    return area;
}

int main() {
	double a = 2.0;
	scanf("%lf",&a);
	double b = 8.0;
	scanf("%lf",&b);
	int n = 1000;

	double area = integrate(f,a,b,n);

        FILE *file = fopen("values.tex", "w");

    // Check if the file was opened successfully
    if (file == NULL) {
        printf("Error opening file!\n");
        return 1;
    }
    fprintf(file, "%lf\n",a);
    fprintf(file, "%lf\n",b);
    fprintf(file, "Area enclosed is : %.2f\n",area);
    

    fclose(file);

    printf("The area of the region bounded by the line, x-axis is : %.2f\n",area);

    return 0;
}
