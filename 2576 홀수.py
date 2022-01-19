min = 100
sum = 0
for i in range(7):
    num = int(input())
    if num % 2 == 1:
        sum += num
        if min > num:
            min = num
if min == 100:
    print(-1)
else:
    print(sum)
    print(min)
