from collections import deque
import sys
input = sys.stdin.readline

# 입력
N, M, K = map(int, input().split())
board = [[True]*M for _ in range(N)]
for _ in range(K):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(y1, y2):
        for j in range(x1, x2):
            board[i][j] = False

# BFS 탐색
area = []  # 영역
direction = [(1,0), (-1,0), (0,1), (0,-1)]

for i in range(N):
    for j in range(M):
        # 탐색하지 않은 영역이면 BFS 탐색
        if board[i][j]:
            queue = deque([(i, j)])
            board[i][j] = False
            size = 0
            while queue:
                x, y = queue.popleft()
                size += 1
                for dx, dy in direction:
                    nx, ny = x+dx, y+dy
                    if 0 <= nx < N and 0 <= ny < M and board[nx][ny]:
                        board[nx][ny] = False
                        queue.append((nx, ny))
            area.append(size)

# 정렬 후 출력
area.sort()
print(len(area))
print(" ".join(map(str, area)))
