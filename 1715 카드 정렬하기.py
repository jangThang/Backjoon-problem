import heapq
import sys
input = sys.stdin.readline

# 입력
n = int(input())  # 카드 묶음 수
deck = []
for _ in range(n):
    heapq.heappush(deck, int(input()))

# 우선순위 큐
if n == 1:
    print(0) # 카드뭉치가 1개이면 비교 X
else:
    res = 0  # 비교 횟수
    while len(deck) > 1:
        min1 = heapq.heappop(deck)
        min2 = heapq.heappop(deck)
        res += min1 + min2
        heapq.heappush(deck, min1+min2)
    print(res)
