from collections import deque
def solution(n, computers):
    #     0  1  2
    # 0 [[1, 1, 0], 
    # 1  [1, 1, 0], 
    # 2  [0, 0, 1]]
    
    #     0  1  2
    # 0 [[1, 1, 0], 
    # 1  [1, 1, 1], 
    # 2  [0, 1, 1]]
    
    answer = 0
    visited = [0] * n
    
    def dfs(i):
        visited[i] = 1
        for j in range(n):
            if computers[i][j] == 1 and not visited[j]:
                dfs(j)
    
    for i in range(n):
        if not visited[i]:
            dfs(i)
            answer += 1
    
    return answer