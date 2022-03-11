from itertools import combinations_with_replacement

N, M = map(int, input().split())
numlist = list(map(int, input().split()))
case = combinations_with_replacement(sorted(numlist), M)

for i in case:
    for j in i:
        print(j, end=" ")
    print()
