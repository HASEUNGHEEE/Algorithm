input = input() 
"""
input = 1111111
1 => 01
1 => 10
11 => 11
1 => 12
1 => 13
1 => 14
output = 14
"""
output = 0

while True:
  output += 1 # 14
  num = str(output) 
  while len(num) > 0 and len(input) > 0:
    if num[0] == input[0]: 
      # num = 14 input = 1
      input = input[1:]
      # input = ''
    num = num[1:]
    # num = 4
    # num = ''
    # len(num) > 0 성립 X -> while 문 탈출
  if not input:
    print(output)
    break