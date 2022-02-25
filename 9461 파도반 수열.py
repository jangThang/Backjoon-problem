import sys
input = sys.stdin.readline

T = int(input())
cache = [1, 1, 1, 2, 2, 3] #파도반 수열

def sail(n):
    #n이 cache에 없을 경우, n까지 수열 구함
    while n > len(cache)-1:
        cache.append(cache[len(cache)-5]+cache[len(cache)-1])

    #n이 cache에 있을 경우
    return cache[n-1]

for _ in range(T):
    N = int(input())
    print(sail(N))
