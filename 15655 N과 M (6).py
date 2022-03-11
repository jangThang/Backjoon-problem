from itertools import combinations

N, M = map(int, input().split())
numlist = list(map(int, input().split()))
case = combinations(sorted(numlist), M)

for i in case:
    for j in i:
        print(j, end=" ")
    print()
