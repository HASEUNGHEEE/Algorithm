n = int(input())
info = [list(map(int, input().split())) for _ in range(n)]

# 반복문 돌면서 몸무게와 키 둘 다 큰 원소가 있으면 cnt 1 증가
# 등수는 cnt + 1
output = []
for i in range(n):
  cnt = 0
  for j in range(n):
    if i != j:
      if info[i][0] < info[j][0] and info[i][1] < info[j][1]:
        cnt += 1
  output.append(cnt + 1)

# 리스트 요소 한번에 출력
print(*output)