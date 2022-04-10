import sys
input = sys.stdin.readline

cache = [[[0]*21 for _ in range(21)] for _ in range(21)]
def w(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return 1
    elif a > 20 or b > 20 or c > 20:
        return w(20, 20, 20)
    elif cache[a][b][c]:  # 캐시값이 있으면, 캐시값 반환
        return cache[a][b][c]
    elif a < b < c:
        cache[a][b][c] = w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c)
        return cache[a][b][c]
    else:
        cache[a][b][c] = w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)
        return cache[a][b][c]

while True:
    a, b, c = map(int, input().split())
    if a == b == c == -1:
        break
    print(f'w({a}, {b}, {c}) = {w(a,b,c)}')
