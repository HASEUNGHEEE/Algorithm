def solution(n):
    # n을 2진수로 변환했을 때의 1의 갯수
    cnt = bin(n).count('1')
    
    # n보다 크고 1,000,000 이하의 자연수 중에서
    for m in range(n+1, 1000001):
        # 2진수로 변환했을 때의 1의 갯수가 cnt와 같은 수
        if bin(m).count('1') == cnt: return m