import heapq as hq

def solution(operations):
    min_heap, max_heap = [], [] # 최소힙, 최대힙
    for operation in operations:
        operator, value = operation.split()
        val = int(value)
        
        # 삽입 명렁어
        if operator == "I":
            hq.heappush(min_heap, val)
            hq.heappush(max_heap, -val)
        
        # 삭제 명령어
        elif operator == "D":
            if not max_heap:
                pass
            elif value == "1":
                min_heap.remove(-hq.heappop(max_heap))
            elif value == "-1":
                max_heap.remove(-hq.heappop(min_heap))
                
    
    return [-hq.heappop(max_heap), hq.heappop(min_heap)] if max_heap else [0, 0]

