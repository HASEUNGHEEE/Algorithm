import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int number = Integer.parseInt(br.readLine());
        br.close();
        
        StringBuilder sb = new StringBuilder();
        
        while (number > 0) {
            sb.append(number + "\n");
            number--;
        }
        System.out.println(sb); 
    }
}
