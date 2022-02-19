import sys
import heapq
input = sys.stdin.readline

N = int(input())
minusHeap = [] # 음수만 저장
plusHeap = [] # 양수만 저장

for _ in range(N):
    x = int(input())
    # x가 음수일 때
    if x < 0:
        heapq.heappush(minusHeap, -x) #최대 힙과 비슷하게 마이너스 붙여서 저장

    # x가 양수일 때
    elif x > 0:
        heapq.heappush(plusHeap, x)

    # x가 0이고 둘 다 비어있지 않으면 비교 후 pop
    elif minusHeap and plusHeap:
        if minusHeap[0] == plusHeap[0]: #둘의 절댓값이 같으면, minusHeap에서 pop
            print(-heapq.heappop(minusHeap))
        elif minusHeap[0] > plusHeap[0]:
            print(heapq.heappop(plusHeap))
        else:
            print(-heapq.heappop(minusHeap))

    # x가 0이고 minusHeap만 있을 때
    elif minusHeap:
        print(-heapq.heappop(minusHeap))

    # x가 0이고 plusHeap만 있을 때
    elif plusHeap:
        print(heapq.heappop(plusHeap))

    # x가 0이고 모두 비어있으면 0 출력
    else:
        print(0)
    #print(minusHeap, plusHeap) 힙 동작 확인
