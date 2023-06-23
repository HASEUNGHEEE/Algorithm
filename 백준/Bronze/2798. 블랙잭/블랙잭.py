from itertools import combinations
import sys

# 입력
n, m = map(int, input().split())
cards = list(map(int, input().split()))
answer = []

for com in combinations(cards, 3): # cards 리스트에서 3장씩 뽑는 모든 조합 구해서 탐색
    tmp = 0
    tmp += sum(com)
    if tmp <= m: answer.append(tmp)

# 출력
print(max(answer))