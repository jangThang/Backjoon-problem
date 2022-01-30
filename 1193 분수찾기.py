X = int(input()) #입력

cnt = 0 # count
diagonal = 0 # 대각선 번호
n = 0 # 대각선 중 n번째 수

# X가 속한 대각선 찾기
for i in range(1,X+1):
    cnt += i
    if cnt >= X:
        diagonal = i # i번째 대각선 중
        n = X-(cnt-i) # n번째 수
        break

        
# 순서 찾기
numerator = 0 # 분자
denominator = 0 # 분모

# 홀수 대각선일 때 (우상향)
if diagonal % 2 == 1:
    numerator = diagonal + 1
    denominator = 0
    
    for j in range(n):
        numerator -= 1
        denominator += 1

# 짝수 대각선일 때 (좌하향)
elif diagonal % 2 == 0:
    numerator = 0
    denominator = diagonal + 1
    
    for j in range(n):
        denominator -= 1
        numerator += 1

# 출력
print(f'{numerator}/{denominator}')
