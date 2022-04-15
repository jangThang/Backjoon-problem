import sys
input = sys.stdin.readline

# 입력
N, M = map(int, input().split())
maze = [[0]*M]
for _ in range(N):
    maze.append(list(map(int, input().split())))

# DP
cache = [[0]*M for _ in range(N+1)]
for i in range(1, N+1):
    for j in range(M):
        cache[i][j] = max(cache[i-1][j], cache[i][j-1]) + maze[i][j]
print(cache[N][M-1])
