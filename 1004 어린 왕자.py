import sys
input = sys.stdin.readline

# 입력
T = int(input())
for _ in range(T):
    x1, y1, x2, y2 = map(int, input().split())
    res = 0  # 거치는 행성계

    n = int(input())
    for _ in range(n):
        x, y, r = map(int, input().split())
        start = ((x1-x)**2 + (y1-y)**2)**0.5  # 출발지에서 행성 중심까지의 거리
        end = ((x2-x)**2 + (y2-y)**2)**0.5  # 도착지에서 행성 중심까지의 거리

        # 모두 안에 있으면 지나갈 필요 없음
        if start < r and end < r:
            pass
        # 시작점이나 도착점이 안에 있을 경우 +1
        elif start < r:
            res += 1
        elif end < r:
            res += 1
    print(res)
