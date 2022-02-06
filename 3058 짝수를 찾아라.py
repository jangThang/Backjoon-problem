T = int(input())
for i in range(T):
    numlist = list(map(int, input().split()))
    sum = 0
    min = 101 # 입력범위 1~100
    for i in numlist:
        if i % 2 == 0:
            sum += i
            if min > i:
                min = i
    print(sum, min)
