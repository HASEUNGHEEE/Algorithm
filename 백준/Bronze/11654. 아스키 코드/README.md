# [Bronze V] 아스키 코드 - 11654 

[문제 링크](https://www.acmicpc.net/problem/11654) 

### 성능 요약

메모리: 14232 KB, 시간: 124 ms

### 분류

구현(implementation)

### 문제 설명

<p>알파벳 소문자, 대문자, 숫자 0-9중 하나가 주어졌을 때, 주어진 글자의 아스키 코드값을 출력하는 프로그램을 작성하시오.</p>

### 입력 

 <p>알파벳 소문자, 대문자, 숫자 0-9 중 하나가 첫째 줄에 주어진다.</p>

### 출력 

 <p>입력으로 주어진 글자의 아스키 코드 값을 출력한다.</p>

### 메모
```
/*
Scanner 사용 X
- System.in 은 byte 값으로 문자 한 개만 읽으면서 해당 문자에 대응되는 아스키코드 값을 저장할 수 있다.
- 예외 처리를 꼭 해주어야 한다.
*/
public class Main {
    public static void main(String[] args) throws IOException {
        int input = System.in.read();
        System.out.println(input);
    }
}
```
```   
// Scanner 사용
Scanner sc = new Scanner(System.in);
int input = sc.next().charAt(0);
System.out.println(input);
```
