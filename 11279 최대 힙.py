import sys
import heapq
input = sys.stdin.readline

N = int(input())
heap = []

for _ in range(N):
    x = int(input())
    # x가 0이 아니면 push
    if x != 0:
        heapq.heappush(heap, -x)

    # x가 0이고 비어있지 않으면 pop
    elif heap:
        print(-heapq.heappop(heap))

    # x가 0이고 비어있으면 0 출력
    else:
        print(0)
