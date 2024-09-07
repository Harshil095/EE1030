#include <stdio.h>
#include <math.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <sys/socket.h>

#include "libs/matfun.h"
#include "libs/geofun.h"
int main() {
	double **A,**B,**C,**D;
	float x,y,z;
	A=createMat(3,1);
	B=createMat(3,1);
	C=createMat(3,1);
	D=createMat(3,1);
	A[0][0]=3;
	A[1][0]=-1;
	A[2][0]=2;
	B[0][0]=1;
	B[1][0]=-2;
	B[2][0]=4;
	C[0][0]=-1;
	C[1][0]=1;
	C[2][0]=2;
        D[0][0]=A[0][0]+C[0][0]-B[0][0];
	D[1][0]=A[1][0]+C[1][0]-B[1][0];
	D[2][0]=A[2][0]+C[2][0]-B[2][0];
	FILE *file =fopen("output.dat","w");
	if (file==NULL)  {
		printf("Error opening file!\n");
		return 1;
	}
	fprintf(file,"The value of x is %f\n",D[0][0]);
	fprintf(file,"The value of y is %f\n",D[1][0]);
	fprintf(file,"The value of z is %f\n",D[2][0]);
	fclose(file);

	freeMat(A,3);
	freeMat(B,3);
	freeMat(C,3);
	return 0;
}	

