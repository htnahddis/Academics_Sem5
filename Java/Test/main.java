import java.util.*;

class main {

    public static void main ( String[] args){

        Scanner in = new Scanner(System.in);

        System.out.println("Enter the two numbers: ");
        int num1 = in.nextInt();
        int num2 = in.nextInt();

        int sum = summation(num1, num2);
        System.out.println(sum);
    }

    public static int summation( int a, int b){
        return (a + b);

    }
}