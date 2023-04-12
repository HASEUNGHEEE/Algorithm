s = input()
answer = [0 for _ in range(26)] # [0] * 26

for char in s:
  answer[ord(char) - 97] = s.count(char)

for i in answer:
  print(i, end = " ")