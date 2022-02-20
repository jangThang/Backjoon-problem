N = int(input())
cache = [0]*(N+1) #메모이제이션

for i in range(2, N+1):
    # 1을 뺐을 때
    cache[i] = cache[i-1] + 1

    # 2로 나누었을 때
    if i % 2 == 0:
        cache[i] = min(cache[i], cache[i//2]+1)

    # 3으로 나누었을 때
    if i % 3 == 0:
        cache[i] = min(cache[i], cache[i//3]+1)
print(cache[N])
