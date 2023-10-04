import sys
input = sys.stdin.readline

n, b = map(int, input().split())
st = []

output = ""

while n != 0:
  st.append(n % b)
  n //= b

while st:
  res = st.pop()
  if res >= 10:
    output += chr(res + 55)
  else:
    output += str(res)

print(output)