import sys
input = sys.stdin.readline

# 상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
  global result
  q = set([(x, y, graph[x][y])])
  while q:
    x, y, answer = q.pop()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if 0 <= nx < r and 0 <= ny < c and graph[nx][ny] not in answer:
        q.add((nx, ny, answer + graph[nx][ny]))
        result = max(result, len(answer)+1)


r, c = map(int, input().split())
graph = [list(input()) for _ in range(r)]
result = 1
bfs(0, 0)
print(result)