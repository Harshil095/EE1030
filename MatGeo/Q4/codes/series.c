#include <stdio.h>
#include <math.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <sys/socket.h>
#include <netinet/in.h>

#include "libs/matfun.h"
#include "libs/geofun.h"

int main() {
    double BC, AB, AC; //using arrays

    printf("Enter the side BC value in cm : ");
    scanf("%lf", &BC);
    printf("Enter the side AB value in cm : ");
    scanf("%lf", &AB);
    printf("Enter the side AC value in cm : ");
    scanf("%lf", &AC);

    FILE *file = fopen("values.tex", "w");

    // Check if the file was opened successfully
    if (file == NULL) {
        printf("Error opening file!\n");
        return 1;
    }

    // Write the values to the file
    fprintf(file, " 7.06 \n");
    fprintf(file, " 7.00 \n");
    fprintf(file, " 9.00 \n");

    // Close the file
    fclose(file);

    printf("Values have been written to values.txt\n");

    return 0;
}

