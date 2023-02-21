import java.util.Arrays;

class Solution {
    public int[] solution(int[] array, int[][] commands) {
        int[] answer = new int[commands.length];
        
        for (int i = 0; i < commands.length; i++) {
            // 정수 배열 인덱스 범위만큼 자르기 (copyOfRange)
            int[] splitArray = Arrays.copyOfRange(array, commands[i][0]-1, commands[i][1]);
            // 오름차순 정렬
            Arrays.sort(splitArray);
            // answer 배열에 담기
            answer[i] = splitArray[commands[i][2]-1];
        }
        return answer;
    }
}