import sys
# 파이썬 재귀의 최대 깊이를 변경하여 런타임 에러 방지한다.
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

n, m = map(int, input().split())

graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)

for _ in range(m):
  x, y = map(int, input().split())
  graph[x].append(y)
  graph[y].append(x)

def dfs(z):
  visited[z] = True
  for node in graph[z]:
    if not visited[node]:
      dfs(node)

count = 0
for i in range(1, n+1):
  if not visited[i]: # if visited[i] == False
    count += 1
    dfs(i)

print(count)