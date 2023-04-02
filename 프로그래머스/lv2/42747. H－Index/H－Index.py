def solution(citations):     
    # 리스트 내림차순 정렬 [6, 5, 3, 1, 0]
    citations.sort(reverse=True)
    # [(0,6), (1,5), (2,3), (3,1), (4,0)]
    for idx, citation in enumerate(citations):
        if idx >= citation:
            return idx
    return len(citations)