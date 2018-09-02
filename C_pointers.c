#include <stdio.h>

int main(){
  int a,b;
  int *arr[2]; //array of pointers
  int ar[2];



  ar[0]=a;
  ar[1]=b;

  arr[0]=&ar[0];
  arr[1]=&ar[1];

  a=10;
  b=20;

  for(int i=0;i<2;i++){
    *arr[i]=i+200;
  }
  for(int i=0;i<2;i++){
    printf("%d\n",ar[i]);
  }

  for(int i=0;i<2;i++){
    printf("value of arr[%d]=%d\n",i,*arr[i]);
  }


  return 0;
}
