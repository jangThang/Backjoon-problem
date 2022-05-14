import sys
input = sys.stdin.readline

# 입력
numlist = list(map(int, input().split()))

# 약수가 3개 이상인 수 찾기
num = 2
while True:
    cnt = 0
    for i in numlist:
        if num % i == 0:
            cnt += 1

    if cnt >= 3:
        print(num)
        break
    num += 1
