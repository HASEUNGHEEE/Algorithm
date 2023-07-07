import math
from itertools import permutations
# 소수 판별 함수
def is_prime_number(x):
    if x < 2:
        return False
    # 2부터 x의 제곱근까지의 모든 수를 확인
    for i in range(2, int(math.sqrt(x))+1): 
        # x가 해당 수로 나누어 떨어지면 소수 아님
        if x % i == 0: 
            return False
    return True

def solution(numbers):
    answer = []
    for i in range(1, len(numbers) + 1):
        per = list(permutations(numbers, i))
        for j in range(len(per)):
            num = int(''.join(per[j]))
            if is_prime_number(num):
                answer.append(num)
    
    return len(set(answer))