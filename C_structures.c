#include <stdio.h>

// recap structures in C

struct laptop{
  int battery;
  double cost;
};

int main(){
  struct laptop mac,mac2;
  struct laptop *lap; //pointer to structure
  lap=&mac;
  mac.battery=3;
  mac.cost=1000;

  mac2=*lap;
  mac2.battery=5;
  lap->battery=50; // use the pointer to change the value of mac.battery

  if(&mac==&mac2){
    printf("they point to the same thing.\n");
  }
  else{
    printf("no they do not point to the same thing.\n");
  }

  printf("battery=%d\n.",mac2.battery);
  printf("battery=%d\n.",mac.battery);

  printf("Mac cost is %lf.\n",mac.cost);
  printf("or using pointers:\n Mac cost is %lf.\n",lap->cost);
  return 0;
}
