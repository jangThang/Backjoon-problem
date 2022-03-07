from collections import deque
import sys
input = sys.stdin.readline

#입력
N = int(input())
sea = []  # 그래프
startX, startY = 0, 0 # 아기상어 위치
for i in range(N):
    lst = list(map(int, input().split()))
    for j in range(N):
        if lst[j] == 9:
            lst[j] = 0  # 크기가 9인 물고기로 오인하지 않도록
            startX, startY = i, j  # 아기상어 위치
    sea.append(lst)

# BFS탐색
direction = [(0, 1), (-1, 0), (0, -1), (1, 0)]  # 상하좌우
size = 2
move = 0
eat = 0

while True:
    visited = [[False] * N for _ in range(N)]  # 방문표시
    queue = deque([(startX, startY, 0)])  # 시작 위치
    visited[startX][startY] = True
    flag = 9999 # 먹을 수 있는 물고기 탐색여부
    fish = []  # 물고기 위치
    while queue:
        x, y, cnt = queue.popleft()
        if cnt > flag:
            break

        #상하좌우 탐색
        for dx, dy in direction:
            nx, ny = x+dx, y+dy
            # 범위를 벗어나지 않고, 자신이 지나갈 수 있는 미방문인 곳을 탐색
            if 0 <= nx < N and 0 <= ny < N and sea[nx][ny] <= size and not visited[nx][ny]:
                visited[nx][ny] = True  # 방문
                queue.append((nx, ny, cnt+1))
                # 자신보다 작은 물고기가 있으면 먹음
                if 0 < sea[nx][ny] < size:
                    fish.append((nx, ny, cnt+1))
                    flag = cnt  # 탐색완료

    # 먹을 수 있는 물고기가 있으면 계속 탐색
    if fish:
        fish.sort() #위, 왼쪽 물고기 먼저 먹음
        x, y, dist = fish[0] #먹을 물고기 위치와 필요한 이동거리
        sea[x][y] = 0 #먹고나면 빈 칸
        move += dist

        # 먹은 물고기 횟수+1, 사이즈와 동일하다면 사이즈업
        eat += 1
        if eat == size:
            size += 1
            eat = 0
        startX, startY = x, y

    # 더이상 먹을 수 있는 물고기 없음
    else:
        break
print(move)
