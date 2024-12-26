import sys
input = sys.stdin.readline

# 입력 처리
N = int(input().strip()) # 개행 문자 제거
cost = [list(map(int, input().strip().split())) for _ in range(N)]

INF = float('inf') # 초기 비용을 무한대로 설정해 최솟값 비교시 항상 갱신
min_cost = INF # N개의 집을 칠하는 최소 비용 저장

# 첫번째 집의 색깔을 빨,초,파로 고정하여 각각 계산
for first_color in range(3): # 빨강: 0 초록: 1 파랑: 2
    # DP 테이블 초기화 (dp[i][j]: i번째 집까지 j색으로 칠했을 때의 최소 비용)
    dp = [[INF]*3 for _ in range(N)]

    # 초기 조건: 선택된 색의 비용은 cost[0][first_color]로 설정하고, 다른 색은 INF로 설정
    dp[0][first_color] = cost[0][first_color]
    for color in range(3):
        if color != first_color:
            dp[0][color] = INF

    # 점화식 따라 DP 테이블 채우기
    for i in range(1, N): # 1 부터 N-1 까지
        dp[i][0] = cost[i][0] + min(dp[i-1][1], dp[i-1][2])
        dp[i][1] = cost[i][1] + min(dp[i-1][0], dp[i-1][2])
        dp[i][2] = cost[i][2] + min(dp[i-1][0], dp[i-1][1])

    # 마지막 집의 색 비교: dp[N-1]에서 last_color != first_color 인 값 중 최소 비용 선택
    for last_color in range(3):
        if last_color != first_color:
            min_cost = min(min_cost, dp[N-1][last_color])

print(min_cost)