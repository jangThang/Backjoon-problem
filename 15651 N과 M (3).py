from itertools import product

N, M = map(int, input().split())
case = product(range(1, N+1), repeat=M)

for i in case:
    for j in i:
        print(j, end=" ")
    print()
