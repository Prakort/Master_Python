#include <iostream>
#include <string>
#include<stdio.h>
using namespace std;


string word;

string to_code(char c){
  if(
    c == 'B' ||
    c == 'P' ||
    c == 'F' ||
    c == 'V'
    )
    return "1";
  else if(
    c == 'C' ||
    c == 'S' || 
    c == 'K' ||
    c == 'G' || 
    c == 'J' ||
    c == 'Q' || 
    c == 'X' ||
    c == 'Z' 
  )
    return "2";
  else if(
    c == 'D' ||
    c == 'T'  
  )
    return "3";
  else if(
    c == 'L'
  )
    return "4";
  else if(
    c == 'M' ||
    c == 'N' 
  )
    return "5";
  else if(
    c == 'R' 
  )
    return "6";
  else 
    return "0";
}

void solution(){
  int n = word.length();
  string result = "";
  result += word.at(0);
  int i = 1;
  int j = 1;

  while(j < n && i < 4){
    string prev = to_code(word[j-1]);
    string code = to_code(word[j]);
  
    if( code == "0" || code == prev ){
      j++;
    } else {
      result += code;
      i++;
      j++;
    }
  }

  while( i++ < 4 ){
    result += "0";
  }
  printf("         %-25s%s\n", word.c_str() ,result.c_str());  

}
int main(){

  printf("         %-25s%s\n", "NAME","SOUNDEX CODE");
  while(cin >> word){
    solution();
  }
  puts("                   END OF OUTPUT");
}
