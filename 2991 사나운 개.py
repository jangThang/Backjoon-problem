import sys
input = sys.stdin.readline

# 입력
A, B, C, D = map(int, input().split()) # A C분 공격, B D분 휴식
P, M, N = map(int, input().split()) # 우체부/우유배달원/신문배달원 도착

# 출력
for t in [P, M, N]:
    cnt = 0  # 물리는 횟수
    if 0 < t % (A+B) <= A:
        cnt += 1

    if 0 < t % (C+D) <= C:
        cnt += 1
    print(cnt)
