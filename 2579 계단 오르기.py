import sys
input = sys.stdin.readline

n = int(input())
stairs = []
for _ in range(n):
    stairs.append(int(input()))

if n == 1:
    print(stairs[0])
elif n == 2:
    print(stairs[0]+stairs[1])
else:
    cache = [stairs[0], stairs[0]+stairs[1], max(stairs[0]+stairs[2], stairs[1]+stairs[2])]
    for i in range(3, n):
        cache.append(max(cache[i-2]+stairs[i], cache[i-3]+stairs[i-1]+stairs[i]))
    print(cache[n-1])
