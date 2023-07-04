def solution(sizes):
    '''
    large_num = [] # 60, 70, 60, 80
    small_num = [] # 50, 30, 30, 40
    
    for size in sizes:
        large_num.append(max(size))
        small_num.append(min(size))
        
    large_num.sort(reverse=True)
    small_num.sort(reverse=True)
        
    return large_num[0] * small_num[0]
    '''

    return max(max(size) for size in sizes) * max(min(size) for size in sizes)
