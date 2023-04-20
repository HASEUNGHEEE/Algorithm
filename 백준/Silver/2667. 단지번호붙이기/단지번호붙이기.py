import sys
input = sys.stdin.readline

n = int(input())
data = [list(input()) for _ in range(n)]

# 상하좌우
dx=[-1,1,0,0]
dy=[0,0,-1,1]
cnt=0
apt=[]

def dfs(x,y):
    global cnt
    data[x][y] = '0'
    cnt+=1
    for i in range(4):
        nx = x + dx[i] 
        ny = y + dy[i]
        if nx < 0 or nx >= n or ny < 0 or ny >= n:
            continue
        if data[nx][ny] == '1':
            dfs(nx,ny)

for i in range(n):
    for j in range(n):
        if data[i][j] == '1':
            cnt= 0
            dfs(i,j)
            apt.append(cnt)

apt.sort()
print(len(apt), *apt, sep = '\n')