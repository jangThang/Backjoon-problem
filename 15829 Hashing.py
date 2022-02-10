L = int(input()) #문자길이
string = input() #문자열

r = 31
M = 1234567891

sum = 0
cnt = 0
for s in string:
    i = ord(s)-96
    sum += (i * r**cnt) % M # 31의 제곱이 M을 넘어설 수 있으므로 매번 나눠줌
    cnt += 1

sum %= M # 합이 M을 넘어설 수 있으므로 다시 나눠줌
print(sum)
