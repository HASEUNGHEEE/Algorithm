n = int(input())
names = [input()[0] for _ in range(n)]
name_set = set(names)
result = []

for i in name_set:
  if names.count(i) >= 5:
    result.append(i)

if len(result) > 0:
  print(''.join(sorted(result)))
else:
  print("PREDAJA")