from math import comb

# 입력
n, k = map(int, input().split())

# 이항계수
print(comb(n-1, k-1))
