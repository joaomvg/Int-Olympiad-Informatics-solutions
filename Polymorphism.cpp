#include <iostream>

using namespace std;

class A{
  int x;
public:
  void setx(int w){
    x=w;
  }
  void p(){
    cout<<"x="<<x<<endl;
  }
};

class B: public A{
public:
  void copy(){
    p();
  }
};


class C: public A{
public:
  void copy(){
    p();
  }
};

int main(){
  A a,*p1,*p2;
  B b;
  C c;

  p1=&b;
  p2=&c;
  
  p1->setx(3);
  p2->setx(45);
  
  b.copy();
  c.copy();

  return 0;
  
  
}
