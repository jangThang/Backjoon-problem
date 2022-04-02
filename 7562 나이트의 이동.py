from collections import deque

# 입력
T = int(input())
for _ in range(T):
    l = int(input())
    s1, s2 = map(int, input().split())
    e1, e2 = map(int, input().split())

    # bfs
    board = [[0]*l for _ in range(l)]
    queue = deque([(s1, s2)])
    board[s1][s2] = 1

    direction = [(-2, -1), (-1, -2), (1, -2), (2, -1), (-2, 1), (-1, 2), (1, 2), (2, 1)]
    while queue:
        x, y = queue.popleft()
        if x == e1 and y == e2:
            print(board[x][y]-1)
            break
        for dx, dy in direction:
            nx, ny = x+dx, y+dy
            if 0 <= nx < l and 0 <= ny < l and board[nx][ny] == 0:
                board[nx][ny] = board[x][y] + 1
                queue.append((nx, ny))
