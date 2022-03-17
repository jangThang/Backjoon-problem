from collections import deque

# 입력
A, B = map(int, input().split())

# BFS 탐색
queue = deque([(1, A)])
while queue:
    cnt, x = queue.popleft()

    # B와 같다면 탐색종료
    if x == B:
        print(cnt)
        break

    # 2를 곱한다
    if x * 2 <= B:
        queue.append((cnt+1, x*2))

    # 1를 오른쪽에 추가한다
    if x * 10 + 1 <= B:
        queue.append((cnt+1, x*10+1))

# 찾지 못했다면 -1 출력
else:
    print(-1)
