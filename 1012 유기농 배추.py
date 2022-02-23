from collections import deque
import sys
input = sys.stdin.readline

#bfs 탐색(탐색할 그래프, 시작지점(x,y))
def bfs(graph, x, y):
    queue = deque()
    queue.append((x, y))
    graph[x][y] = False #시작지점 방문

    direction = [[0,1], [0,-1], [1,0], [-1,0]] #상하좌우 이동
    while queue:
        a, b = queue.popleft()

        #상하좌우 탐색
        for i in range(4):
            dx = a + direction[i][0]
            dy = b + direction[i][1]

            #인접행렬 범위를 벗어나지 않을 때, 배추가 있는지 탐색
            if not (dx < 0 or dy < 0 or dx >= M or dy >= N):
                if graph[dx][dy]:
                    graph[dx][dy] = False
                    queue.append((dx, dy))

T = int(input())
for _ in range(T):
    M, N, K = map(int, input().split()) #배추밭의 가로, 세로, 배추 개수
    graph = [[False]*N for _ in range(M)]
    for i in range(K):
        x, y = map(int, input().split())
        graph[x][y] = True #배추 있음

    cnt = 0 #배추 흰 지렁이 개수
    for i in range(M):
        for j in range(N):
            if graph[i][j]: #배추가 있으면
                bfs(graph, i, j) #bfs 시행
                cnt += 1
    print(cnt)
