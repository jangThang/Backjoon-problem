# 입력
n, h, v = map(int, input().split())

# 가장 큰 것 찾기
res = max(h*v, (n-h)*v, h*(n-v), (n-h)*(n-v))
print(res * 4)
