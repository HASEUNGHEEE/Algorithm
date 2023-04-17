str = input()
result = ''

for char in str:
  # 대문자
  if char.isupper():
    num = ord(char) + 13
    if num > 90: num -= 26
    result += chr(num)
  # 소문자
  elif char.islower():
    num = ord(char) + 13
    if num > 122: num -= 26
    result += chr(num)
  # 숫자, 공백
  else:
    result += char

print(result)