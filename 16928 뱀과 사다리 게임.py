import sys
from collections import deque
input = sys.stdin.readline

#입력
board = [0]*101 #보드판
N, M = map(int, input().split())
ladder = {} #사다리
for _ in range(N):
    x, y = map(int, input().split())
    ladder[x] = y #사다리 저장

snake = {} #뱀
for _ in range(M):
    u, v = map(int, input().split())
    snake[u] = v #뱀 저장

#bfs탐색
visited = [False]*101 #방문여부
queue = deque([1]) #1번 칸부터 시작
visited[1] = True
while queue:
    #주사위는 1~6
    x = queue.popleft()
    for i in range(1, 7):
        nx = x+i
        #범위를 초과하거나 이미 방문했으면 무시
        if nx > 100 or visited[nx]:
            continue
        #사다리일 경우 해당 칸으로 이동
        if nx in ladder.keys():
            nx = ladder[nx]
        # 뱀일 경우 해당 칸으로 이동
        if nx in snake.keys():
            nx = snake[nx]
        #첫 방문일 경우
        if not visited[nx]:
            queue.append(nx)
            visited[nx] = True
            board[nx] += board[x]+1
print(board[100])
