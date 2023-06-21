answer = 0

def dfs(numbers, target, index, result):
    global answer
    
    # 1. 탈출 조건
    if index == len(numbers):
        if result == target: 
            answer += 1
            return
            
        else: return
            
    
    # 2. 수행 동작
    dfs(numbers, target, index + 1, result + numbers[index])
    dfs(numbers, target, index + 1, result - numbers[index])
    

def solution(numbers, target):
    global answer
    dfs(numbers, target, 0, 0)
    return answer
    