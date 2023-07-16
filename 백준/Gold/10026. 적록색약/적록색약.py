from collections import deque

# 상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

# dfs 함수
def bfs(x, y):
  q = deque()
  q.append([x, y])
  visited[x][y] = 1

  while q:
    x, y = q.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      # graph 범위를 벗어나지 않고, 현재 색상과 다음에 방문할 색상이 같고, 방문하지 않은 경우
      if 0 <= nx < n and 0 <= ny < n and graph[x][y] == graph[nx][ny] and not visited[nx][ny]:
        visited[nx][ny] = 1
        q.append([nx, ny])
        
# 입력
n = int(input())
graph = [list(input()) for _ in range(n)]

# 적록색약 아닌 경우
color_cnt = 0
visited = [[0]*n for _ in range(n)]
for i in range(n):
  for j in range(n):
    if not visited[i][j]:
      bfs(i, j)
      color_cnt += 1

# 적록색약인 경우
for i in range(n):
  for j in range(n):
    # 색상 차이를 느끼지 못하므로 같은 색으로 변경한다
    if graph[i][j] == 'G':
      graph[i][j] = 'R'
      
color_weakness_cnt = 0
visited = [[0]*n for _ in range(n)]
for i in range(n):
  for j in range(n):
    if not visited[i][j]:
      bfs(i, j)
      color_weakness_cnt += 1


print(color_cnt, color_weakness_cnt)