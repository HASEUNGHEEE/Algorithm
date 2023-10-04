import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
  n = int(input())
  palindrome = []

  for i in range(2, 65): # 2진수 ~ 64진수
    ch = []
    tmp = n # 반복 확인해야 하므로 tmp에 n값 담아두기
    while tmp != 0:
      ch.append(tmp%i)
      tmp //= i

    for j in range(len(ch)//2): # 회문 -> 절반까지 확인하면 됨
      if ch[j] != ch[-1-j]: # 회문 아니면 'X'
        palindrome.append('X')
        break

  if len(palindrome) == 63: print(0) # 2진수부터 64진수까지 회문 하나도 없으면 63개의 X만 있다
  else: print(1)