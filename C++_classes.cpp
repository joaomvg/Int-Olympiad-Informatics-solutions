// classes example
#include <iostream>
using namespace std;

int area(int x,int y){
  return x*y;
}

class Rectangle {
    int width, height;
    int b(){
      return width*height;
    }
  public:
    void set_values (int x,int y){
      width = x;
      height = y;
    };
    int a=b();
};

/*
void Rectangle::set_values (int x, int y) {
  width = x;
  height = y;
}
*/

//int Rectangle:: a(){return width*height;}

int main () {
  Rectangle rect;
  rect.set_values (3,4);
  // cout<<"width="<<rect.width; Error: private members cannot be accessed

  cout << "area: \n" << rect.a;
  return 0;
}
