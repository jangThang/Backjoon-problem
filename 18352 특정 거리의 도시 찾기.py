import heapq  # 우선순위 큐 구현을 위함
import sys
input = sys.stdin.readline

# 입력
N, M, K, X = map(int, input().split())  # node, edge, 최단거리, 시작점
graph = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append((b, 1))  # 도착지, 가중치

# 다익스트라 최적경로 탐색
def dijkstra(graph, start):
    distances = [int(1e9)] * (N+1)  # 처음 초기값은 무한대
    distances[start] = 0  # 시작 노드까지의 거리는 0
    queue = []
    heapq.heappush(queue, [distances[start], start])  # 시작 노드부터 탐색 시작

    while queue:  # queue에 남아있는 노드가 없을 때까지 탐색
        dist, node = heapq.heappop(queue)  # 탐색할 노드, 거리

        # 기존 최단거리보다 멀다면 무시
        if distances[node] < dist:
            continue

        # 노드와 연결된 인접노드 탐색
        for next_node, next_dist in graph[node]:
            distance = dist + next_dist  # 인접노드까지의 거리
            if distance < distances[next_node]:  # 기존 거리 보다 짧으면 갱신
                distances[next_node] = distance
                heapq.heappush(queue, [distance, next_node])  # 다음 인접 거리를 계산 하기 위해 큐에 삽입
    return distances

# 출력
dist_start = dijkstra(graph, X)
find = False
for idx, i in enumerate(dist_start):
    if i == K:
        print(idx)
        find = True
if not find:
    print(-1)
