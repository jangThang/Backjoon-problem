import sys
from collections import deque
input = sys.stdin.readline

#입력
N = int(input())
house = []
for _ in range(N):
    house.append([int(x) for x in input().rstrip()])
res = [] #집 크기

#bfs탐색
direction = [(1,0), (-1,0), (0,1), (0,-1)] #상하좌우
queue = deque()
for i in range(N):
    for j in range(N):
        size = 0 #방 크기
        #방문 안한 집이 있으면 탐색
        if house[i][j] == 1:
            size += 1
            house[i][j] = 0
            queue.append((i, j))
        while queue:
            x, y = queue.popleft()
            for dx, dy in direction:
                nx, ny = x+dx, y+dy

                #범위를 벗어나면 무시
                if nx < 0 or ny < 0 or nx >= N or ny >= N:
                    continue

                #처음 방문하면 탐색
                if house[nx][ny] == 1:
                    house[nx][ny] = 0 #탐색 완료
                    queue.append((nx, ny))
                    size += 1 #방 추가
        if size != 0:
            res.append(size)
#오름차순 정렬
res.sort()
print(len(res))
for i in res:
    print(i)
