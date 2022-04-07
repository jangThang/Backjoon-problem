from collections import deque
import sys
input = sys.stdin.readline


while True:
    # 입력
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break

    board = []
    for _ in range(h):
        board.append(list(map(int, input().split())))

    # BFS 탐색
    cnt = 0  # 섬의 개수
    for i in range(h):
        for j in range(w):
            # 땅이 있으면 bfs 탐색 시작
            if board[i][j] == 1:
                cnt += 1
                queue = deque([(i, j)])
                board[i][j] = 0

                # 상하좌우, 대각선 8방향 탐색
                direction = [(1,0), (-1,0), (0,1), (0,-1), (1,1), (-1,-1), (1,-1), (-1,1)]
                while queue:
                    x, y = queue.popleft()

                    for dx, dy in direction:
                        nx, ny = x+dx, y+dy
                        # 지도를 벗어나지 않은 땅이 있다면 탐색
                        if 0 <= nx < h and 0 <= ny < w and board[nx][ny] == 1:
                            board[nx][ny] = 0
                            queue.append((nx, ny))
    print(cnt)
