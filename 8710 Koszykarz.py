# 입력
k, w, m = map(int, input().split())

# 계산
res = (w - k)//m
if (w-k) % m != 0:
    res += 1
print(res)
