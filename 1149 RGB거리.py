import sys
input = sys.stdin.readline

#입력
N = int(input())
cost = []
for _ in range(N):
    cost.append(list(map(int, input().split())))

#DP
for i in range(1, N):
    # i번째 집을 빨강색으로 칠했을 때
    cost[i][0] = min(cost[i-1][1], cost[i-1][2]) + cost[i][0]

    # i번째 집을 초록색으로 칠했을 때
    cost[i][1] = min(cost[i-1][0], cost[i-1][2]) + cost[i][1]

    # i번째 집을 파란색으로 칠했을 때
    cost[i][2] = min(cost[i-1][0], cost[i-1][1]) + cost[i][2]
print(min(cost[N-1]))
