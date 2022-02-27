N = input()

#모든 자릿수를 더한 수가 3의 배수이면서 일의 자리가 0
digit_sum = 0
zero = False
for i in N:
    digit_sum += int(i)
    if i == '0':
        zero = True

#3의 배수가 맞다면
if digit_sum % 3 == 0 and zero:
    print("".join(sorted(list(N), reverse=True)))

#3의 배수가 아니라면
else:
    print(-1)
