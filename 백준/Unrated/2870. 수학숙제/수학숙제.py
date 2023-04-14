import re
N = int(input())
answer = [] # 찾은 숫자를 담을 리스트
  
for _ in range(N):
  # 입력된 글자 input()에서 연속된 숫자들을 추출하여 List로 리턴 => re.findall()
  numbers = re.findall(r'\d+', input())
  # 연속된 숫자 원소에 접근
  for number in numbers:
    answer.append(int(number))

# 오름차순으로 정렬 후 하나씩 출력
answer.sort()
for i in answer:
  print(i)


"""
정규표현식 r'\d+' : 1회 이상 반복되는 숫자들에 대한 패턴
\d => 숫자를 한 글자만 찾는다
+ => 하나 혹은 그 이상 연결된
\d+ => 하나 혹은 그 이상 연결된 숫자
"""