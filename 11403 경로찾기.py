import sys
input = sys.stdin.readline

#플로이드 와샬 알고리즘
def floyd(n, dist):
    # 최단 경로 리스트 초기화
    for via in range(n): #경유지
        for start in range(n): #출발지
            for end in range(n): #도착지
                # 경유해서 가는 게 있다면, 경로 있음으로 교체
                if dist[start][via] * dist[via][end]:
                    dist[start][end] = 1
    return dist

#입력
N = int(input())
graph = []
for _ in range(N):
    graph.append(list(map(int, input().split())))

#플로이드 와샬
dist = floyd(N, graph)

#출력
for i in range(N):
    for j in range(N):
        print(dist[i][j], end=" ")
    print()
