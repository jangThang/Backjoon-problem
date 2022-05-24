from collections import deque
from copy import deepcopy
import sys
input = sys.stdin.readline

# 입력
N, M = map(int, input().split())
board = []
for _ in range(N):
    board.append(list(map(int, input().rstrip())))

# bfs
direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]  # 상하좌우
visited = [[[0]*2 for _ in range(M)] for _ in range(N)]
queue = deque([(0, 0, 0)])
visited[0][0][0] = 1
while queue:
    x, y, w = queue.popleft()
    if x == N-1 and y == M-1:
        print(visited[x][y][w])
        break
    for dx, dy in direction:
        nx, ny = x+dx, y+dy
        if 0 <= nx < N and 0 <= ny < M:
            # 벽이 아니고, 방문하지 않은 곳이면 탐색
            if board[nx][ny] == 0 and visited[nx][ny][w] == 0:
                visited[nx][ny][w] = visited[x][y][w] + 1
                queue.append((nx, ny, w))

            # 아직 부숴본 적 없는 벽이라면 뚫고 탐색
            elif board[nx][ny] == 1 and w == 0:
                visited[nx][ny][w+1] = visited[x][y][w] + 1
                queue.append((nx, ny, w+1))
else:
    print(-1)
