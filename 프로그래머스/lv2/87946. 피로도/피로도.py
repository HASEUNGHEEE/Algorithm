from itertools import permutations
def solution(k, dungeons):
    count = []
    
    for per in permutations(dungeons, len(dungeons)):
        new_k = k
        cnt = 0
        for i in per:
            if new_k >= i[0]:
                new_k -= i[1]
                cnt += 1
        count.append(cnt)
    
    return max(count)