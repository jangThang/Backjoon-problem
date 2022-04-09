# 입력
n = int(input())

# DP
cache = [[0] * 10 for _ in range(n+1)]
for i in range(10):
    cache[0][i] = 1

for i in range(1, n+1):
    for j in range(10):
        for k in range(j+1):
            cache[i][j] += (cache[i-1][k] % 10007)
print(cache[n][9] % 10007)
