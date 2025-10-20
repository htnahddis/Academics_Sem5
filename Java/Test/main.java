import java.util.*;
import java.util.Arrays;


class main {

    public static int[] School( int[] classOfStudents){

        //we need to find the mode, median and mean score of the class
        int[] stats = new int[2];
      

        //for now i will stor the mode, median and mean respectively in the stats array
        int mean = 0;

        for( int i = 0 ; i < classOfStudents.length; i++){
            mean += i;
        }

        stats[0] = mean/(classOfStudents.length - 1);

        Arrays.sort(classOfStudents);
        
        stats[1] = classOfStudents[ (int) classOfStudents.length/2 ];

        return stats;
    }

    public static void main (String[] args) {

        int[] solution = new int[2];

        Scanner in = new Scanner(System.in);

        System.out.println("What is the number of students who passed the final exam? /n");
        int totalNumberOfPassedStudents = in.nextInt();
                int[] arr = new int[totalNumberOfPassedStudents];

        for(int i = 0 ; i < totalNumberOfPassedStudents; i++){
            System.out.println("Enter the marks for studnet " + (i+1) + " :");
            arr[i] = in.nextInt();
        }

        solution = School(arr);

        System.out.println("The mean and median score of the class is " + solution[0] + ", " + solution[1] + ". ");
 
    }
}