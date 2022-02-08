M = int(input())
N = int(input())

def isPrime(n):
    if n == 1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

prime = []
for i in range(M, N+1):
    if isPrime(i):
        prime.append(i)
if len(prime) == 0:
    print(-1)
else:
    print(sum(prime))
    print(min(prime))
