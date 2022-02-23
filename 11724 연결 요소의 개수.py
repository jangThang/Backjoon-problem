import sys
input = sys.stdin.readline

#dfs 탐색(탐색할 그래프, 시작 노드, 방문여부 리스트)
def dfs(graph, node, visited):
    visited[node] = True #시작 노드 방문
    # 인접 노드를 재귀적으로 방문
    for i in graph[node]:
        if not visited[i]: #방문하지 않은 노드라면
            dfs(graph, i, visited) #해당 노드를 시작 노드로 dfs

#그래프 입력
N, M = map(int, input().split())
graph = [ [i] for i in range(N+1) ]
for i in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False]*(N+1) #방문 여부 리스트
cnt = 0 #연결 요소 개수
for i in range(1, N+1):
    if not visited[i]: #방문하지 않은 노드라면
        cnt += 1 #연결요소를 하나 늘리고
        dfs(graph, i, visited) #dfs탐색
print(cnt)
