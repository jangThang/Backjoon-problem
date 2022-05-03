import sys
input = sys.stdin.readline

while True:
    # 입력
    n = int(input())
    if n == -1:
        break

    res = 0  # 이동한 거리
    time = 0  # 이동한 시간
    for _ in range(n):
        s, t = map(int, input().split())
        res += s*(t-time)
        time = t
    print(res, "miles")
