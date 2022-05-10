import sys
input = sys.stdin.readline

# 입력
n, l = map(int, input().split())  # 과일의 개수, 초기 길이
height = list(map(int, input().split()))

# 그리디 (작은 과일부터 먹기)
height.sort()
for h in height:
    if h <= l:
        l += 1
    else:
        break
print(l)
