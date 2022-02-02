import sys
input = sys.stdin.readline

N, K = map(int, input().split())
res = 1

# n!/(n-k)!
for i in range(K):
    res *= (N-i)

# /k!
for j in range(K):
    res //= (K-j)
print(res)
