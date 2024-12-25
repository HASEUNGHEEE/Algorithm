import sys
input = sys.stdin.readline

# 입력 처리
N = int(input())
cost = [list(map(int, input().split())) for _ in range(N)]

# DP 테이블 초기화
dp = [[0]*3 for _ in range(N)]

# 초기 조건
dp[0][0] = cost[0][0]
dp[0][1] = cost[0][1]
dp[0][2] = cost[0][2]

# 점화식 따라 DP 테이블 채우기
for i in range(1, N): # 1 부터 N-1 까지
    dp[i][0] = cost[i][0] + min(dp[i-1][1], dp[i-1][2])
    dp[i][1] = cost[i][1] + min(dp[i-1][0], dp[i-1][2])
    dp[i][2] = cost[i][2] + min(dp[i-1][0], dp[i-1][1])

# 마지막 집에서 최소 비용 출력
print(min(dp[N-1][0], dp[N-1][1], dp[N-1][2]))