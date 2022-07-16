# 입력
numlist = list(map(int, input().split()))
res = 0
for i in numlist:
    if i > 0:
        res += 1
print(res)
