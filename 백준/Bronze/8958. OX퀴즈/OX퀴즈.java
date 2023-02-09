import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int testCaseNum = Integer.parseInt(br.readLine());
        
        StringBuilder sb = new StringBuilder();
        
        String[] arr = new String[testCaseNum];
        for (int i = 0; i < testCaseNum; i++) {
            arr[i] = br.readLine();
        }

        for (int i = 0; i < testCaseNum; i++) {
            int count = 0; // 연속된 횟수
            int sum = 0; // 누적 합

            for (int j = 0; j < arr[i].length(); j++) {
                if (arr[i].charAt(j) == 'O') {
                    count++;
                } else {
                    count = 0;
                }
                sum += count;
            }
            sb.append(sum).append('\n');
        }
        System.out.println(sb);
    }
}
