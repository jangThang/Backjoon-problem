from collections import deque
import sys
input = sys.stdin.readline

#입력
N = int(input())
queue = deque([])
for _ in range(N):
    op = input().rstrip()
    if op == 'pop':
        print(queue.popleft() if queue else -1)
    elif op == 'size':
        print(len(queue))
    elif op == 'empty':
        print(0 if queue else 1)
    elif op == 'front':
        print(queue[0] if queue else -1)
    elif op == 'back':
        print(queue[-1] if queue else -1)
    else: #push
        push, n = op.split()
        queue.append(int(n))
