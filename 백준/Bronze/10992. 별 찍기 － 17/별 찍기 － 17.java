import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        br.close();

        StringBuilder sb = new StringBuilder();

        if (N == 1) {
            sb.append("*");
            System.out.println(sb);
            return;
        }

        // 첫번째 줄
        for (int j = 0; j < N - 1; j++) {
            sb.append(" ");
        }
        sb.append("*").append("\n");

        // 두번쨰 ~ N-1 번째 줄
        for (int i = 1; i < N - 1; i++) {
            for (int j = 1; j < N - i; j++) {
                sb.append(" ");
            }
            sb.append("*");
            for (int j = 1; j <= (2 * i) - 1; j++) {
                sb.append(" ");
            }
            sb.append("*").append("\n");
        }

        // N번쨰 줄
        for (int j = 0; j < (2 * N) - 1; j++) {
            sb.append("*");
        }
        System.out.println(sb);
    }
}