plate = input()
res = 0
pre = ''
for i in plate:
    # 같은 방향으로 쌓임
    if pre == i:
        res += 5
    else:
        res += 10
    pre = i
print(res)
