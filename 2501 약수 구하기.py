N, K = map(int, input().split())

cnt = 0
for divide in range(1,N+1):
    # 약수일 경우, cnt + 1
    if N % divide == 0:
        cnt += 1

    # k번째 약수일 경우, 출력
    if cnt == K:
        print(divide)
        break
# k번째 약수 없음
else:
    print(0)
