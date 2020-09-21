
/**
 * basic
 */
import java.io.*;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Collections;
import java.util.Comparator;
import java.util.LinkedList;
public class basic {

  private static int size;

  public static void main(final String[] args) {

    // array
    /***
     * All array are dymanically allocated
     * Size must be initialized 
     */
    // 1D array
    int nums[]  = new int[]{1,2,3,4,5,6};
    nums[0] = 5;
    Arrays.sort(nums);    // sort the array
    int cloned[] = nums.clone(); // deepcopy
    Arrays.fill(nums, 10); // fill every element to be 10

    // 2D array
    int multi[][] = new int[20][10]; // 20 rows x 10 cols
    int arr[][] = { {2,7,9},{3,6,1},{7,4,2} };    // declaring and initializing 2D array 

    arr.getClass(); // get the class of the array type
    for (int[] row : arr) // Fill each row with 10.  
      Arrays.fill(row, 10); 

    
    // List
    List<Integer> list = new ArrayList<Integer>();
    List<Integer> list2 = new ArrayList<Integer>();
    list.add(0); // append element at the end of the list
    list.add(20);
    list.add(20);
    list.add(20);
    list.add(20);
    System.out.println(list.toString());
    list.set(1, 2); // replace the element at index
    System.out.println(list.toString());
    list.add(1, 222); // append element at index 0, shift to the right 
    System.out.println(list.toString());
    // for( Integer x: list){
    //   System.out.println(x);
    // }
    list.add(0, 1); // append element at index 0
    list.addAll(list2); // add all element from list2

    // list.clear(); // remove all elements
    list.contains(1); // return true if the element exists
    list.containsAll(list2); // return true if list1 has all the list2 elemetns
    list.equals(list2); // return true if list1 == list2
    list.get(0); // return element at index 0
    list.indexOf(1); // return the index of the 20 element
    list.isEmpty(); // check if the list is empty
    list.iterator(); // return an iterator over the element
    list.lastIndexOf(20); // return the last index of the element
    list.listIterator(); // return a list iterator over the list element
    //list.remove(1); // remove an element at first occurrence
    list.removeAll(list2); // remove all element from list1 that contains in list2
    list.set(1, 2);
    // System.out.println(list.toString());
    // for( int x: list){
    //   System.out.println(x + " ");
    // }
    list.size(); // return the size of the list
    // list.sort();
    Collections.sort(list);
    list.sort((a,b)-> b - a );

    int size = list.size();
    Integer temp [] = list.toArray( new Integer[size]); // convert list to array with size



    // LinkedList
    LinkedList<Integer> lk = new LinkedList<>();
    int index  = 0; int el = 10;
    System.out.println("LinkedList\n");
    lk.add(el); // appends the element at the end
    System.out.println(lk.toString());
    lk.add(index, el); // add the element at index
    lk.addAll(list); // append all the element from iterator at the end of the list
    System.out.println(lk.toString());
    lk.addFirst(1111); // append element to the front of the list, all elements shift to the right
    System.out.println(lk.toString());
    lk.addLast(9999); // append element to the end of linkedlist
    System.out.println(lk.toString());
    // lk.clear();
    lk.contains(el); // check if the list contains elemenet
    int element = lk.element(); // return the first element of the list, not remove
    System.out.println("First element is " + element + " \n");
    lk.get(1); // return the element in the index
    lk.getFirst(); // get first el
    lk.getLast(); // get last el
    lk.indexOf(el); // return the index of the first occurrence of the el
    lk.lastIndexOf(el); // return the last index of the el
    lk.listIterator(); // return iterator list
    System.out.println(lk.toString());
    lk.offer(1992); // add the el as the tail 
    System.out.println(lk.toString());
    lk.offerFirst(1991); // insert the el to the front of the list
    System.out.println(lk.toString());
    lk.offer(1993); // insert the el to the tail
    System.out.println(lk.toString());
    /**
     * addFirst() vs offerFirst()
     * offerFirst is safer if the dque reach capacity, it will return false
     * but addFirst will throw exception
     */
    
  }
}

