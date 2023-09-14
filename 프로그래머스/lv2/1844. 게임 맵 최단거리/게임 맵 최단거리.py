from collections import deque
def solution(maps):
    # 상하좌우
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    n, m = len(maps), len(maps[0])
    q = deque()
    q. append((0, 0))
    
    while q:
        x, y = q.popleft()
        for i in range(4): # 4방향 탐색
            nx, ny = x + dx[i], y + dy[i]
            # 범위 내에 있고, 벽이 아닐 때(이동 가능한 1일 때)
            if 0 <= nx < n and 0 <= ny < m and maps[nx][ny] == 1:
                maps[nx][ny] = maps[x][y] + 1 # 방문 처리 + 이동하는 칸의 개수 저장
                q.append((nx, ny))
                
    if maps[n-1][m-1] == 1: 
        return -1
    else:
        return maps[n-1][m-1]