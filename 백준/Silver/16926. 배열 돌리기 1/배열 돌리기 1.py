import sys
from collections import deque
input = sys.stdin.readline

# 입력
n, m, r = map(int, input().split())
graph = [list(input().split()) for _ in range(n)]
answer = [[0]*m for _ in range(n)]
q = deque()

for i in range(min(n, m) // 2):
  # graph를 1차원 배열로 변환하여 q에 담기
  q.clear()
  q.extend(graph[i][i:m-i]) # 위
  q.extend([row[m-i-1] for row in graph[i+1:n-i-1]]) # 오른쪽
  q.extend(graph[n-i-1][i:m-i][::-1]) # 아래
  q.extend(row[i] for row in graph[i+1:n-i-1][::-1]) # 왼쪽
  q.rotate(-r)

  # q의 값들을 2차원 배열로 변환하여 answer에 담기
  for j in range(i, m-i):
    answer[i][j] = q.popleft()
  for j in range(i+1, n-i-1):
    answer[j][m-i-1] = q.popleft()
  for j in range(m-i-1, i-1, -1):
    answer[n-i-1][j] = q.popleft()
  for j in range(n-i-2, i, -1):
    answer[j][i] = q.popleft()

# 출력
for line in answer:
  print(" ".join(line))