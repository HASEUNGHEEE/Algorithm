n, m = map(int, input().split())
board = [input() for _ in range(n)]
count = []

# 0번 인덱스 'B', 1번 인덱스 'W' -> 흰색 시작으로 초기 설정
color = ['W', 'B']

for i in range(n-7):
    for j in range(m-7):
        W, B = 0, 0 # W를 칠할 개수, B를 칠할 개수
        for x in range(i, i+8):
            for y in range(j, j+8):
              # (x+y) % 2 == 0 -> 인덱스 합이 짝수인 경우면 초기 색과 같아야 한다 -> W
              # (x+y) % 2 == 1 -> 인덱스 합이 홀수인 경우면 초기 색과 달라야 한다 -> B
              # 흰색 시작일 때 틀린 경우
              if board[x][y] != color[(x+y) % 2]:
                W += 1
                
              # 검은색 시작일 때 틀린 경우
              else:
                B += 1
        count.append(min(W, B))

print(min(count))