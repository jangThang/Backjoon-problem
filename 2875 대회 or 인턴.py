N, M, K = map(int, input().split())

team = 0
while True:
    N -= 2
    M -= 1
    # 남은 여자 혹은 남자가 0명 미만이거나, 인턴십 보낼 학생이 모자를 때
    if N < 0 or M < 0 or N+M < K:
        break
    team += 1
print(team)
