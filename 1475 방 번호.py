N = input()

number = [0]*10 #0부터 9까지
sixNine = 0 #6과 9는 따로 저장
for s in N:
    if s == '6' or s == '9':
        sixNine += 1
    else:
        number[int(s)] += 1

# 6과 9의 합계가 짝수면 2로 나누고
if sixNine % 2 == 0:
    sixNine //= 2
# 홀수면 2로 나눈 다음 1세트 추가
else:
    sixNine = sixNine//2 + 1
    
# 6과 9가 필요한 세트 수와, 그 외 숫자들이 필요한 세트 수를 비교
print(max(max(number), sixNine))
