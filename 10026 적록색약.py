from collections import deque
import sys
input = sys.stdin.readline

#입력
N = int(input())
ntable = [] #일반 테이블
rgtable = [] #적록색맹 테이블
for _ in range(N):
    x = list(input().rstrip())
    ntable.append(x)
    rgtable.append([1 if i == 'B' else 2 for i in x]) #B는 1, RG는 2로 저장

#BFS탐색
def bfs(table, a, b, color):
    direction = [(1,0), (-1,0), (0,1), (0,-1)]
    queue = deque([(a, b)])
    while queue:
        x, y = queue.popleft()
        for dx, dy in direction:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < N and table[nx][ny] == color:
                queue.append((nx, ny))
                table[nx][ny] = 0

cnt = 0 #일반 구역수
cnt_rg = 0 #적록색맹 구역수
for i in range(N):
    for j in range(N):
        if ntable[i][j] != 0:
            cnt += 1
            bfs(ntable, i, j, ntable[i][j])
        if rgtable[i][j] != 0:
            cnt_rg += 1
            bfs(rgtable, i, j, rgtable[i][j])
print(cnt, cnt_rg)
