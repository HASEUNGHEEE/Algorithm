from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
position = list(map(int, input().split()))

# deque([1, 2, 3, ... , n])
deque = deque([i for i in range(1, n+1)])

cnt = 0
# 뽑아내려는 위치
for i in position:
    while True:
        if deque[0] == i: # deque의 첫번째 인덱스가 뽑아내려는 위치와 같을 때
            deque.popleft()
            break
        else:
            if deque.index(i) <= len(deque) // 2: 
                while deque[0] != i: # deque의 첫번째 인덱스와 뽑을 위치 i가 같아질 때까지
                    deque.append(deque.popleft())
                    cnt += 1
            else:
                while deque[0] != i:
                    deque.appendleft(deque.pop())
                    cnt += 1
print(cnt)            
"""
rotate 함수
deque.rotate(-x) // 왼쪽으로 x만큼 이동한다
deque.rotate(x) // 오른쪽으로 x만큼 이동한다
"""
