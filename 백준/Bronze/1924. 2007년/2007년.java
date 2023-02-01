import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        
        int month = Integer.parseInt(st.nextToken());
        int day = Integer.parseInt(st.nextToken());
        br.close();
        
        int[] daysInMonth = {31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};
        String[] dayOfWeek = {"SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"};
        
        int totalDays = day;
        for (int i = 0; i < month - 1; i++) {
            totalDays += daysInMonth[i];
        }
        
        System.out.println(dayOfWeek[totalDays % 7]);
    }
}