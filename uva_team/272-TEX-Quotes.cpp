#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <sstream>

using namespace std;

int main(){

  string line;
  // boolean for switch the `` and ''
  int flag = 1;
  // get each line
  while( getline(cin, line)){
    
    for( int i = 0 ; i < line.length(); i++){
      // only "" could be changed
      if( line[i] == '"'){
        // 1 type at a time
        string output = flag ? "``" : "''";
        cout << output;
        // switch boolean
        flag = !flag;
      }else {
        cout << line[i];
      }
    }
    cout << endl;
  }

}
