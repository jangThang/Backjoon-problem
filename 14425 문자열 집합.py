import sys
input = sys.stdin.readline

# 입력
N, M = map(int, input().split())
S = set()  # 집합 S
for _ in range(N):
    S.add(input().rstrip())

# 같은 단어 찾기
cnt = 0
for _ in range(M):
    if input().rstrip() in S:
        cnt += 1
print(cnt)
