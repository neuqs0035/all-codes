public class Sum {
    
    public static void main(String[] args) {
        
        int arr[] = {2,5,46,7,67,678,2,434,45,56};

        System.out.println("Total Elements Sum Is = " + sum_elements(arr));
    }

    public static int sum_elements(int arr[]){

        int sum = 0;

        for (int i : arr) {
            
            sum += i;

        }

        return sum;
    }
}
