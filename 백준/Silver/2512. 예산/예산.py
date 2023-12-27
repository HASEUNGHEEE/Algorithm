import sys
input = sys.stdin.readline

n = int(input())
cities = list(map(int, input().split()))
budgets = int(input())
start, end = 0, max(cities)

# 이분탐색
while start <= end:
    mid = (start + end) // 2
    total = 0 # 총 지출 예산
    for i in cities:
        if i > mid:
            total += mid
        else:
            total += i
    # 지출 양이 예산보다 작으면
    if total <= budgets:
        # 시작점 변경
        start = mid + 1
    # 지출 양이 예산보다 크면
    else:
        end = mid - 1
        
print(end)