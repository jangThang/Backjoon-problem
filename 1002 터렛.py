import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    dist = ((x1-x2)**2 + (y1-y2)**2)**0.5 #두 터렛 간의 거리 제곱

    #case1 두 원이 겹침
    if (x1, y1, r1) == (x2, y2, r2):
        print(-1)

    #case2 한 점만 만남 (내접, 외접)
    elif dist == abs(r1-r2) or dist == r1+r2:
        print(1)

    #case3 두 점만 만남
    elif abs(r1-r2) < dist < r1+r2:
        print(2)

    #case4 만나지 않음
    else:
        print(0)
