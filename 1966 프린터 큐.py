import sys
from collections import deque
input = sys.stdin.readline

T = int(input())
for i in range(T):
    N, M = map(int, input().split())
    printQueue = deque(list(map(int, input().split()))) #프린터 큐

    idx = deque(list(range(N))) # 인덱스
    idx[M] = 'M'

    cnt = 0 #뽑히는 순서
    while True:
        # 중요도가 가장 높으면 pop
        if printQueue[0] == max(printQueue):
            cnt += 1
            # 해당 문서가 M일 경우 종료
            if idx[0] == 'M':
                print(cnt)
                break
            # 아닐 경우 pop
            else:
                printQueue.popleft()
                idx.popleft()
        # 중요도가 높지 않을 경우 뒤로 보냄
        else:
            printQueue.append(printQueue.popleft())
            idx.append(idx.popleft())
