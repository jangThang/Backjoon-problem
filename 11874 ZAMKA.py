# 입력
L = int(input())
D = int(input())
X = int(input())

# 출력
N = 10001  # 최소값
M = 0  # 최댓값
for i in range(L, D+1):
    res = 0
    for j in str(i):
        res += int(j)
    if res == X:
        N = min(N, i)
        M = max(M, i)
print(N)
print(M)
