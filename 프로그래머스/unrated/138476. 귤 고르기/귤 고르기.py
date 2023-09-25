def solution(k, tangerine):
    answer = 0
    count = {}
    for i in tangerine:
        if count.get(i) == None: count[i] = 1
        else: count[i] += 1
        
    # 딕셔너리 value 기준으로 내림차순 정렬    
    sorted_count = sorted(count.values(), reverse=True)
    
    for val in sorted_count:
        k -= val
        answer += 1
        if k <= 0: return answer
            