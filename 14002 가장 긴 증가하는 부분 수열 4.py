# 입력
N = int(input())
A = list(map(int, input().split()))

# DP로 가장 긴 증가 부분 수열 찾기
cache = [1]*N
for i in range(N):
    for j in range(i):
        # 더 작은 이전 원소 발견
        if A[i] > A[j]:
            # 이전 원소에 +1한 게 더 길면 갱신
            cache[i] = max(cache[i], cache[j]+1)
res = max(cache)
print(res)

# 역추적
array = [] # 증가수열
for i in range(N-1, -1, -1):
    if cache[i] == res:
        array.append(A[i])
        res -= 1

for i in array[::-1]:
    print(i, end=" ")
