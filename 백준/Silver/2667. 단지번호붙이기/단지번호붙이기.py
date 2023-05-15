import sys
input = sys.stdin.readline

# 상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# dfs
def dfs(x, y):
  global cnt
  graph[x][y] = 0
  cnt += 1
  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]
    if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] == 1:
      dfs(nx, ny)

# 입력
n = int(input())
graph = [list(map(int, input().rstrip())) for _ in range(n)]
# 단지내 집의 수
apt = []
for i in range(n):
  for j in range(n):
    if graph[i][j] == 1:
      cnt = 0
      dfs(i, j)
      apt.append(cnt)
  
# 출력
apt.sort()
print(len(apt))
for x in apt:
  print(x)