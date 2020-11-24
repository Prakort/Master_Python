#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <sstream>
#include <math.h>
#include <cstdio>
using namespace std;

int memo[21][201];
int costs[21][21];
int N,M,C;
int num_garment;
int solution(int money, int garment){
  //cout << money << " " << garment << endl;
  if( money < 0) return -10000000;
  if( garment ==  num_garment) return M - money;

  int & ans = memo[money][garment];

  if( ans > -1) return ans;

  for(int model = 1; model <= costs[garment][0]; ++model){
    ans = max(ans, solution(money - costs[garment][model], garment+1));
  }
  cout << ans << endl;
  return ans;

};
int main(){
  int cases;
  cin >> cases;

  while (cases-- )
  {
   int num_garment;
   cin >> M >> num_garment;

   for(int i = 0; i < num_garment ; i++)
   {  
     int number_g;
     cin >> number_g;
     for(int j = 0; j < number_g ; ++j){
      int x;
      cin >> x;
      cout << x << endl;
      // cin >> costs[i][j];      
     }
   
   }
  memset(memo, -1, 200 * 20 * 4);
  int ans = solution(M, 0);
  if(ans > 0)
    cout << ans << endl;
  else 
  {
    cout << ans << endl;
     cout << "No solution\n";
  }
   
  }
  
}
