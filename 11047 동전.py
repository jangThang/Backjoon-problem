N, K = map(int, input().split())
coin = []
for i in range(N):
    coin.append(int(input()))

res = 0
for c in coin[::-1]:
    if c <= K: # 남은 돈이 동전 단위보다 같거나 큰 경우 (거슬러줄 수 있는 경우) 
        res += K//c
        K %= c
print(res)
