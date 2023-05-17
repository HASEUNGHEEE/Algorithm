import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

# 상, 하, 좌, 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y, height):
  check[x][y] = 1
  
  for  i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]
    if 0 <= nx < n and 0 <= ny < n and check[nx][ny] == 0 and graph[nx][ny] > height:
      dfs(nx, ny, height)
  

# 입력
n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

# 0~99까지 탐색
res = 0
for height in range(100):
  check = [[0]*n for _ in range(n)]
  cnt = 0
  for i in range(n):
    for j in range(n):
      if check[i][j] == 0 and graph[i][j] > height:
        cnt += 1
        # 현재 height보다 값이 클 때만 탐색해야 한다
        dfs(i, j, height)
  res = max(res, cnt)
  # grapph[i][j] <= height이라서 if문 그냥 통과할 때
  if cnt == 0:
    break

print(res)