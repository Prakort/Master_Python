#include <iostream>
#include <string>
#include <algorithm>
#include <cmath>
#include <stdio.h>

#define EPS 1e-7 // .0000007

using namespace std;
// coefficients
double p, q, r, s, t, u;
// define the equation
double eq(double x){
  return p*(exp(-x)) + q*(sin(x)) + r*cos(x) + s*tan(x) + (t*(x*x)) + u;
}

void solution(){
  // find the lower and upper bound of f(x)
  double lower = eq(0);
  double upper = eq(1);

  // IVT if [a,b] if f(a)  and f(b) have opposite sign, x exists
  if( (lower * upper) < 0 ){
    double low = 0;
    double hi = 1;

    // using binary search to find the right answer
    while(low + EPS < hi){
      double mid = (hi + low) / 2;
      if( eq(mid) <= 0){
        hi = mid;
      } else {
        low = mid;
      }
    }
    printf("%.4lf\n", (low + hi)/2); 

  } else {
    cout << "No solution\n";
  }
}
int main(){
  while( cin >> p >> q >> r >> s >> t >> u){
    solution();
  }
}
