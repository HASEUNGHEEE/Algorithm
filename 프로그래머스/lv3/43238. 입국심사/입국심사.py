"""
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
    
"""

# function 분리하지 않고도 solution 함수 안에서 다 해결할 수 있다.
# 주석 안에 있는 코드와 같은 로직

def solution(n, times):
    answer = 0
    times = sorted(times)
    left, right, mid = 1, times[-1] * n, 0

    while left <= right:
        mid = (left + right) // 2
        amount = 0
        for time in times:
            amount += mid // time

        if amount >= n:
            right = mid - 1
        else:
            left = mid + 1
    
    answer = left
    return answer




    
    