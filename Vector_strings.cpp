#include <iostream>
#include<string>
#include<vector>

using namespace std;

int main(){
  /*
  vector <string> v;
  v.push_back("joao");
  v.push_back("ana");
  v.push_back("antonio");
  v.push_back("carlos");

  sort(v.begin(),v.end());
  */

  int n=12345;
  string s;
  char a='1';
  s=to_string(n);
  n=s[0]-48;
  cout<<n<<endl;
  /*
  int l=v.size();
  for(int i=0;i<l;i++){
    cout<<v[i]<<endl;
  }
  */
 
  return 0;
}
