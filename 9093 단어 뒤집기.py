import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    s = list(input().rstrip().split())
    for word in s:
        print(word[::-1], end=" ")
    print()
