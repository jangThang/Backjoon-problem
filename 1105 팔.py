# 입력
L, R = input().split()

# 같은 자리에 있는 8 찾기
res = 0
if len(L) == len(R):
    for i, j in zip(L, R):
        if i == j == '8':
            res += 1
        elif i != j:
            break
print(res)
