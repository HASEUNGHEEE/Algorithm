from collections import deque
def solution(people, limit):
    answer = 0
    # people 리스트 오름차순 정렬 [50, 50, 70, 80]
    people = deque(sorted(people))
    
    while people:
        answer += 1
        person = people.pop() # 몸무게가 가장 큰 사람 구출
        if people and people[0] <= limit - person: # 몸무게 가장 작은 사람과 같이 구출할 수 있다면
            people.popleft()
    return answer
