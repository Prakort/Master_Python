/**
 * Prakort Lean
 * 104932087 
 **/
#include <algorithm>
#include <cstddef>
#include <iostream>
#include <string>
#include <vector>
 
using namespace std;

string N;

void solve(){
  int map[128];

  for(char c: N){
    int index = (int)c;
    cout << index << endl;
  }
}

int main(){
  int flag = 0;
  while (cin >> N)
  {
    if(flag){
      cout << endl;
    }
    flag = 1;

    solve();
  }
  
}
