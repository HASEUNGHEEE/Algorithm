def solution(n, computers):
    network_cnt = 0 # 네트워크 개수
    visited = [0] * n # 방문 처리용 리스트
    
    def dfs(i):
        visited[i] = 1
        for j in range(n):
            if computers[i][j] == 1 and not visited[j]:
                dfs(j)
    
    # network
    for i in range(n):
        if not visited[i]:
            dfs(i)
            network_cnt += 1
            
    return network_cnt


