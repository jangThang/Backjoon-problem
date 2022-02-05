import sys
input = sys.stdin.readline


T = int(input())
for i in range(T):
    s = int(input()) # 자동차 가격
    n = int(input())
    for j in range(n):
        p, q = map(int, input().split())
        s += p*q
    print(s)
