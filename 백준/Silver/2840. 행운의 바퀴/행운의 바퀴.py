n, k = map(int, input().split())
board = ['?'] * n
idx = 0
flag = True

for _ in range(k):
  num, char = input().split()
  # 원형 -> n으로 나누었을 때의 나머지로 인덱스 설정
  idx = (idx + int(num)) % n
  # 한번도 나온 적 없는 문자일 때
  if board[idx] == '?':
    board[idx] = char
  else:
    if board[idx] == char: continue
    flag = False

for i in range(n):
  if board[i] == '?': continue
  for j in range(i+1, n):
    # 존재하는 문자인지 확인
    if board[i] == board[j]:
      flag = False
      break

if flag:
  for _ in range(n):
    print(board[idx], end='')
    idx = (idx - 1) % n
else:
  print('!')