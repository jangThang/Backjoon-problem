import sys
input = sys.stdin.readline

N = int(input()) #Pn
M = int(input()) #S의 길이
S = input().rstrip()

res = 0 #Pn이 나온 횟수
cnt = 0 #IOI카운트
for s in S:
    #IOI카운트에서 O는 짝수번째여야 함
    if s == 'O' and cnt%2 == 1:
        cnt += 1

    #IOI카운트에서 I는 홀수번째여야 함
    elif s == 'I' and cnt%2 == 0:
        cnt += 1

    #그 외의 I라면 맨 처음 I시작
    elif s == 'I':
        cnt = 1

    #그 외라면 카운트 아님
    else:
        cnt = 0

    #Pn만큼 IOI카운트세면 결과에 +1
    if cnt >= 1+2*N and cnt%2 == 1:
        res += 1
print(res)
