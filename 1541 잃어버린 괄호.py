import sys
input = sys.stdin.readline

term = list(input().rstrip())
res = 0
num = ''
minus = False

# minus가 1번만 나와도, 그 다음부터는 음수
for i in term:
    # minus가 한 번도 안 나왔을 때
    if not minus:
        if i == '-':
            minus = True
            res += int(num)
            num = ''
        elif i == '+':
            res += int(num)
            num = ''
        else:
            num += i

    # minus가 한 번 이상 나왔을 경우
    elif minus:
        if i == '-' or i == '+':
            res -= int(num)
            num = ''
        else:
            num += i

if minus:
    res -= int(num)
else:
    res += int(num)
print(res)
