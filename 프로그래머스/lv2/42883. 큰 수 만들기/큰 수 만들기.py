def solution(number, k):
    
    # 1차 시도 코드: 조합 -> 시간초과
    # return max(list([''.join(i) for i in combinations(number, len(number)-k)]))
    
    # 2차 시도 코드: 스택
    stack = []
    
    for num in number:
        while stack and stack[-1] < num and k > 0:
            stack.pop()
            k -= 1
        stack.append(num)
        
    stack = stack[:-k] if k != 0 else stack
        
    return ''.join(stack)