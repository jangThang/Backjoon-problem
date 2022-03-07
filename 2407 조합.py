#from math import comb
#n, m = map(int, input().split())
#print(comb(n, m))


n, m = list(map(int, input().split()))
cache = [[-1 for j in range(m + 1)] for i in range(n + 1)]

#동적계획법
def nCr(n, r):
    #조합값이 1인 경우
    if n == 1:
        return 1
    elif n == r or r == 0:
        return 1

    #직접 계산
    else:
        if cache[n][r] == -1:
            cache[n][r] = nCr(n - 1, r) + nCr(n - 1, r - 1)
        return cache[n][r]

#출력
print(nCr(n, m))
