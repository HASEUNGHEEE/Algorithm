import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        int[] array = new int[N];
        
        StringBuilder sb = new StringBuilder();

        for (int i = 0; i < N; i++) {
            int value = Integer.parseInt(br.readLine());
            array[i] = value;
        }
        Arrays.sort(array);
        
        for (int i = 0; i < array.length; i++) {
            sb.append(array[i]).append('\n');
        }
        System.out.println(sb);
    }
}