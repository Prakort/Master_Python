#include <iostream>
#include <string>
#include <algorithm>

using namespace std;

int main(){
  int n, x, y, p;
  // get the number of test cases
  cin >> n;
  while(n-- > 0){
    int d,t;
    // get the radius of explosion
    cin >> d;
    // get the number of rat population
    cin >> t;

    int data[1025][1025] = {0};
    while(t-- > 0){
      // get the coordinates and population of the rat
      cin >> x >> y >> p ;
      // find the lowerbound and upperbound with the radius
      for( int i = x - d ; i <= x + d ; i++){
        for( int j = y - d; j <= y + d ; j++){
          // check if the coordinate is valid
          if( i>= 0 && i < 1025 && j >=0 && j < 1025)
            // increment the rat population
            data[i][j] += p;
        }
      }
    }

    int max = -1, ans_x = 0, ans_y = 0;

    for( int i = 0; i < 1025; i++){
      for( int j = 0 ; j < 1025; j++){
        // find the largest population
        if( data[i][j] > max ){
          max = data[i][j];
          ans_x = i;
          ans_y = j;
        }
      }
    }
    cout << ans_x << " " << ans_y << " " << max << "\n";

  } 
}
