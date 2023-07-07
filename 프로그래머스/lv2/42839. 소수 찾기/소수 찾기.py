import math
from itertools import permutations
"""
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

"""

# 같은 로직, 더욱 간결한 코드
def solution(numbers):
    num_set = set()
    
    for i in range(len(numbers)):
        # 1. list(n)의 원소들 중에서 i+1 개의 원소를 뽑아 순열을 만들고
        # 2. join하여 int화
        # 3. set에 담아 num_set에 합친다(|= 병합 업데이트 연산자)
        num_set |= set(map(int, map("".join, permutations(list(numbers), i+1))))
    
    num_set -= set(range(0,2)) # 0과 1은 set에서 제거
    
    for i in range(2, int(max(num_set) ** 0.5) + 1): # 2부터 set 최댓값의 제곱근까지의 모든 수를 확인하면서
        num_set -= set(range(i * 2, max(num_set) + 1, i)) # set에서 배수들을 다 제거한다
        
    return len(num_set)