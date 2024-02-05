import java.util.Scanner;

public class Factorial{
    public static void main(String[] args) {

        Scanner scan = new Scanner(System.in);

        System.out.print("\nEnter Number To Find Factorial (integer only) : ");
        int num = scan.nextInt();

        int fact = 1;
        
        for(int i = 1;i<=num;i++){
            fact *= i;
        }

        System.out.println("\nFactorail Of Number " + num + " Is = " + fact);

    }

}