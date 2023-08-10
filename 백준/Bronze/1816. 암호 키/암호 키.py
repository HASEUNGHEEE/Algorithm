import sys
input = sys.stdin.readline

# 입력
n = int(input())
for _ in range(n):
  s = int(input())
  for i in range(2, 1_000_001):
    if s % i == 0:
      print("NO")
      break
    if i == 1000000:
      print("YES")