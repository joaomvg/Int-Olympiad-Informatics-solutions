#include <iostream>

class add{
  int a;
  int b;
  public:
    add(int x, int y){
      a=x;
      b=y;
    }
    int adt(){
      return a+b;
    }
};


int main(){

  int a,b;
  a=2;
  b=4;
  add A(a,b);

  printf("sum of %d and %d=%d",a,b,A.adt());

}
