N, M = map(int, input().split())
res = max((M//2)*N + (M%2)*(N//2), (N//2)*M + (N%2)*(M//2))
print(res)
