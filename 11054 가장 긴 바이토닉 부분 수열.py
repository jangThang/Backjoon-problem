# 입력
N = int(input())
A = list(map(int, input().split()))
reverse_A = A[::-1]

# DP로 가장 긴 증가 및 감소 부분 수열 찾기
increase = [1]*N
decrease = [1]*N
for i in range(N):
    for j in range(i):
        # 더 작은 이전 원소 발견
        if A[i] > A[j]:
            # 이전 원소에 +1한 게 더 길면 갱신
            increase[i] = max(increase[i], increase[j]+1)

        # 더 큰 이전 원소 발견
        if reverse_A[i] > reverse_A[j]:
            decrease[i] = max(decrease[i], decrease[j]+1)

# 가장 긴 바이토닉 수열의 길이 찾기
maxlen = 0
for i in range(N):
    maxlen = max(maxlen, increase[i]+decrease[N-i-1]-1)
print(maxlen)
