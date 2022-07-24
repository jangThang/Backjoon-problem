# 입력
N = int(input())
K = int(input())

# 출력
res = N
for i in range(1, K+1):
    res += N*(10**i)
print(res)
