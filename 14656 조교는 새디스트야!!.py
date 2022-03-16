import sys
input = sys.stdin.readline

# 입력
n = int(input())
numlist = list(map(int, input().split()))

# 순서 안 맞는 사람 골라내기
baseball = 0 # 엉덩이가 야구공이 될 사람 수
for idx, num in enumerate(numlist, 1):
    # 순서에 맞지 않으면 엉덩이가 야구공이 되도록 맞음
    if idx != num:
        baseball += 1
print(baseball)
