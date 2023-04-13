import sys
input = sys.stdin.readline

a, b, c = map(int, input().split())
# 입력으로 주어진 시간은 1과 100 사이
time = [0] * 100
total = 0

for _ in range(3):
  start, end = map(int, input().split())
  for i in range(start, end):
    time[i] += 1

for j in time:
  if j == 0: # 같은 시간에 차 0대
    total += 0
  elif j == 1: # 같은 시간에 차 1대
    total += a
  elif j == 2: # 같은 시간에 차 2대
    total += (b * 2)
  elif j == 3: # 같은 시간에 차 3대
    total += (c * 3)
    
print(total)