import sys
input = sys.stdin.readline

T = int(input())
for i in range(T):
    x, y = map(int, input().split())
    dist = y-x
    cnt = 0

    while dist > cnt*(cnt+1):
        cnt += 1

    if dist <= cnt**2:
        print(2*cnt-1)
    else:
        print(2*cnt)
