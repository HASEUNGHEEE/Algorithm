from itertools import permutations
def solution(k, dungeons):
    answer = 0
    
    for per in permutations(dungeons, len(dungeons)):
        new_k = k
        cnt = 0
        for i in per:
            if new_k >= i[0]:
                new_k -= i[1]
                cnt += 1
        answer = max(answer, cnt)
    
    return answer