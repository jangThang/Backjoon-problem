# 입력
N = int(input())
numlist = list(map(int, input().split()))

# 오르막길
pre = numlist[0]
high = 0
res = 0
for i in numlist:
    # 이전 높이보다 크면 오르막길
    if pre < i:
        high += i - pre

    # 작거나 같으면 다시 리셋
    else:
        res = max(res, high)
        high = 0
    pre = i

# 출력
print(max(high, res))
