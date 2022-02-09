import sys
input = sys.stdin.readline

# 에라토스 테네스의 체
def isPrime(n):
    primeList = [True] * n
    for i in range(2, int(n ** 0.5) + 1):
        if primeList[i]: # i가 소수라면
            for j in range(2 * i, n, i):  # 2i부터 n까지 i의 배수들은 False
                primeList[j] = False
    return [i for i in range(2, n) if primeList[i] == True] # 소수인 것만 리턴


while True:
    n = int(input())
    if n == 0: # 0 입력 시 종료
        break
    primeList = isPrime(2*n+1) # 2n까지 소수 판별
    cnt = 0
    for i in primeList:
        if i > n:
            cnt += 1 # n보다 큰 소수의 개수 세기
    print(cnt)
