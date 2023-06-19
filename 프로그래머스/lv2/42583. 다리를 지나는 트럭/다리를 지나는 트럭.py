from collections import deque
def solution(bridge_length, weight, truck_weights):
    time = 0
    bridge = deque([0] * bridge_length)
    waiting = deque(truck_weights)
    bridge_weight = 0
    
    while waiting:
        time += 1
        bridge_weight -= bridge.popleft()
        
        if bridge_weight + waiting[0] <= weight:
            bridge_weight += waiting[0]
            bridge.append(waiting.popleft())
        else:
            bridge.append(0)
    
    time += bridge_length
    return time