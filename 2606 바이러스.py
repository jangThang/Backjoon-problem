from collections import deque
import sys
input = sys.stdin.readline

# BFS 탐색 (탐색할 그래프, 노드 수, 시작 지점)
def bfs(graph, n, start):
    queue = deque([start]) #인접 노드를 저장할 Queue

    visited = [False]*(n+1) #방문 여부를 확인할 리스트
    visited[start] = True #시작 노드 방문
    res = 0 #감염된 컴퓨터 개수

    #모든 노드를 탐색할 때까지 반복
    while queue:
        #방문 노드
        node = queue.popleft()
        res += 1

        #방문한 노드의 주변 노드를 큐에 삽입
        for i in graph[node]:
            #방문하지 않는 주변 노드일 경우
            if not visited[i]:
                queue.append(i) #큐에 추가
                visited[i] = True #방문
    return res

nodeNum = int(input())
edgeNum = int(input())
graph = [ [i] for i in range(nodeNum+1) ]

for i in range(edgeNum):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

print(bfs(graph, nodeNum, 1)-1) #1번 노드 제외
