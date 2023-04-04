def solution(clothes):
    # 1. 옷을 종류별로 구분한다.
    hash_map = {}
    for clothe, type in clothes:
        hash_map[type] = hash_map.get(type, 0) + 1
    """
    HashMap.get(type, 0)
    Key(type)에 해당하는 Value가 있으면 가져오고,
    없을 경우 0을 Default로 하여 사용하겠다는 의미의 함수
    """
    
    # 2. 입지 않는 경우를 추가하여 모든 조합을 계산한다.
    answer = 1
    for type in hash_map:
        answer *= hash_map[type] + 1
    """
    ex) headgear : 2 => 총 3가지 경우의 수
    1) 1번 headgear를 쓴다
    2) 2번 headgear를 쓴다
    3) 아무 headgear도 쓰지 않는다
    """
    
    # 3. 아무 종류의 옷도 입지 않는 경우를 제외한다.
    return answer - 1