import sys
input = sys.stdin.readline

# 입력
n = int(input())
tips = []
for _ in range(n):
    tips.append(int(input()))

# 내림차순 정렬
tips.sort(reverse=True)

# 팀 많이 주는 사람부터 주문 받기
res = 0
for idx, tip in enumerate(tips, 1):
    # 팁이 음수이면 0
    if tip + (1 - idx) < 0:
        pass
    else:
        res += tip + (1 - idx)
print(res)
