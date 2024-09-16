#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <sys/socket.h>
#include <netinet/in.h>

#include "libs/matfun.h"
#include "libs/geofun.h"
int main(){
	double **A,**B,**C,**U,**X,**Y,**mul;
	double **norm;
	A=createMat(3,1);
	B=createMat(3,1);
	C=createMat(3,1);
	U=createMat(3,1);
	A[0][0]=1;
	A[1][0]=1;
	A[2][0]=1;
	B[0][0]=2;
	B[1][0]=4;
	B[2][0]=-5;
	C[0][0]=1;
	C[1][0]=2;
	C[2][0]=3;
	X=Matadd(B,C,3,1);
	Y=transposeMat(X,3,1);
	mul=Matmul(X,Y,3,1,1);
	U[0][0]=(X[0][0])/7;
	U[1][0]=(X[1][0])/7;
	U[2][0]=(X[2][0])/7;
	FILE*file=fopen("output.dat","w");
	if(file==NULL){
		printf("Error opening file\n");
		return 1;
        }
	fprintf(file,"The value of Lambda is %f \n",(C[0][0]));
	fprintf(file,"The unit vector U is , x,y,z = %f %f %f",(U[0][0]),(U[1][0]),(U[2][0]));
	fclose(file);
	freeMat(A,3);
	freeMat(B,3);
	freeMat(C,3);
	freeMat(U,3);
	freeMat(X,3);
	freeMat(Y,3);
	return 0;
}
