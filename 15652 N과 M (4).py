from itertools import combinations_with_replacement

N, M = map(int, input().split())
case = combinations_with_replacement(range(1, N+1), M)

for i in case:
    for j in i:
        print(j, end=" ")
    print()
