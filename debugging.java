

import java.util.HashSet;
import java.util.Set;
import java.util.*;
import java.lang.*;

public class debugging {

  public static void main(String[] args) {
    int arr[][] = new int[][]{{1,2,3,4},{1,2,3,4}};
    // boolean q1 = pair(2, 4, arr, 8);
    // System.out.println(q1);

    // String vowel = "aaabceee";
    // System.out.println(removeConsecutiveVowel(vowel));
    // 1-2-10
    // 1-4-5
    // 
    int a2[] = new int[]{ 1, 4, 6, 2, 3, 8 }; 
    // int a = countTripletSumPermutation(a2.length, a2, 24);
    // System.out.println(a);

    // int sum = calculateSumOfNumbersInString("a1b2");
    // System.out.println(sum);

    // String ans = reverseAlphabetCharsOnly("a!!!b.c.d,e'f,ghi");
    System.out.println(compareProduct(1221));

    int a3[] = {15, 18, 2, 3, 6, 12}; 
    System.out.println(rotation(a3.length, a3));

  } 


  static boolean pair(int rows, int cols, int arr[][], int sum){

    Set<Integer> set = new HashSet<Integer>();

    for (int i = 0; i < rows; i ++){
      for (int j = 0 ; j < cols ; j++ ){
        if(set.contains(sum - arr[i][j])){
          
          return true;
        }else{
          // incorrect
          set.add(sum);
          // correct 
          set.add(arr[i][j]);
        }
      }
    }

    return false;
  }

  static boolean isVowel(char ch){
    return ch == 'a' || ch == 'i' || ch == 'u' || ch == 'e' || ch == 'o';
  }


  // change && to ||
  static String removeConsecutiveVowel(String str){
    String str1 = "";
    str1 = str1 + str.charAt(0);

    for( int i = 1; i < str.length() ; i ++)
      // && => ||
      if((!isVowel(str.charAt(i-1))) && (!isVowel(str.charAt(i)))){
        char ch = str.charAt(i);
        str1 = str1 + ch;
      }

    return str1;
  }



  static int countTripletSumPermutation(int size, int []arr, int tripletSum ){
    int count = 0;
    for( int i = 0; i < size - 2; i++){
      if(tripletSum % arr[i] == 0){
        for ( int j = i + 1; j < size - 1; j++){
            if(tripletSum % (arr[i] * arr[j]) == 0){
              // int value = tripletSum / (arr[i] * arr[j]); <- n/ 0 which wont work
              for ( int k = j +1 ; k < size ; k ++ ){
                if (arr[k] * arr[i] * arr[j] == tripletSum){
                  count++;
                }
              }
            }
        
        }
      }
    }

    return count;
  }

  // add { } else condition or indent the temp = "0"
  // test case temp shoud be '0'
  // "" empty string
  static int calculateSumOfNumbersInString(String inputString){
    
    int sum = 0;

    // for(int i = 0; i < inputString.length(); i++){
    //   char ch = inputString.charAt(i);
    //   if (Character.isDigit(ch))
    //     sum += Integer.parseInt(Character.toString(ch));
    // }
    String temp = "0";
    for(int i = 0; i < inputString.length(); i++){
      char ch = inputString.charAt(i);

      if (Character.isDigit(ch)){
        temp += ch;
      }
      else{
        sum += Integer.parseInt(temp);
        temp = "0";
      }
     
    }
    return sum + Integer.parseInt(temp);
  }


  // update pointers right away when swapping the chars
  static String reverseAlphabetCharsOnly(String inputString){

    char [] inputChar = inputString.toCharArray();

    int right = inputString.length() - 1;
    int left = 0;

    while(left < right){
      if(! Character.isAlphabetic(inputChar[left]))
        left++;
      else if (!Character.isAlphabetic(inputChar[right]))
        right--;
      else{
        char temp = inputChar[left];
        inputChar[left] = inputChar[right];
        inputChar[right] = temp;
        // Correct
        left++;
        right--;
      }
      // Incorrect
      // left++;
      // right--;

    }

    return new String(inputChar);
  }

  static boolean compareProduct(int num){
    if (num < 10)
      return false;
    int oddProdValue = 1, evenProdValue = 1;
    int index = 0;
    while(num > 0){
      int digit = num % 10;
      if (index % 2 == 1)
        oddProdValue *= digit ;
      else
        evenProdValue *= digit ;
      num = num /10;

      index++;
      // if (num == 0)
      //   break;
      // digit = num % 10;
   
      // evenProdValue *= digit;
      // num = num / 10;

    }
    
    if ( evenProdValue == oddProdValue)
      return true;

    return false;
  }


  static int help(int list[], int low, int high){
    if (high < low)
      return 0;
    if (high == low)
      return low; 

    int mid = low + (high - low )/ 2;
    if (mid < high && list[mid+1] < list[mid])
      return (mid + 1);

    // correct
    if (mid > low && list[mid]< list[mid-1])
    // wrong
    // if (mid > low && list[mid] > list[mid-1])
      return mid; 

    return help(list, mid, high);
  }

  static int rotation(int size, int list[]){
    int res = help(list, 0, size-1);
    return res;
  }

}
