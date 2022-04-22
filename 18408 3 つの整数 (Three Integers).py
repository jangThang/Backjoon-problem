# 입력
A, B, C = input().split()

# 1, 2 개수 세기
one = 0
two = 0

for i in [A, B, C]:
    if i == '1':
        one += 1
    else:
        two += 1

# 출력
if one > two:
    print(1)
else:
    print(2)
