N = int(input())
res = 0 # 걸린 시간
cnt = 1 # 노래 카운트
while N > 0:
    if cnt > N:
        cnt = 1
    N -= cnt
    cnt += 1
    res += 1
print(res)
