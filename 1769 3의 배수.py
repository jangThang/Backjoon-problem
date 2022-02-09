n = input()
cnt = 0 #횟수
# 1의 자리가 될 때까지 반복
while len(n) > 1:
    cnt += 1
    # 각 자릿수의 합
    sum = 0
    for i in n:
        sum += int(i)
    n = str(sum)

print(cnt)
if int(n) % 3 == 0:
    print("YES")
else:
    print("NO")
