import sys
input = sys.stdin.readline

# 입력
n, m = map(int, input().split())
map = [list(map(int, input().split())) for _ in range(n)]

top = n * m

left = 0
for i in range(n):
    for j in range(m):
        if j == 0:
            left += map[i][j]
        else:
            if map[i][j-1] < map[i][j]:
                left += map[i][j] - map[i][j-1]

front = 0
for j in range(m):
    for i in range(n):
        if i == 0:
            front += map[i][j]
        else:
            if map[i-1][j] < map[i][j]:
                front += map[i][j] - map[i-1][j]
        
answer = 2 * (top + left + front)
print(answer)