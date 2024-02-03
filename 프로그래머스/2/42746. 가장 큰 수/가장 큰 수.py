def solution(numbers):
    # string형 list로 변환
    str_numbers = list(map(str, numbers))
    # 문자열 타입으로 정렬
    str_numbers.sort(key = lambda x: x*3, reverse=True)
    # '000', '00' 등을 '0'으로 반환하기 위해 join하여 int형 -> 문자열
    return str(int(''.join(str_numbers)))

print(solution([6, 10, 2]))          
print(solution([3, 30, 34, 5, 9]))    
print(solution([0,0,0,0]))