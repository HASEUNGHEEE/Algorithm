def solution(routes):
    answer = 0
    entry_point = -30001
    camera_cnt = 0
    
    # 진출 지점 기준으로 2차원 리스트 오름차순 정렬
    routes.sort(key=lambda x: x[1]) 
    
    # 2차원 리스트 반복하며 값(1차원 리스트)에 접근
    for route in routes:
        if route[0] > entry_point:
            camera_cnt += 1
            entry_point = route[1]
    
    return camera_cnt