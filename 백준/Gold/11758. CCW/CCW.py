def ccw(x1, y1, x2, y2, x3, y3):
    # CCW 계산식
    value = (x2-x1) * (y3-y1) - (y2-y1) * (x3-x1)
    if value > 0: # 반시계 방향
        return 1
    elif value < 0: # 시계 방향
        return -1
    else: return 0 # 일직선

if __name__ == '__main__':
    # 입력 처리
    x1, y1 = map(int, input().split())
    x2, y2 = map(int, input().split())
    x3, y3 = map(int, input().split())
    
    # 출력 처리
    print(ccw(x1, y1, x2, y2, x3, y3))