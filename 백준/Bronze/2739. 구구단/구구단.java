import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;

public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int number = Integer.valueOf(br.readLine());
		br.close();

		StringBuilder sb = new StringBuilder();

		for (int i = 1; i <= 9; i++) {
			sb.append(number + " * " + i + " = ").append(number * i).append("\n");
		}
        System.out.println(sb);
	}
}