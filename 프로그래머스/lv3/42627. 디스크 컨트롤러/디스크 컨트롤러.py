import heapq as hq
def solution(jobs):
    answer, time, cnt = 0, 0, 0
    leng = len(jobs)
    heap = []
    jobs.sort()
    print(len(jobs))
    print(leng)
    while cnt < len(jobs):
        while len(jobs) > 0:
            if jobs[0][0] <= time:
                hq.heappush(heap, jobs.pop(0)[::-1]) # [소요시간, 요청시점] 순으로 힙에 push
            else:
                break
        if len(heap) > 0:
            job = hq.heappop(heap)
            time += job[0] # 소요시간
            answer += time - job[1]
            cnt += 1
        else:
            time += 1
    
    return answer // leng # 소수점 이하의 수 버림


