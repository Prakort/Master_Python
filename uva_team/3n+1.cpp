#include <iostream>  
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int solution(int n){
  vector<int> vec;
  while (n != 1)
  {
    if (n % 2 == 1) n = (3 * n) + 1;
    else n = n / 2;
    vec.push_back(n);
  }
  vec.push_back(1);
  return vec.size();
}

int main(){
  int x, y;

  while( cin >> x >> y) {
    int ans = 0;

    int min = x < y ? x : y;
    int max = x > y ? x : y;

    for( int i = min; i <= max; i++){
      int count = solution(i);
      if( count > ans) ans = count;
    }
    cout << x << " " << y << " " << ans;
    cout << endl;
  }

}
