import java.util.*;


class multidimensional{

    public static void print(int[] arr){

         for(int i = 0 ; i < arr.length; i++){
             System.out.print( arr[i] + "\t");
        }

    }

    public static void main (String[] args){
        
        int[] arr = {3,4,9,1,4,6};


        //Code to print the base of arrays
        System.out.println("Original Array: \n ");
        print(arr);
       
        //Sort 
        Arrays.sort(arr);

        System.out.println("\nSorted Array: \n ");
        print(arr);


        //Changing the data structure: we do asDataStructure()
        Arrays.asList(arr);
        print(arr);


        // binarySearch(arr_name, fromIndex, toIndex, key, comaparator)
        System.out.println("\nKey Element searching: \n" + Arrays.binarySearch(arr, 4));

        
        
        
            }
}