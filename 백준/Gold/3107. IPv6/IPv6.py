import sys
input = sys.stdin.readline

ip_address = list(input().rstrip().split(":")) # 구분자(:) 기준으로 문자열 분리하여 리스트화

full_address = []
check_flag = False

for address in ip_address:
  if address == '' and check_flag == False:
    full_address += ['0000' for _ in range(8-len(ip_address)+1)]
    check_flag = True
  else:
    full_address.append(address.zfill(4)) # zfill(): 문자열 앞을 0으로 채우는 함수

print(":".join(full_address)) # 구분자(:) 기준으로 문자열 합치기