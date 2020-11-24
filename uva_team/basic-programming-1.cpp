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
using namespace std;
int y,x;
vector< int > A;

void one(vector<int>& A){
  cout << 7 << endl;
}
void two(vector<int>& A){
  if(A[0] > A[1])
    cout << "Bigger\n";
  else if(A[0] == A[1])
    cout << "Equal\n";
  else 
    cout << "Smaller\n";
}

void three(vector<int> A){
  int b[3] ={A[0], A[1], A[2]};
  sort(b, b + 3);
  cout << b[1] << endl;
}

void four(vector<int>& A){
  int s = 0;
  for( int c : A)
    s += c;
  cout << s << endl;;
}

void five(vector<int>& A){
  int s = 0;
  for( int c : A){
    if(c % 2 == 0){
      s += c;
    }
   
  }

  cout << s << endl;
}

void six(vector<int>& A){
  string s = "";
  for(int c : A){
    s += char(97 + c % 26);
  }

  cout << s << endl;
}

void seven(vector<int>& A) {
  int i = 0;
  int n = A.size();
  vector<int> seen(n);
  while(1){
    if(seen[i] == 1){
      cout << "Cyclic" << endl;
      break;
    }

    if( i >= n){
      cout << "Out" << endl;
      break;
    }
    if( i + 1 == n){
      cout << "Done" << endl;
      break;
    }
    seen[i] = 1;
    i = A[i];
  }
}

int main(){
  

  cin >> y >> x;
  int m = y;
  A.resize(y);
  int i = 0;
  while( m--){
    int a;
    cin >> A[i];
    i++;
  }

  switch (x)
  {
    case 1: 
      one(A);
      break;
    case 2: 
      two(A);
      break;
    case 3: 
      three(A);
      break;
    case 4: 
      four(A);
      break;
    case 5: 
      five(A);
      break;
    case 6: 
      six(A);
      break;
    case 7: 
      seven(A);
      break;  
    default:
      break;
  }


}
