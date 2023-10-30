import sys
import math
input = sys.stdin.readline

# 세로: h, 가로: w
h, w, n, m = map(int, input().split())
cols = math.ceil(h/(n+1))
rows = math.ceil(w/(m+1))
print(cols*rows)