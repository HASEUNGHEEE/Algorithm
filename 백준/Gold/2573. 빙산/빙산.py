import sys
from collections import deque
input = sys.stdin.readline

def bfs(si, sj, v):
  q = deque()
  q.append((si, sj))
  v[si][sj] = 1

  while q:
    ci, cj = q.popleft()
    # 네 방향, 미방문, 0보다 큰 경우
    for di, dj in ((-1,0), (1,0), (0,-1), (0,1)):
      ni, nj = ci+di, cj+dj
      if v[ni][nj] == 0 and arr[ni][nj] > 0:
        q.append((ni, nj))
        v[ni][nj] = 1


# 1~900000년, 전체 순회하면서 반복 작업
# 900000: 최악의 경우 고려한 값
def solve():
  for year in range(1, 900000):
    # 1. 네 방향 0의 개수 카운트
    sub_arr = [[0]*m for _ in range(n)]
    for i in range(1, n-1): # 외곽이 모두 0이므로 제외
      for j in range(1, m-1):
        if arr[i][j] == 0: continue
        for di, dj in ((-1,0), (1,0), (0,-1), (0,1)):
          ni, nj = i+di, j+dj
          if arr[ni][nj] == 0:
            sub_arr[i][j] += 1
    # 2. 높이 낮추기
    for i in range(1, n-1): # 외곽이 모두 0이므로 제외
      for j in range(1, m-1):
        if sub_arr[i][j] > 0:
          arr[i][j] = max(0, arr[i][j] - sub_arr[i][j])
    # 3. 빙산 덩어리 개수 카운트
    v = [[0]*m for _ in range(n)]
    cnt = 0
    for i in range(1, n-1): # 외곽이 모두 0이므로 제외
      for j in range(1, m-1):
        if v[i][j] == 0 and arr[i][j] > 0:
          bfs(i, j, v)
          cnt += 1
          if cnt > 1: return year
    if cnt == 0: return 0
  


# 입력
n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

# 출력
answer = solve()
print(answer)