#include <iostream>
#include <cstdlib>
#include <cmath>
#include <fstream>

using namespace std;

int main(){
  ifstream f;
  f.open("primes.dat");
  int i=0;
  double a,b;

  while(i<10){
    f>>a;
    f>>b;
    cout<<a<<" "<<b<<endl;
    i+=1;
  }


  f.close();

  return 0;
}
