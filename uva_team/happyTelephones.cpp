#include <iostream>  
#include <sstream>
#include <algorithm>

using namespace std;

int main() {
  int n, m;
  string str;

  while(1){
    cin >> n >> m; 
    // cout << n << "    " << m << endl;
    if( n == 0 & m == 0 )
      break;
  
    int start[1000000], end[1000000];
    int x, y;
    for ( int i = 0; i < n ; i++){
      cin >> x >> y >> start[i] >> end[i];
      end[i] += start[i];
    }
 

    for( int k = 0; k < m ; k++){
      cin >> x >> y;
      y +=x;
      int count = 0;
      for( int i = 0; i < n ; i++){
        if(max(x, start[i]) < min(y, end[i]))
          count++;
      }
      cout << count << endl;;

    }
  }
}

/***
 * 
 * 3 2
 * 2 3 2 3
 * 2 3 1 1
 * 3 3 4 5 
 * 2 3
 * 2 3
 * 
 ***/
