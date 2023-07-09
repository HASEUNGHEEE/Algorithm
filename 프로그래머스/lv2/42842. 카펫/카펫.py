from collections import deque

def solution(brown, yellow):
    answer = []
    
    # 1. yellow 약수 구하기
    divisor = []
    for i in range(1, yellow//2 + 1):
        if yellow % i == 0: divisor.append(i)
    divisor.append(yellow)
    
    
    # 2. 가로: 약수쌍 중 큰 값, 세로: 약수쌍 중 작은 값
    for i in range(len(divisor)):
        height = divisor[i]
        width = divisor.pop()
        
        if (width + 2) * (height + 2) - yellow == brown:
            answer.append(width + 2)
            answer.append(height + 2)
            break
        
        i += 1
        
    return answer