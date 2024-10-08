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
        D=Matadd(A,C,3,1);
	D=Matsub(D,B,3,1);
	FILE *file =fopen("output.dat","w");
	if (file==NULL)  {
		printf("Error opening file!\n");
		return 1;
	}
	fprintf(file,"X\n");
        fprintf(file,"%f\n",D[0][0]);
	fprintf(file,"%f\n",D[1][0]);
	fprintf(file,"%f\n",D[2][0]);
	fclose(file);

	freeMat(A,3);
	freeMat(B,3);
	freeMat(C,3);
	return 0;
}	

