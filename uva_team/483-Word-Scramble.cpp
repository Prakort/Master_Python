#include <iostream>
#include <string>
#include <sstream>
#include <algorithm>

using namespace std;

string reverse(string str){

  int n = str.length();
  
  for( int i = 0; i < n / 2 ; i++){
    char t = str[i];
    str[i] = str[n - i - 1];
    str[n - i - 1] = t;
  }

  return str;
}
int main(){
  string line;
  // read each line
  while (getline(cin, line))
  {
    // need to get each word in the line
    stringstream str(line); 
    string word;
    // count # of ' '
    size_t n = count(line.begin(), line.end(), ' ');
    // iterate through the line
    while(getline(str, word, ' ')){
      // print the reverse word
      cout << reverse(word);
      // print ' ' if it's not the end of the line
      if (n-- > 0)
        cout << " ";
  
    }
    cout << endl; 
  }
  
}
