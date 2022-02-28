#입력
A, B = input().split()

#각 자릿수 곱하고 더하기
res = 0
for i in A:
    for j in B:
        res += int(i) * int(j)
print(res)
