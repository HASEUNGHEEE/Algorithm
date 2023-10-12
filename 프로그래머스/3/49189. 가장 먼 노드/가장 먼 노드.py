from collections import deque
def solution(n, edge):
    answer = 0
    
    vertex = [[] for _ in range(n+1)] # 노드 관계 정리
    step = [0] * (n+1) # step 판단하기 위한 리스트
    for a, b in edge:
        vertex[a].append(b)
        vertex[b].append(a)
    
    # 1번 노드부터 시작
    q = deque([1])
    step[1] = 1
    while q:
        now = q.popleft()
        for i in vertex[now]:
            # 방문한 적 없다면 큐에 추가하고 step 하나 더해서 갱신
            if step[i] == 0:
                q.append(i)
                step[i] = step[now] + 1
    
    for i in step:
        if i == max(step):
            answer += 1
            
    return answer