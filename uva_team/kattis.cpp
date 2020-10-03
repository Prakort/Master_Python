#include <iostream>  
#include <string>
#include <vector>
#include <bitset>
#include <algorithm>
#include <map> 
#include <sstream>
using namespace std;
int main() {
  string x;

  std::vector<string> vec;

  std::string line;

  while (getline(std::cin, line)) {
    std::vector<int> vec;
    istringstream ss(line); 
    do { 
        // Read a word 
      string word; 
      ss >> word; 
      if (ss != nullptr )
        vec.push_back(std::stoi(word));
      // Print the read word 
      cout << word << endl; 

    } while (ss);
  }

  // while(std::cin.getline(title)) {
  //   cout << x << "-";
  //   if(x != "\n") {
  //    cout << x << " ";
  //    vec.push_back(x);
  //   } else {
  //     cout << "clear" ;
  //   }
 
  // }

}
