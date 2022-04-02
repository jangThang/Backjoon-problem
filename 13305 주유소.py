import sys
input = sys.stdin.readline

# 입력
N = int(input())
road = list(map(int, input().split()))
cost = list(map(int, input().split()))

# 그리디 알고리즘
min_cost = 1000000001  # 최대 가격
res = 0  # 최소 기름값
for dist, cost in zip(road, cost):
    min_cost = min(min_cost, cost)
    res += min_cost * dist
print(res)
