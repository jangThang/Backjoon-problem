n = int(input())

square = [x**2 for x in range(1, 318)] # 제곱수
cache = [x for x in range(n+1)] # 캐싱
for i in range(n+1):
    for s in square:
        # 제곱수가 i보다 크면 break
        if s > i:
            break
        # 해당 제곱수로 더하는 게 더 작으면 갱신
        cache[i] = min(cache[i], cache[i-s]+1)
print(cache[n])
