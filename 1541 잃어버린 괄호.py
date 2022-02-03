import sys
input = sys.stdin.readline

term = list(input().rstrip())
res = 0
num = ''
minus = False

# minus가 1번만 나와도, 그 다음부터는 음수
for i in term:
    if i == '-' and minus == True:
        minus = True
        res -= int(num)
        num = ''
    elif i == '-' and minus == False:
        minus = True
        res += int(num)
        num = ''
    elif i == '+' and minus == False:
        res += int(num)
        num = ''
    elif i == '+' and minus == True:
        res -= int(num)
        num = ''
    else:
        num += i
if minus:
    res -= int(num)
else:
    res += int(num)
print(res)
