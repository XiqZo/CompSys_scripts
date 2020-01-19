#include <stdio.h>
#include <math.h>
#include <stdlib.h>

int main (){
    double AddressSize;
    double E;
    double C;
    double B;
    double retIndex;  
    double retOffset;
    double retTag; 

    printf( "Enter Address size : ");
    scanf("%lf", &AddressSize);
    printf( "Enter the Set associative E : ");
    scanf("%lf", &E);
    printf( "Enter the Data cache size in kb : ");
    scanf("%lf", &C);
    printf( "Enter the Block Size: ");
    scanf("%lf", &B);

    C = C*1024;

    retOffset = log2(B);
    retIndex = log2(C/(E*B));
    retTag = AddressSize-(retOffset + retIndex);
    printf("\nOffset bits = %lf\n", retOffset); 
    printf("Set index bits = %lf\n", retIndex); 
    printf("Tag bits = %lf\n", retTag); 
    return 0;
}
