def solution(n):
    memo = [0, 1]
    for i in range(2, n+1):
        memo.append(memo[-1] + memo[-2])
    return memo[-1] % 1234567

"""
재귀 설정으로 해결

import sys
sys.setrecursionlimit(10**6)

memo = {0:0, 1:1, 2:1}
def fibonacci(n):
    if n in memo:
        return memo[n]
    else:
        temp = fibonacci(n-1) + fibonacci(n-2)
        memo[n] = temp
        return temp

def solution(n):
    return fibonacci(n) % 1234567
"""