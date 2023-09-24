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