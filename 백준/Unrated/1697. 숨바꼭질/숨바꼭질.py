import sys
from collections import deque

def bfs(v):
  dq = deque([v])
  while dq:
    v = dq.popleft()
    if v == k:
      return visited[v]
    for i in (v-1, v+1, 2*v):
      if 0 <= i <= 100000 and not visited[i]:
        visited[i] = visited[v] + 1
        dq.append(i)

# 파이썬 재귀의 최대 깊이를 변경하여 런타임 에러 방지한다.
sys.setrecursionlimit(10 ** 7)
n, k = map(int, sys.stdin.readline().split())

visited = [0 for _ in range(100001)]
print(bfs(n))