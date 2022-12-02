import java.util.Stack;
import java.util.EmptyStackException;

class Solution {
    boolean solution(String s) {
        Stack<Character> stack = new Stack<>();
        
        try {
            for (char currentCharacter : s.toCharArray()) {
                if (!stack.isEmpty() && currentCharacter == ')') {
                    stack.pop();
                    continue;
                }
                stack.push(currentCharacter);
            }
            if (stack.isEmpty()) {
                return true;
            } else {
                return false;
            }
        } catch (EmptyStackException e) {
            return true;
        }
    }
}