n = int(input())
# a*d 뿐만 아니라 abc*wed 등의 패턴도 가능
pattern = input().split("*")
length = len(pattern[0]) + len(pattern[1])

for _ in range(n):
  file = input()
  if length > len(file): print("NE")
  else:
    if pattern[0] == file[:len(pattern[0])] and pattern[1] == file[-len(pattern[1]):]:
      print("DA")
    else:
      print("NE")