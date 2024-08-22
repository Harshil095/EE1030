#include <stdio.h>

// Function to calculate the coordinates of the fourth vertex D
void find_fourth_vertex(float A[3], float B[3], float C[3], float D[3]) {
    // Calculate the midpoint of diagonal AC
    float mid_AC[3];
    for (int i = 0; i < 3; i++) {
        mid_AC[i] = (A[i] + C[i]) / 2.0;
    }

    // Calculate the coordinates of D using the midpoint
    for (int i = 0; i < 3; i++) {
        D[i] = 2 * mid_AC[i] - B[i];
    }
}

int main() {
    // Define the coordinates of vertices A, B, and C
    float A[3] = {3.0, -1.0, 2.0};
    float B[3] = {1.0, -2.0, 4.0};
    float C[3] = {-1.0, 1.0, 2.0};
    float D[3]; // Coordinates of the fourth vertex D

    // Find the coordinates of the fourth vertex D
    find_fourth_vertex(A, B, C, D);

    // Print the coordinates of D
    printf("Coordinates of the fourth vertex D: (%.2f, %.2f, %.2f)\n", D[0], D[1], D[2]);

    return 0;
}

