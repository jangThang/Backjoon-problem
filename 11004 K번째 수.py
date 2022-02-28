import sys
input = sys.stdin.readline

N, K = map(int, input().split())
numlist = list(map(int, input().split()))
numlist.sort()
print(numlist[K-1])
