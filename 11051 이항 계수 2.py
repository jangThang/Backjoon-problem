import sys
input = sys.stdin.readline

N, K = map(int, input().split())
cache = [[1 for _ in range(K+1)] for _ in range(N+1)]

for i in range(1, K+1):
    for j in range(i+1, N+1):
        cache[j][i] = (cache[j-1][i-1] + cache[j-1][i]) % 10007
        print(j, i, cache[j][i])

print(cache[N][K])
