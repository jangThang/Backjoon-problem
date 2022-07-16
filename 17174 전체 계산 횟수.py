# 입력
N, M = map(int, input().split())
res = N
while N//M != 0:
    N //= M
    res += N
print(res)
