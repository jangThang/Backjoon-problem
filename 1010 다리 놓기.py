from math import comb
import sys
input = sys.stdin.readline

#입력
T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    print(comb(M, N))
