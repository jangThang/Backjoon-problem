A, B = map(int, input().split())

cnt = 0
res = 0
for i in range(1000):
    for j in range(i):
        cnt += 1
        if cnt >= A:
            res += i
        if cnt > B-1:
            break
    if cnt > B-1:
        break
print(res)
