#include <iostream>
#include <cstdlib>
#include <cmath>
#include <fstream>

using namespace std;

int prime(int n){
  int m,s=0;
  m=sqrt(n);
  if(m==1){
    s=0; //it is prime
  }
  else{
    for(int i=2;i<m+1;i++){
      if(n%i==0){
        s=1;
        break;
      }
    }
  }
  return s;
}

int main(){
  int n,s,count;
  n=1000000;
  count=0;
  ofstream f; //open a file for writing
  f.open("primes.dat");

  for(int i=2;i<n+1;i++){
    s=prime(i);
    if(s==0){
      count+=1;
      f<<i<<" "<<1<<endl;
    }
    else if(s==1){
      f<<i<<" "<<0<<endl;
    }
  }

  f.close();
  printf("%d",count);


  return 0;
}
