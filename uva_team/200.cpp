#include <iostream>  
#include <string>
#include <vector>
#include <bitset>
#include <algorithm>
#include <map> 
#include <set> 
#include <deque>
#include <cstring>
using namespace std;

/** 
 * Prakort Lean 
 * Jameel Jiwani
 * Bilal Malik
 * Problem: 200 Rare Order 
 * link: https://onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=136
**/



// Convert integer value to ASCII character
char toChar(int x){
  return char(x + 'A');
}
// Convert character value to integer value
int toInt(char c){
  return c - 'A';
}

string solution(vector<string> words) {

  // Define our graph for Topological sorting
  // key: character appears first
  // value: a set of the characters appears after
  map<int, set<int> > graph;

  // Degree of every first node is zero
  int indegree[26] = {0};

  // Let's add an empty set for each key
  for( auto w: words){
    for( auto c : w){
      // Since map in C++ allows duplicate key
      // we have to check if the key already exists
      if(graph.find(toInt(c)) == graph.end()){
        graph.insert(make_pair(toInt(c), set<int>()));
      }
    }
  }


  // iterate through words to find the order/relation

  // We apply the 2 rules of the sorting 
  for(int i = 1 ; i < words.size() ; i++){
    // compare two words
    string word1 = words[i-1];
    string word2 = words[i];
    
    for( int j = 0; j < word1.length() ; j++){
      // sorted words, the length of word1 should not be greater than word2
      if( j == word2.length())
        return "";
      // Find the first different character
      if(word1[j] != word2[j]){
        // convert them to integer value
        int start = toInt(word1[j]);
        int dist = toInt(word2[j]);

        // we already know the key exists 
        auto it = graph.find(start);
  
        // let's get the set of that key
        auto list = it->second;
        // Make sure there is no duplicate of the dist character
        // since we have to increment its indegree
        auto find = list.find(dist);
        // node has not appears after start character yet
        if( find == list.end()){
          // add the node into the set
          it->second.insert(dist);
          // increment its indegree
          indegree[dist]++;
        }
        // break since we found the first diff character between 2 strs      
        break;
      }
    }
  }

  // define deque since it allows to check level by level
  deque<char> orders;
  string ans = "";

  // How do we know which character start first?
  // If a character with indegree 0 then it starts first
  // Number of indegree is 0 means there is no char appears before it
  for( auto it = graph.begin(); it != graph.end(); it++){
    auto key = it->first;
    // 0 indegree
    if(indegree[key] == 0){
      // push into the deque
      orders.push_front(key);
      // convert back to the char
      char c = toChar(key);
      // append to the string result
      ans.push_back(c);
    }
  }
  // keep checking til deque is empty
  while(orders.size() != 0){
    // get current char and find the characters appears after it
    int cur = orders.front();
    orders.pop_front();

    auto find = graph.find(cur);
    set<int> list = find->second;
    // iterate through the set
    for( auto it = list.begin(); it != list.end() ;it++){
      int n = *it;
      // decrement the indegree of the node that has CURRENT char appears before
      indegree[n]--;
      // if the indegree of that NODE is zero that means it's time for it to appear
      if(indegree[n] == 0){
        char c = toChar(n);
        // add the NODE char to the sequence
        ans.push_back(c);
        // append the NODE to the deque
        orders.push_back(n);
      }
    }

  }

  // Why do we have to check if the length of the key with the length of the result?
  // in case there is a loop, the length of result will be less than the length of the key
  return graph.size() == ans.length()? ans : "";
  
}

int main(){

  // declare a string
  string str; 
  vector<string> words;
  // keep reading the string
  while( cin >> str ) {
    // stop when there is '#'
    if( str == "#") {
      cout << solution(words) << endl;
      words.erase(words.begin(), words.end());
    }else {
      words.push_back(str);
    };
   
  }
  // call the solution function

}
