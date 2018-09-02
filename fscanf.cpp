#include <iostream>
#include <cstdlib>
#include <cmath>

int main(){
  FILE *f=fopen("primes.dat","r");
  int x[10][2];
  char a;

  for(int i=0;i<10;i++){
    fscanf(f,"%c",&a);
    printf("%c",a);
  }

  fclose(f);

  return 0;

}
