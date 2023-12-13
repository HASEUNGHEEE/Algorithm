# 스위치 변환(0이면 1로, 1이면 0으로)
def change(idx):
  if switches[idx] == 0:
    switches[idx] = 1
  else:
    switches[idx] = 0

switch_n = int(input())
switches = [-1] + list(map(int, input().split()))
s = int(input())
for _ in range(s):
  gen, num = map(int, input().split())
  # 남학생
  if gen == 1:
    for idx in range(num, switch_n+1, num):
        change(idx)
  # 여학생
  else:
    change(num)
    for k in range(switch_n//2):
        if num + k > switch_n or num - k < 1 : break
        if switches[num + k] == switches[num - k]:
            change(num + k)
            change(num - k)
        else:
            break
          
for i in range(1, switch_n+1):
  print(switches[i], end = " ")
  if i % 20 == 0 :
      print()