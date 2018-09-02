#include <stdio.h>

int sum(int x, int y){
  return x+y;
}

int main(){
  printf("input value:\n");
  int a; // use lf for double
  scanf("%d",&a);
  printf("you entered %d",a);
  printf("insert another integer:\n");
int b;
  scanf("%d",&b);
  printf("the sum of %d and %d is:\n %d\n",a,b,sum(a,b));
  return 0;

}
