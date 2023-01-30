import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int T = sc.nextInt();
        
        for (int i = 0; i < T; i++) {
            String[] numbers = sc.next().split(",");
            int A = Integer.parseInt(numbers[0]);
            int B = Integer.parseInt(numbers[1]);
            System.out.println(A + B);
        }
    }
}