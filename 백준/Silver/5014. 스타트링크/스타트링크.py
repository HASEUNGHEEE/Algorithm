import sys
from collections import deque
input = sys.stdin.readline

def bfs(start, end):
  q = deque()
  v = [0] * (f+1)
  q.append(start)
  v[start] = 1

  while q:
    now = q.popleft()
    if now == end:
      return v[now] - 1
      
    for next in (now + u, now - d):
      if 1 <= next <= f and v[next] == 0:
        q.append(next)
        v[next] = v[now] + 1
  
  # 목적지 찾을 수 없을 때
  return "use the stairs"

f, s, g, u, d = map(int, input().split())

# s층에서 g층으로 가기 위해 눌러야 하는 버튼의 수 최솟값 출력
print(bfs(s,g))