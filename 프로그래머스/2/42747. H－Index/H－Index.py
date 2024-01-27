def solution(citations):     
    # 리스트 내림차순 정렬 [6, 5, 3, 1, 0]
    citations.sort(reverse=True)
    # [(0,6), (1,5), (2,3), (3,1), (4,0)]
    for idx, citation in enumerate(citations):
        if idx >= citation:
            return idx
    return len(citations) # idx+1 도 가능
    
# return idx만 하면 idx보다 큰 citation이 있을 때 None이 출력된다
print(solution([5, 5, 5, 5, 5])) #None 출력
print(solution([5, 10, 20, 30, 40])) #None 출력
print(solution([88, 89])) #None 출력

   
