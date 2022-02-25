N = input()

num = 0
digit = 0
# 이진수 => 십진수 변환
for i in N[::-1]:
    num += int(i)*(2**digit)
    digit += 1

num *= 17 #17배
res = ''
# 십진수 => 이진수 변환
while num != 0:
    res = str(num%2) + res
    num //= 2
print(res)
