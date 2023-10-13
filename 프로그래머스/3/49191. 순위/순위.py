from collections import defaultdict
def solution(n, results):
    answer = 0
    winners, losers = defaultdict(set), defaultdict(set)
    
    for w,l in results:
        winners[w].add(l)
        losers[l].add(w)
        
    for i in range(1, n+1):
        for win in losers[i]: winners[win].update(winners[i])
        for lose in winners[i]: losers[lose].update(losers[i])
    
    for i in range(1, n+1):
        if len(winners[i]) + len(losers[i]) == n-1: answer += 1
        
    return answer