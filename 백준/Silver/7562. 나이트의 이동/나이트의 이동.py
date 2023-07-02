import sys
from collections import deque

# 8방향
dx = [-1, 1, 2, 2, 1, -1, -2, -2]
dy = [-2, -2, -1, 1, 2, 2, 1, -1]

# bfs 함수
def bfs(x1, y1, x2, y2):
    q = deque()
    q.append([x1, y1])
    graph[x1][y1] = 1
    while q:
        x1, y1 = q.popleft()
        if x1 == x2 and y1 == y2:
            return graph[x1][y1] - 1
        for i in range(8):
            nx = x1 + dx[i]
            ny = y1 + dy[i]
            if 0 <= nx < l and 0 <= ny < l and graph[nx][ny] == 0:
                q.append([nx, ny])
                graph[nx][ny] = graph[x1][y1] + 1

# 입력
input = sys.stdin.readline
tc = int(input())
while tc:
    l = int(input())
    graph = [[0]*l for _ in range(l)]
    
    x1, y1 = map(int, input().split())
    x2, y2 = map(int, input().split())
    # 현재 위치와 목적지 같으면 0 출력
    if x1 == x2 and y1 == y2:
        print(0)
        tc -= 1
        continue
    
    print(bfs(x1, y1, x2, y2))
    tc -= 1