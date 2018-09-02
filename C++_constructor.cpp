#include <iostream>

class P{
  int **a;

  public:
    P(int **x){ //constructor: basically initialises a
      a=x;
    }

  int b(){
    return **a;
  }
};

int main(){
  int **a;

  a=(int **) malloc(1*sizeof(int *));
  a[0]=(int *) malloc(2*sizeof(int));

  a[0]={4,5};

  P f(a);

  printf("%d\n",f.b());
 return 0;
}
