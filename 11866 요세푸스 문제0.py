N, K = map(int, input().split())
numlist = list(range(1, N+1))

res = [] #요세푸스
idx = 0 #인덱스
for t in range(N):
    idx += K - 1
    if idx >= len(numlist):  # 한바퀴를 돌면, 나머지부터 다시 시작
        idx = idx % len(numlist)

    res.append(str(numlist.pop(idx)))
    s = ", ".join(res)
print(f"<{s}>")
