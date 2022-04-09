import sys
input = sys.stdin.readline

# 입력
n = int(input())
level = []
for _ in range(n):
    level.append(int(input()))

# 그리디 알고리즘
cnt = 0  # 레벨을 감소시키는 횟수
post = level[-1] + 1  # 차후 레벨의 경험지
for i in level[::-1]:
    # 차후 레벨보다 경험지가 높다면 낮춤
    if post <= i:
        cnt += i - post + 1
        post -= 1

    # 차후 레벨보다 경험지가 낮다면 넘어감
    else:
        post = i
print(cnt)
