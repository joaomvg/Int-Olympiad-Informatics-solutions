#include <iostream>
#include <vector>

using namespace std;


int main(){
  vector<pair<int,int> > v;
  pair <int,int> apair;
  int l=10;

  apair.first=1;
  apair.second=2;
  

  for(int i=0;i<l;i++){
    apair.first=i;
    apair.second=i;
    v.push_back(apair);
  }

  cout<<"size="<<v.size();
  l=v.size();
  for(int i=0;i<l;i++){
    cout<<v[i].first<<"..."<<v[i].second<<endl;
  }
  
  return 0;
}
