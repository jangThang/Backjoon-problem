# 입력
n = int(input())

# DP
cache = [1, 1, 2]
for i in range(3, n+1):
    tmp = 0
    for j in range(i):
        tmp += cache[j] * cache[i-j-1]
    cache.append(tmp)
print(cache[n])
