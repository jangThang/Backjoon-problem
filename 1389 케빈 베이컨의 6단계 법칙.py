import sys
input = sys.stdin.readline

#플로이드 와샬 알고리즘
def floyd(n, dist):
    # 최단 경로 리스트 초기화
    for via in range(n): #경유지
        for start in range(n): #출발지
            for end in range(n): #도착지
                # 경유지를 경유하는 게 더 짧다면 갱신
                if dist[start][end] > dist[start][via] + dist[via][end]:
                    dist[start][end] = dist[start][via] + dist[via][end]
    return dist

#입력
N, M = map(int, input().split()) #노드, 간선 수
graph = [[10000]*N for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a-1][b-1] = 1
    graph[b-1][a-1] = 1

dist = floyd(N, graph)

res = 0 #가장 작은 사람
min_score = 100000
for i, lst in enumerate(dist, 1):
    if sum(lst) < min_score:
        min_score = sum(lst)
        res = i
print(res)
