#입력
N = int(input()) #목표 채널
M = int(input())
broken = []
if M:
    broken = list(input().split()) #고장난 숫자버튼

res = abs(100 - N) #100번에서 +/-로만 이동할 때, 필요한 버튼 수
for channel in range(1000001):
    #고장난 버튼이 포함되어있으면 넘어가기
    for i in str(channel):
        if i in broken:
            break

    #고장난 버튼이 없으면 계산
    #[채널이동에 필요한 버튼 횟수]와 [+/-버튼 누를 횟수]를 계산해서 비교
    else:
        res = min(res, len(str(channel)) + abs(N - channel))
print(res)
