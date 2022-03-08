import sys
input = sys.stdin.readline

# 입력
N, M = map(int, input().split())
queue = list(range(1, N+1))
numlist = list(map(int, input().split()))

res = 0  # 2번, 3번 연산횟수
pointer = 0  # 큐 포인터
for idx, x in enumerate(numlist):
    # 왼쪽으로 탐색
    left = 0 # 2번 연산횟수
    while x != queue[(pointer+left)%(N-idx)]:
        left += 1

    # 오른쪽으로 탐색
    right = 0 # 3번 연산횟수
    while x != queue[(pointer-right)%(N-idx)]:
        right += 1

    # 더 적은 탐색횟수로 이동
    if left > right:
        res += right
        pointer = (pointer-right)%(N-idx)
        queue.pop(pointer)

    else:
        res += left
        pointer = (pointer+left)%(N-idx)
        queue.pop(pointer)
print(res)
