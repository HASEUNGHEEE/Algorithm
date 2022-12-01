import java.util.*;

public class Solution {
    public Stack solution(int[] arr) {
        Stack<Integer> stack = new Stack<>();
        for(int currentNumber : arr) {
            if(stack.isEmpty() || stack.peek() != currentNumber) {
                stack.add(currentNumber);
            }
        }
        return stack;
    }
}