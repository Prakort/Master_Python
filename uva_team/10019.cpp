#include <iostream>  
#include <string>
#include <vector>
#include <bitset>
#include <algorithm>
#include <map>
using namespace std;

void solution(int x){

  int copy1 = x;
  int copy2 = x;
  int b2 = 0;
  int rem2 = 0;

  map<int, int> m ;
  m.insert(pair<int, int>(0,0));
  m.insert(pair<int, int>(1,1));
  m.insert(pair<int, int>(2,1));
  m.insert(pair<int, int>(3,2));
  m.insert(pair<int, int>(4,1));
  m.insert(pair<int, int>(5,2));
  m.insert(pair<int, int>(6,2));
  m.insert(pair<int, int>(7,3));
  m.insert(pair<int, int>(8,1));
  m.insert(pair<int, int>(9,2));


  while(copy2 != 0){
    rem2 = copy2 % 10;
    copy2 /= 10;
    b2 += m.find(rem2)->second ;
  }

  int b1 = 0;
  int rem;

  while (copy1 != 0)
  {
    rem = copy1 % 2;
    copy1 /= 2;
    if (rem == 1) {
      b1++;
    }
  }
 
  cout << b1 << " " << b2 << endl;
 
}
int main() {


  int n, x;
  cin >> n;
  while(n > 0){
    cin >> x;
    solution(x);
    n--;
  }
  
}


