n = int(input())
cache = [0, 1] #1은 1

for i in range(2, n+1):
    squareN = 5 #최대 4개
    j = 1

    # j^2이 i보다 커지면 종료
    while j**2 <= i:
        # j**2를 추가했을 때, 제곱수가 작아지면 대체
        squareN = min(squareN, cache[i - j**2])
        j += 1
    # i일 때의 제곱수 메모
    cache.append(squareN+1)
print(cache[n])
