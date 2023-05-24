import sys
from collections import deque
input = sys.stdin.readline

def bfs():
    q = deque()
    q.append([start[0], start[1]])
    while q:
        x, y = q.popleft()
        if abs(x - end[0]) + abs(y - end[1]) <= 1000:
            print("happy")
            return
        for i in range(n):
            if not visited[i]:
                nx, ny = location[i]
                if abs(x - nx) + abs(y - ny) <= 1000:
                    q.append([nx, ny])
                    visited[i] = 1
    print("sad")
    return

t = int(input())
for i in range(t):
    n = int(input())
    start = [int(x) for x in input().split()]
    location = []
    for j in range(n):
        x, y = map(int, input().split())
        location.append([x, y])
    end = [int(x) for x in input().split()]
    visited = [0] * n
    bfs()