from itertools import combinations

N, M = map(int, input().split())
case = combinations(range(1, N+1), M)

for i in case:
    for j in i:
        print(j, end=" ")
    print()
