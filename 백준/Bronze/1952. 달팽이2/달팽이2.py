import sys
input = sys.stdin.readline

m, n = map(int, input().split())
board = [[0]*n for _ in range(m)]
ch = [[0]*n for _ in range(m)]
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

# 시작값
x, y, cnt, dr = 0, 0, 1, 0
board[x][y] = cnt
cnt += 1
turn_cnt = 0 # 방향 전환 횟수

while cnt <= m*n:
    nx= x + dx[dr]
    ny = y + dy[dr]
    # 좌표 범위 내에 있고, board 값이 0인 경우에 이동한다.
    if 0 <= nx < m and 0 <= ny < n and board[nx][ny] == 0:
      x, y = nx, ny
      board[x][y] = cnt
      cnt += 1 # cnt 하나 증가
    # 그렇지 않으면 방향을 전환한다.
    else:
      dr = (dr+1) % 4
      turn_cnt += 1

print(turn_cnt)