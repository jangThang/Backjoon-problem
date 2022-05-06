import sys
input = sys.stdin.readline

# 입력
N, M = map(int, input().split())  # 가로, 세로
square = []
for _ in range(N):
    square.append(list(input()))

# 가장 큰 정사각형 찾기
size = min(N, M)
res = 0
for i in range(N):
    for j in range(M):
        for k in range(size):
            if ((i + k) < N) and ((j + k) < M) and (square[i][j] == square[i][j + k] == square[i + k][j] == square[i + k][j + k]):
                res = max(res, (k+1)**2)
print(res)
