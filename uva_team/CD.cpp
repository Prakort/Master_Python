/**
 * Prakort Lean
 * 104932087 
 **/
#include <iostream>
#include <string>
#include <vector>
#include <bitset>
#include <algorithm>
#include <map>
#include <set>
#include <queue>
#include <cstring>
#include <sstream>
#include <cstdio>
#include <math.h>
#include <ctype.h>
#include <bits/stdc++.h> 
using namespace std;

int main(){

  int N, M;
  std::unordered_set < long unsigned > Jack;
  std::cin >> N >> M;

  int i = N+M;
  int t = N+M;
  while(N--){
    long unsigned x;
    std::cin >> x;
    Jack.insert(x);
  }
  long unsigned count = 0;
  while(M--){
    long unsigned x;
    std::cin >> x;
    auto i = Jack.find(x);
    if(i != Jack.end()){
      count +=1;
    }
  }


  // long counter =  t - Jack.size();
  std::cout << count << endl;

  if(N == '0' && M == '0')
    return 0;
  

}
