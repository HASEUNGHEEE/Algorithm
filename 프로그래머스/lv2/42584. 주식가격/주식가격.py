def solution(prices):
    answer = [i for i in range(len(prices)-1, -1, -1)] # [4, 3, 2, 1, 0]
    stack = [0]
    
    for i in range(1, len(prices)):
    
        while stack and prices[stack[-1]] > prices[i]:
            idx = stack.pop()
            answer[idx] = i - idx
        stack.append(i)
    
    return answer