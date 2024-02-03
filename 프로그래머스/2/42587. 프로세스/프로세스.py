from collections import deque
def solution(priorities, location):
    answer = 0
    que = deque(priorities)

    while que:
        maximum = max(que)
        now = que.popleft()
        location -= 1
        if now != maximum:
            que.append(now)
            if location < 0: location = len(que) - 1
        else:
            answer += 1
            if location < 0: break
    return answer
