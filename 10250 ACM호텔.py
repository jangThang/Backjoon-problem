import sys
input = sys.stdin.readline

T = int(input())
for i in range(T):
    H, W, N = map(int, input().split())
    cnt = 1
    room = ''
    for num in range(1, W+1):
        for floor in range(1, H+1):
            if cnt == N:
                room = str(floor) + f"{num:02d}" #H,W는 1부터 99까지
                cnt += 1
                break
            cnt += 1
        if cnt == N+1:
            break
    print(room)
