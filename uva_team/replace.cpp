#include <string>
#include <iostream>

using namespace std;

bool replace(char *&toModify, const char* toFind, const char* replaceWith){
  
  int size = strlen(toModify);
  char newString[10000] = {0};

  int new_index = 0;
  int n = 0;
  int toFindLen = strlen(toFind);
  int toReplaceWithLen = strlen(replaceWith);

  for(int i = 0 ; toModify[i] != '\0' ;){
    if( toModify[i] == toFind[n]){
      bool match = true;
      for( int j = i; j < i+toFindLen ; j++){
        if (toModify[j] != toFind[n++]){
          match = false;
          break;
        }
      }

      // reset index for replaceWith
      n = 0;
      if( match ){
        // add replaceWith to the newString
        while(n < toReplaceWithLen){
          newString[new_index++] = replaceWith[n++];
        }
        // update i index of the toModify string
        // we update i + length toFind not replaceWith len
        i = i + toFindLen;
      }else{
        // increment i if there is no match
        i++;
      }
      // reset index of toFind
      n = 0;

    } else {
      // add current char to newString if there is no match
      newString[new_index++] = toModify[i++];
    }

  }
  // add '\0' to the end of char array
  newString[new_index] = '\0';
  toModify = &newString[0];
  return true;
}


int main(){
  char s[] = "aaa";
  // s = [a]
  char *p = &s[0];
  replace(p, "a", "ab");
  puts(p);
}
