def solution(n, wires):
    tree = [[] for _ in range(n + 1)]
    for v1, v2 in wires:
        tree[v1].append(v2)
        tree[v2].append(v1)
        
    """
    tree =    [[], [2], [1,3], [2,4], [3]]
    visited = [False, True, True, True, False]
    child =   [0, 3, 2, 1, 0]
    """
        
    visited = [False] * (n + 1)
    child = [0] * (n + 1)
    
    def dfs(node):
        visited[node] = True
        for next in tree[node]:
            if not visited[next]:
                child[node] += dfs(next) + child[next]
                print(node)
                print(child[node])
        return 1
    
    dfs(1)
    answer = n
    
    for c in child:
        answer = min(answer, abs(n - 2*(c+1)))
        
    
    return answer