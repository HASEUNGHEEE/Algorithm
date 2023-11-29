n, k = map(int, input().split())
info = [list(map(int, input().split())) for _ in range(n)]

for i in range(n):
  if info[i][0] == k:
    cnt = 0
    for j in range(n):
      if i != j:
        if info[i][1] < info[j][1]:
          cnt += 1
        elif info[i][1] == info[j][1]:
          if info[i][2] < info[j][2]:
            cnt += 1
          elif info[i][2] == info[j][2]:
            if info[i][3] < info[j][3]:
              cnt += 1
print(cnt + 1)



  
  