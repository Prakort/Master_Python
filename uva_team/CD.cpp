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
  do {

  std::unordered_set < long unsigned > Jack;
  std::cin >> N >> M;
  if( N==0 || M ==0)
    break;
  int i = N+M;
  int t = N+M;
  while(i--){
    long unsigned x;
    std::cin >> x;
    Jack.insert(x);
  }
  std::cout << t - Jack.size() << endl;
  } while (1);
}
