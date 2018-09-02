#include <stdio.h>


int *sq(int *p){
  *p=56;
  return p;
}

int main(){
  int n=5;
  int *ptr;
  ptr=&n;

  printf("n=%d\n",n);
  printf("n=%d\n",*sq(ptr));
  printf("n=%d\n", n);

  return 0;
}
