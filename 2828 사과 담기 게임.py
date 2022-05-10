import sys
input = sys.stdin.readline

# 입력
n, m = map(int, input().split())  # 스크린의 길이, 바구니 너비
m -= 1
j = int(input())

# 그리디
res = 0  # 바구니가 이동해야 하는 최소 거리
loc = 1  # 바구니의 왼쪽 끝 위치
for _ in range(j):
    x = int(input())

    # 바구니보다 왼쪽에 있을 경우
    if x < loc:
        res += (loc - x)
        loc = x

    # 바구니에 위치할 경우
    elif loc <= x < loc+m:
        pass  # 가만히 있음

    # 바구니보다 오른쪽에 있을 경우
    else:
        res += (x-m) - loc
        loc = x-m
print(res)
