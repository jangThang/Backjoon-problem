#입력
N = int(input())
A = list(map(int, input().split()))

#DP
cache = [1]*N
for i in range(N):
    for j in range(i):
        # 더 작은 이전 원소 발견
        if A[i] > A[j]:
            # 이전 원소에 +1한 게 더 길면 갱신
            cache[i] = max(cache[i], cache[j]+1)
print(max(cache))
