import sys
input = sys.stdin.readline

# 입력
n = int(input())
m = int(input())
graph = [[100001]*n for _ in range(n)] # 100001은 연결되지 않은 경로
for _ in range(m):
    a, b, c = map(int, input().split())
    # 시작도시와 도착도시를 연결하는 노선은 하나가 아닐 수 있음
    graph[a-1][b-1] = min(graph[a-1][b-1], c)

#플로이드 와샬 알고리즘
def floyd(n, dist):
    # 최단 경로 리스트 초기화
    for via in range(n): #경유지
        for start in range(n): #출발지
            for end in range(n): #도착지
                # 자기 자신으로 오는 경로는 없음
                if start == end:
                    dist[start][end] = 0
                # 경유해서 가는 게 더 빠르다면, 최단거리를 갱신
                elif dist[start][end] > dist[start][via] + dist[via][end]:
                    dist[start][end] = dist[start][via] + dist[via][end]
    return dist

res = floyd(n, graph)

#결과 출력
for row in res:
    for i in row:
        if i == 100001:
            print(0, end=" ")
        else:
            print(i, end=" ")
    print()
