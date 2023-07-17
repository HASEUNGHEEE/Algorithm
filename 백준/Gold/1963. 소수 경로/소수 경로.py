import sys, math
from collections import deque

"""
소수 찾는 방법
1. 소수인 값들을 찾아서 소수판별 테이블에 더하는 방법

def is_prime(x):
  if x < 2: return False
  for i in range(2, int(x ** 1/2)+1): # 제곱근(x ** 1/2 == math.sqrt(x))까지
    if x % i == 0: return False
  return True

prime = [False]
for i in range(1, 10000):
  prime.append(is_prime(i))
  
2. 소수가 아닌 값들을 찾아서 소수판별 테이블에서 제거하는 방법 - 에라토스테네스의 체
"""
# 에라토스테네스의 체
def prime_number_sieve():
  for i in range(2, 100): # 10000의 제곱근(100)
    # 소수일 경우
    if prime[i] == True:
      # 소수의 배수를 제거한다
      for j in range(i*2, 10000, i): 
        prime[j] = False

prime = [True for _ in range(10000)]
prime_number_sieve()

# bfs
def bfs():
  q = deque()
  q.append([start, 0])
  visited[start] = 1
  
  while q:
    cur, cnt = q.popleft()
    cur_str = str(cur)
    # 최종 소수에 도달하면 cnt 반환
    if cur == end: 
      return cnt
    # 각 자리수(4자리)마다
    for i in range(4):
      # 0~9까지 숫자 넣어서 소수 판별
      for j in range(10):
        temp = int(cur_str[:i] + str(j) + cur_str[i+1:])
        # 소수이고, 방문하지 않았으며, 4자리 수일 때
        if prime[temp] and not visited[temp] and temp >= 1000:
          visited[temp] = 1
          q.append([temp, cnt+1])
          

# 입력
input = sys.stdin.readline
t = int(input())

for _ in range(t):
  start, end = map(int, input().split())
  visited = [0 for _ in range(10000)]
  total = bfs()
  # 출력
  print(total if total != None else "Impossible")