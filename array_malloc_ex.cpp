#include <iostream>
#include <cstdlib>
#include <cmath>

void f(int x[2][2]){
  printf("%d",x[0][0]);
}

int main() {
  int **a;
  int b[2][2];
  b[0][0]=1;
  b[0][1]=25;
  b[1][0]=31;
  b[1][1]=49;

  a=(int **) malloc(2*sizeof(int*));
  a[0]=(int *)malloc(1*sizeof(int));
  a[1]=(int *)malloc(1*sizeof(int));

  a[0][0]=123;
  printf("%d, %d\n",**b,*(*b+1));

  return 0;
}
