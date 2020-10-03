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
      int lower_x = max(x - d, 0);
      int upper_x = min(x + y, 1024);
      int lower_y = max(y - d, 0);
      int upper_y = min(y + d, 1024);

      for( int i = lower_x ; i <= upper_x ; i++){
        for( int j = lower_y; j <= upper_y ; j++){
          // increment the rat population
          data[i][j] += p;
        }
      }
    }

    int max = 0, ans_x = 0, ans_y = 0;

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
