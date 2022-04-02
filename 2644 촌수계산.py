from collections import deque

# 입력
n = int(input())
start, end = map(int, input().split())
m = int(input())

graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# bfs 탐색
visited = [False] * (n+1)
queue = deque([(start, 0)])
visited[start] = True

while queue:
    x, cnt = queue.popleft()
    if x == end:
        print(cnt)
        break

    for i in graph[x]:
        if not visited[i]:
            queue.append((i, cnt+1))
            visited[i] = True
else:
    print(-1)
