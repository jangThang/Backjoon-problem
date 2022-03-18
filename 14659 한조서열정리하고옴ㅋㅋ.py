# 입력
N = int(input())
high = list(map(int, input().split()))

# 그리디
high_max = 0
cnt = 0
res = 0
for i in high:
    # 더 높은 봉우리 만나면 갱신
    if i > high_max:
        high_max = i
        cnt = 0

    # 더 낮은 봉우리면 Kill
    if i < high_max:
        cnt += 1
    res = max(res, cnt)
print(res)
