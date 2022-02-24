import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    Y, K = 0, 0
    for i in range(9):
        a, b = map(int, input().split())
        Y += a
        K += b
    if Y > K:
        print("Yonsei")
    elif Y < K:
        print("Korea")
    else:
        print("Draw")
