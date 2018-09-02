// Example program
#include <iostream>
#include <string>

using namespace std;

void f(int n, int *p, int **q){
    cout<<"addr n:"<<&n<<endl;
    cout<<"addr *p:"<<p<<endl;
    cout<<"addr p:"<<&p<<endl;
    cout<<"addr q:"<<q<<endl;
}

int main()
{
    int n=5;
    int *p;
    p=&n;
    f(n,p,&p);
    cout<<"-------"<<endl;
    cout<<"addr n:"<<p<<endl;
    cout<<"or"<<&n<<endl;
    cout<<"adress to pointer"<<&p;


  return 0;
}
