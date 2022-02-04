N = input()
digit = len(N) #자릿수

res = 0 # 결과값
# 이전 자릿수까지의 합
for i in range(digit):
    # 해당 자릿수의 숫자 개수 * 자릿수
    res += (9 * (10**(i-1))) * (i)

# 현재 자릿수의 합
# N의 자릿수에서 N까지의 숫자 개수 * N의 자릿수
res += (int(N) - 10**(digit-1) + 1) * digit
print(int(res))
