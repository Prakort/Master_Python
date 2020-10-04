#include <iostream>
#include <string>
#include <algorithm>
#include <vector>

using namespace std;

int main(){

  int n, m;
  while(1){
    cin >> n >> m;
    if( n == 0 && m == 0) break;

    vector<int> heads;
    vector<int> knights;

    int x;
    while(n-- > 0){
      cin >> x;
      heads.push_back(x);

    }
    while(m-- > 0){
      cin >> x;
      knights.push_back(x);
    }

    // sort the cost
    sort(heads.begin(),  heads.end()); 
    sort(knights.begin(), knights.end());

    int cost = 0;
    int i = 0;
    int j = 0;

    for( ; i < knights.size(); i++){
      // only knight is equal or taller can slay head
      if( knights[i] >= heads[j]){
        cost += knights[i];
        // increment head index
        j++;
        // check if all heads are slayed
        if(j == heads.size()) 
          break;
      }

    }

    if( j == heads.size()){
      cout << cost <<  endl;
    } else {
      cout << "Loowater is doomed!\n";
    }

  }
}
