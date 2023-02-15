import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        System.out.println(factorial(N));
    }
    
    public static int factorial(int N) {
        if (N <= 1) return 1; // 재귀 종료 조건
        return N * factorial(N - 1);
    }
}