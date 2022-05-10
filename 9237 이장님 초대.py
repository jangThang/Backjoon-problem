import sys
input = sys.stdin.readline

# 입력
n = int(input())  # 묘목 개수
tree = list(map(int, input().split()))

# 그리디
tree.sort(reverse=True)  # 걸리는 시간이 큰 순서대로 정렬
res = 0  # 모두 자라는데 걸리는 시간
for day, t in enumerate(tree, 2):
    res = max(res, t+day)
print(res)
