#include <iostream>  
#include <string>
#include <vector>
#include <bitset>
#include <algorithm>
#include <map> 


using namespace std;

// read input and store them into an array
// task1 build inorder map 
// inorder = map
// graph = map 
// for i in len(words):
//   for c in words[i]:
//     inorder[map] = 0
//     graph[c] = set()

// task2 build graph (char appear before) -> char appears after
// for i in n-1:
//   w1 = str[i]
//   w2 = str[i+1]
//   for j in len(w1):
//     if j == len(w2) break 
//     if w2[j] == w1[1] continue 
//     else 
//       src = w1
//       dis = w2 
//       graph[src].add(dis)
//       inorder[dis]++

// task3 find the first letter 
// ans = ""
// q = queue()
// for c in inorder:
//   if inorder[c] == 0:
//     q.append(c)
//     ans += c


// task4 travel level by level 

// while q is not empty: 
//   current = q.pop()
//   for node in graph[current]:
//     inorder[node]--
//     if inorder[node] == 0:
//       ans += node 
//       q.append(node)

// return ans if len(ans) == len(ans) else ""

string solution(vector<string> words) {
  string ans = "";
  int n = words.size(); 
  map<string, vector<string> > graph;
  map<string, int> indegree;

  cout << n << endl;
 
  return ans;
  
}


int main(){
  
  string str; 
  while( cin >> str ) {
    vector<string> words;
    if( str == "#") break;  
    words.push_back(str);
  }

}
