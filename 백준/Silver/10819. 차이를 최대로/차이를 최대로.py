from itertools import permutations
import sys

# 입력
input = sys.stdin.readline
n = int(input())
A = list(map(int, input().split()))
answer = []

for per in permutations(A, n): # 모든 순열 구하여 탐색
    tmp = 0
    for i in range(n-1):
        tmp += abs(per[i] - per[i+1])
    answer.append(tmp)
   
# 출력
print(max(answer)) # 모든 식의 값이 담긴 answer 리스트에서 최댓값 출력