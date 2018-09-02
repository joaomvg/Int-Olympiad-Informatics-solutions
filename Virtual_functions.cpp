#include <iostream>

using namespace std;

class A
{
public:
  void p(){
    cout<<"some other example"<<endl;
  }
  virtual void f()=0;
};

  class B: public A{
    void f(){
      cout<<"class B"<<endl;
    }
  };


class C: public A{
public:
  void f(){
    cout<<"class C"<<endl;
  }
};

int main(){
  B b;
  C c;
  A *a1,*a2; //cannot create an object but can create pointer too

  a1=&b;
  a2=&c;

  a1->f(); //note that I am calling function f() which is not defined in class A but it works because the pointer points to the classes B and C and they inherit function f()
  
  a2->f();

  a1->p();
  a2->p();
  cout<<"a different way"<< endl;
  
  b.p();
  c.p();

  return 0;
  
}
