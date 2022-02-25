import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
maze = []
for _ in range(N):
    maze.append([int(i) for i in input().rstrip()])

direction = [(1,0), (-1, 0), (0, 1), (0, -1)] #상하좌우
queue = deque([(0, 0)]) #0,0부터 시작

#bfs 탐색
while queue:
    x, y = queue.popleft()
    for dx, dy in direction:
        nx = x + dx
        ny = y + dy

        #미로 공간 벗어나면 건너뛰기
        if nx < 0 or ny < 0 or nx >= N or ny >= M:
            continue

        #벽인 경우 무시
        if maze[nx][ny] == 0:
            continue

        #처음 방문하면 거리기록
        if maze[nx][ny] == 1:
            maze[nx][ny] += maze[x][y]
            queue.append((nx, ny))

print(maze[N-1][M-1])
