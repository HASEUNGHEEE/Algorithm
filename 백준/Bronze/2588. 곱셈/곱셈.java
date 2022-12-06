import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int firstNum = scan.nextInt();
        int secondNum = scan.nextInt();
        System.out.println(firstNum * (secondNum % 10));
        System.out.println(firstNum * (secondNum % 100 / 10));
        System.out.println(firstNum * (secondNum / 100));
        System.out.println(firstNum * secondNum);
    }
}