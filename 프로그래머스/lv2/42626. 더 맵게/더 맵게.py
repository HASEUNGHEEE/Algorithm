import heapq as hq

def solution(scoville, K):

    hq.heapify(scoville)
    answer = 0
    while True:
        first = hq.heappop(scoville)
        if first >= K:
            break
        if len(scoville) == 0:
            return -1
        second = hq.heappop(scoville)
        hq.heappush(scoville, first + second*2)
        answer += 1  

    return answer


"""
import heapq
def solution(scoville, K):
    answer = 0
    
    # scoville 리스트를 heap으로 변환
    heapq.heapify(scoville)
    
    while len(scoville) >= 2:
        # heap의 가장 작은 원소 제거 및 리턴
        first_min = heapq.heappop(scoville)
        if first_min >= K:
            return answer
        else:
            # heap의 두번쨰로 작은 원소 제거 및 리턴
            second_min = heapq.heappop(scoville)
            # 새로운 음식의 스코빌 지수
            heapq.heappush(scoville, first_min + (second_min * 2))
            answer += 1
    
    if scoville[0] > K:
        return answer
    else:
        return -1
"""
