import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

# 입력
N = int(input())
tree = [[] for _ in range(N+1)]  # 트리
parents = [0]*(N+1)  # 부모노드 저장

for _ in range(N-1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

# DFS 탐색
def dfs(start, tree, parents):
    # 부모가 없으면 부모 설정 후, DFS 탐색
    for i in tree[start]:
        if parents[i] == 0:
            parents[i] = start
            dfs(i, tree, parents)

dfs(1, tree, parents)
for i in range(2, N+1):
    print(parents[i])
