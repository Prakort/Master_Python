#include <iostream>
#include <string>
#include <sstream>
#include <algorithm>

using namespace std;
double H, U, D, F;

void solution(){
  // calculate the reduce factor after a successive day
  double reduce = (F/100.0) * U;
  // start height each day
  double start = 0;
  // height after the night time
  double afterNight = 0;
  // height climbed during the day
  double climbed = 0;
  // day counter, start from 1
  int i = 1;
  while(1){

    // start height of the new day is the afterNight height
    start = afterNight;
    // height of the well climbed during the day
    climbed = start + U;

    // each day reduce the climbed by its factor
    // we can only reduce if U is pos+
    if(U > 0)
      U -= reduce;

    // snail climbed the wall
    if(climbed > H) break;
    // snails falls back during the night 
    afterNight = climbed - D;
    // snall falls back to the bottom of the well
    if (afterNight < 0) break;
    
    i++;

  }

  if( climbed > H){
    cout << "success on day " << i << endl;
  }else{
    cout << "failure on day " << i << endl;
  }

}
int main(){

  while( cin >> H >> U >> D >> F){
    if(H == 0) break;
    
    solution();
  }
}
