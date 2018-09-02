#include <stdio.h>

int main(){
  //int n;
  //scanf("%d",&n);

  int a[2];
  int *p;
  a[0]=199;
  p=a; // a is a pointer to the first element of the array a[]
  printf("%d\n",*a);

  for(int i=0;i<2;i++){
    *(a+i)=2*i;
    printf("a[%d]=%d\n",i,*(a+i));
  }

  return 0;
}
