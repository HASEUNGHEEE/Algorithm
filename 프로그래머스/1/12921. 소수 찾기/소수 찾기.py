def solution(n):
    answer = 0
    # 애라토스테네스의 체
    # N이 1,000,000 이내로 주어지는 경우 활용! (이론상 400만번 정도 연산이고 메모리도 충분함)
    arr = [True for _ in range(n+1)] # 모두 소수(True)로 초기화
    
    for i in range(2, int(n**0.5)+1): # 2부터 n의 제곱근까지의 모든 수를 확인
        if arr[i] == True: # i가 소수인 경우
            # i를 제외한 i의 모든 배수를 걸러낸다
            j = 2
            while i*j <= n:
                arr[i*j] = False
                j += 1
    
    # 남아있는 소수 개수 세기
    for i in range(2, n+1):
        if arr[i] == True:
            answer += 1
                     
    return answer