# 입력
N = int(input())
store = list(map(int, input().split()))

# 우유 먹방
order = 0
res = 0 # 먹은 우유 갯수
for milk in store:
    if milk == order:
        order = (order+1) % 3
        res += 1
print(res)
