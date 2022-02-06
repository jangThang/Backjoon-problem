T = int(input())
for i in range(T):
    N = int(input())
    maxL = 0
    maxS = ''
    for j in range(N):
        S, L = input().split()
        if maxL < int(L):
            maxL = int(L)
            maxS = S
    print(maxS)
