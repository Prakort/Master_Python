#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <sstream>
#include <math.h>
#include <cstdio>
using namespace std;


int main(){

  int n,m;
  while( cin >> n >> m){
    if( n == 0 || m == 0 ) break; 
    vector< vector<char> > map;
    map.resize(n);
    for(int j = 0; j < n ; j++){
      map[j].resize(m);
      for(int i = 0 ; i < m ; i++){
        char x;
        cin >> x;
        cout << x ;
        map[j][i] = x;
      }
       cout << endl ;
    }

  }
}
