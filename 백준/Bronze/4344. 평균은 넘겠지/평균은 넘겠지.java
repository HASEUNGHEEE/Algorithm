import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int[] scoreArray;

        int testCaseNum = Integer.parseInt(br.readLine());
        StringTokenizer st;



        for (int i = 0; i < testCaseNum; i++) {
            st = new StringTokenizer(br.readLine(), " ");

            int studentNum = Integer.parseInt(st.nextToken());
            scoreArray = new int[studentNum];

            double scoreSum = 0;

            for (int j = 0; j < studentNum; j++) {
                scoreArray[j] = Integer.parseInt(st.nextToken());
                scoreSum += scoreArray[j];
            }

            double avgScore = scoreSum / studentNum;
            double count = 0;

            for (int j = 0; j < studentNum; j++) {
                if (scoreArray[j] > avgScore) {
                    count++;
                }
            }

            System.out.printf("%.3f%%\n", (count/studentNum) * 100);
        }
    }
}