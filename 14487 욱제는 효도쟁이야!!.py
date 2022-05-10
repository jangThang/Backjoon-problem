import sys
input = sys.stdin.readline

# 입력
n = int(input())  # 마을의 수
town = list(map(int, input().split()))

# 그리디 알고리즘
print(sum(town) - max(town))
