#include<iostream>
#include<string>


using namespace std;


int main(){

  string s="jan 123.423";

  string::size_type z;

  double x=stod(s,&z);
  
  cout<<x<<endl;

  
  return 0;


}
