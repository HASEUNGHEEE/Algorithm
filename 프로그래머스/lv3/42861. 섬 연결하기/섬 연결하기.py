import heapq as hq
from collections import defaultdict

def solution(n, costs):
    answer = 0
    
    visited = [False for _ in range(n)] # 방문 여부 확인 (미방문 상태)
    islands = defaultdict(list)
    min_cost = []
    
    for i in costs: # 연결 가능한 섬과 비용 입력
        islands[i[0]].append([i[1], i[2]])
        islands[i[1]].append([i[0], i[2]])
    
    # 0번째 섬에서 이동할 수 있는 섬 확인하기
    visited[0] = True
    for i in islands[0]:
        hq.heappush(min_cost, [i[1], i[0]]) # 비용 기준으로 push
    while min_cost:
        cost, dest = hq.heappop(min_cost)
        if not visited[dest]:
            visited[dest] = True
            answer += cost
            for i in islands[dest]:
                hq.heappush(min_cost, [i[1], i[0]]) # 비용 기준으로 push
    
    return answer
