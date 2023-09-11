# import sys
# input = sys.stdin.readline

# # 입력
# n = int(input())
# m = int(input())
# board = [[0]*n for _ in range(n)]

# # 방향 (하 -> 우 -> 상 -> 좌)
# dx = [1, 0, -1, 0]
# dy = [0, 1, 0, -1]

# # 시작값
# x, y, cnt, dir = 0, 0, n**2, 0
# board[x][y] = cnt
# cnt -= 1
# nx, ny = 0, 0

# while cnt > 0:
#   nx, ny = x + dx[dir], y + dy[dir]
#   # 좌표 범위 내에 있고, board 값이 0인 경우에 이동한다.
#   if 0 <= nx < n and 0 <= ny < n and board[nx][ny] == 0:
#     x, y = nx, ny
#     board[x][y] = cnt
#     if cnt == m:
#       answer = [x+1, y+1] # m의 좌표 저장
#     cnt -= 1 # cnt 하나 감소
    
#   # 그렇지 않으면 방향을 전환한다.
#   else:
#     dir = (dir+1) % 4

# # unpacking
# for line in board:
#   print(*line)
# print(*answer)

import sys
input = sys.stdin.readline

def make_snail(n):
  global snail_x, snail_y
  # 방향 (하 -> 우 -> 상 -> 좌)
  dx = [1, 0, -1, 0]
  dy = [0, 1, 0, -1]
  
  # 시작값
  x, y, cnt, dr = 0, 0, n**2, 0
  board[x][y] = cnt
  cnt -= 1
  
  while cnt > 0:
      nx= x + dx[dr]
      ny = y + dy[dr]
      # 좌표 범위 내에 있고, board 값이 0인 경우에 이동한다.
      if 0 <= nx < n and 0 <= ny < n and board[nx][ny] == 0:
        x, y = nx, ny
        board[x][y] = cnt
        if cnt == m:
          snail_x, snail_y = x, y # m의 좌표 저장
        
        cnt -= 1 # cnt 하나 감소
      # 그렇지 않으면 방향을 전환한다.
      else:
          dr = (dr+1) % 4
  return board

# 입력
n = int(input())
m = int(input())
board = [[0]*n for _ in range(n)]
snail_x, snail_y = 0, 0
board = make_snail(n)

# unpacking
for line in board:
    print(*line)
print(snail_x+1, snail_y+1)