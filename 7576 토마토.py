from collections import deque
import sys
input = sys.stdin.readline

#입력
M, N = map(int, input().split()) #가로, 세로
tomato = []
queue = deque()
for i in range(N):
    tomato.append(list(map(int, input().split())))
    for j in range(M):
        # 잘 익은 토마토의 위치를 Queue에 입력
        if tomato[i][j] == 1:
            queue.append((i, j))

#BFS 탐색
day = 0 #토마토가 다 익는 데 걸리는 시간
direction = [[0, 1], [0, -1], [1, 0], [-1, 0]] #상하좌우 이동
while queue:
    x, y = queue.popleft() #큐에서 토마토 위치 꺼냄
    #토마토 주위 상하좌우 탐색
    for dx, dy in direction:
        a, b = x + dx, y + dy
        #a, b가 모두 범위를 안 벗어나면서, 안 익은 토마토를 발견할 때
        if 0 <= a < N and 0 <= b < M and tomato[a][b] == 0:
            queue.append((a, b)) #익을 토마토
            tomato[a][b] = tomato[x][y]+1

check = False #안 익은 토마토 있는지
for i in tomato:
    for j in i:
        #안 익은 토마토 발견
        if j == 0:
            check = True
            break
    #안 익은 토마토가 있을 시 -1 출력 후 종료
    if check:
        print(-1)
        break
    day = max(day, max(i))
# 다 익었을 경우, 걸린 날짜 출력
else:
    print(day-1)
