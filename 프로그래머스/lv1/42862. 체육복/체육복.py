def solution(n, lost, reserve):
    answer = 0
    
    # reserve와 lost에 동일한 값 있지 않도록 함
    lost_set = set(lost) - set(reserve)
    reserve_set = set(reserve) - set(lost)
    
    for i in reserve_set:
        if (i-1) in lost_set:
            lost_set.remove(i-1)
        elif (i+1) in lost_set:
            lost_set.remove(i+1)
            
    return n - len(lost_set)