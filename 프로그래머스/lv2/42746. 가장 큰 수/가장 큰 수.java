import java.util.*;

class Solution {
    public String solution(int[] numbers) {
        String answer = "";
        
        // int[] -> String[]
        String[] strArr = new String[numbers.length];
        for (int i = 0; i < numbers.length; i++) {
            // String.valueOf() 메서드로 숫자를 문자열로 변환
            strArr[i] = String.valueOf(numbers[i]);
        }
        
        // 내림차순 정렬
        Arrays.sort(strArr, new Comparator<String>() {
            @Override
            public int compare(String a, String b) {
                return (b+a).compareTo(a+b);
            }
        });
        
        // 0이 중복될 경우(ex. {0, 0, 0}) -> 배열의 첫번째 값이 0이면 0을 출력
        if (strArr[0].equals("0")) return "0";
        
        // 0이 아니면 문자열을 answer에 더한다
        for (String str : strArr) {
            answer += str;
        }
        
        return answer;
    }
}