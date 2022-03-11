from itertools import product

N, M = map(int, input().split())
numlist = list(map(int, input().split()))
case = product(sorted(numlist), repeat=M)

for i in case:
    for j in i:
        print(j, end=" ")
    print()
