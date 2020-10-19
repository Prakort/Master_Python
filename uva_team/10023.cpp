#include <iostream>  
#include <string>
#include <vector>
#include <bitset>
#include <algorithm>
#include <map> 

using namespace std;

// 10^1000
// double double
// 7206604678144
// 3000000000000
// 400 => [4,0,0]
//  2 => [2,0,0]
// 

// divide by two func
// multiply function
// addition function

// x * x = y
// min y = x, max => x = y/2
// 1 * 1 = 1
// 2 = 4 / 2
unsigned int sqrt(unsigned int x){

  if (x <= 1) return x;
  unsigned int low = 2, hi = x;

  while( low <= hi ) {
    unsigned int mid = low + ( hi - low ) / 2 ;
    unsigned int n = mid * mid ;

    if ( n > x ) hi = mid - 1;
    else if ( n < x ) low = mid + 1;
    else return mid;
  }
  return hi;
}
int main() {

  unsigned int n, x;
  cin >> n;

  while( n > 0 ){
    cin >> x;
    cout << sqrt(x);
    n--;
  }
  // cout << 2684512 * 2684512 << " answer ";
  //2684512

}
