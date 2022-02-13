N = int(input())

def calFibonacci(n):
    cache = [0, 1] #fibo(0) = 0, fibo(1) = 1
    for i in range(2, n+1):
        cache.append(cache[i-1] + cache[i-2])
    return cache

fibo = calFibonacci(N)
print(fibo[N])
