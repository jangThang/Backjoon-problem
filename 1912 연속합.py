import sys
input = sys.stdin.readline

#입력
N = int(input())
cost = list(map(int, input().split()))

#DP
for i in range(1, N):
    # 이전보다 값이 크면 합함
    cost[i] = max(cost[i], cost[i-1]+cost[i])
print(max(cost))
