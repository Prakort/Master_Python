#include <iostream>
#include <string>
#include <algorithm>
#include <cmath>
#include <stdio.h>

#define EPS 1e-9 // .0000009

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
  double mid = 0;
  int exist = lower * upper > 0 ? 0 : 1;
  // IVT if [a,b] if f(a)  and f(b) have opposite sign, x exists
  if( exist ){
    double low = 0.0;
    double hi = 1.0;

    // using bisection to find the right answer
    while(low + EPS < hi){
      mid = (hi + low) / 2;
      if( eq(mid) < 0){
        hi = mid;
      } else {
        low = mid;
      }
    }
    printf("%.4lf\n", mid); 

  } else {
    cout << "No solution\n";
  }
}
int main(){
  while( cin >> p >> q >> r >> s >> t >> u){
    solution();
  }
}
