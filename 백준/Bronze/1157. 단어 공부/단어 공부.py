import sys
input = sys.stdin.readline
s = input().rstrip().upper()

dic = dict()
for c in s:
  dic[c] = 1 if c not in dic else dic[c] + 1

dic_list = sorted(dic.items(), key=lambda x: x[1], reverse=True)
if len(dic_list) == 1:
  print(dic_list[0][0])
else:
  print("?") if dic_list[0][1] == dic_list[1][1] else print(dic_list[0][0])
