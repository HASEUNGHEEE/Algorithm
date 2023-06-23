import math

def solution(progresses, speeds):
    # 남은 작업을 수행하기 위해 필요한 시간(일)
    last_work = []
    for i in range(len(progresses)):
        last_work.append(math.ceil((100 - progresses[i]) / speeds[i]))
        
    # 배포 가능한 기능 개수
    day = 0
    # 리턴값 담을 리스트
    answer = []
    
    for i in range(1, len(last_work)):
        if last_work[i] > last_work[day]:
            answer.append(i - day)
            day = i
    answer.append(len(last_work) - day)
    return answer




