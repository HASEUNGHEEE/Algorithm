def solution(participant, completion):
    hashDict = {}
    sumHash = 0
    
    # 1. Hash : Participant의 dictionary를 만든다
    # 2. Participant의 sum(hash)를 구한다
    for part in participant:
        hashDict[hash(part)] = part
        sumHash += hash(part)
    
    # 3. Completion의 sum(hash)를 뺀다
    for comp in completion:
        sumHash -= hash(comp)
        
    return hashDict[sumHash]