#include<iostream>
#include<string>


using namespace std;

void f(){
  static int num=123;
}

void g(){
  static int num;
  cout<<num<<endl;
}

int main(){

  f();
  g();

  
  return 0;


}
