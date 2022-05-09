import sys
input = sys.stdin.readline

# 반대로 출력
N, M = map(int, input().split())
for _ in range(N):
    print(input().rstrip()[::-1])
