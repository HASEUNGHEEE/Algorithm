import sys

def solution(n, times):
    times = sorted(times)
    return binarysearch(times, n , times[-1])


def binarysearch(times, n, max_val):
    left = 1 
    right = max_val * n
    mid = 0
    answer = sys.maxsize
    while left <= right:
        mid = (left + right) // 2
        if passed(times, n, mid):
            answer = mid if answer > mid else answer
            right = mid - 1
        else:
            left = mid + 1
    
    return answer

# mid 시간동안 n명이 입국 심사를 받을 수 있는지 확인하는 함수
def passed(times, n, mid):
    amount = 0
    for i in range(len(times)):
        amount += mid // times[i]
        
    if amount >= n: return True
    else: return False
    
    



