# 입력
n = int(input())
data = list(map(int, input().split()))
add, sub, mul, div = map(int, input().split())

# 최댓값과 최솟값 초기화
max_val = -1e9
min_val = 1e9

def dfs(add, sub, mul, div, i, arr):
    global max_val, min_val
    # 주어진 수열을 다 받았을 경우
    if i == n:
        max_val = max(max_val, arr)
        min_val = min(min_val, arr)
    if add:
        dfs(add-1, sub, mul, div, i+1, arr + data[i])
    if sub:
        dfs(add, sub-1, mul, div, i+1, arr - data[i])
    if mul:
        dfs(add, sub, mul-1, div, i+1, arr * data[i])
    if div:
        dfs(add, sub, mul, div-1, i+1, int(arr / data[i]))
         
        
dfs(add, sub, mul, div, 1, data[0])

print(max_val)
print(min_val)