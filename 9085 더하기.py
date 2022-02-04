import sys
input = sys.stdin.readline

T = int(input())
for i in range(T):
    N = int(input())
    numlist = list(map(int, input().split()))
    print(sum(numlist))
