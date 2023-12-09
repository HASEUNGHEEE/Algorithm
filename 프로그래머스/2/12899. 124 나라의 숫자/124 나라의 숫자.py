def solution(n):
    answer = ''
    nums = ['1', '2', '4']
    
    while n:
        n -= 1 
        answer = nums[n % 3] + answer
        n //= 3
    return answer
