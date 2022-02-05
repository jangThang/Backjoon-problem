import sys
input = sys.stdin.readline

while True:
    m, w = map(int, input().split())
    if m == 0 and w == 0:
        break
    print(m+w)
