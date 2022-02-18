N, M, K = map(int, input().split())
maxO = min(M, K) #앞, 뒷장이 같은 최대 O의 개수
maxX = min(N-M, N-K) #앞, 뒷장이 같은 최대 X의 개수
print(maxO+maxX)
