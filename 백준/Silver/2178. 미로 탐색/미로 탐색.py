import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
# readline은 맨 뒤에 '\n'까지 입력받으므로 제거
data = [list(map(int, input().rstrip())) for _ in range(n)]

# 상하좌우
dx = [-1, 1 , 0, 0]
dy = [0, 0, -1, 1]

def bfs(x,y):
  queue = deque()
  queue.append((x,y))

  while queue:
    x, y = queue.popleft()
    
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if 0 <= nx < n and 0 <= ny < m and data[nx][ny] == 1:
        queue.append((nx, ny))
        data[nx][ny] = data[x][y] + 1
  return data[n-1][m-1]
  
print(bfs(0,0))