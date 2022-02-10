import sys
input = sys.stdin.readline

N, M = map(int, input().split())
tree = list(map(int, input().split()))

start, end = 1, max(tree) # 나무 높이의 최소, 최댓값
# 나무길이를 찾는 이진 탐색
while start <= end:
    mid = (start+end)//2
    wood = 0 #나무토막 총합
    for i in tree:
        if i > mid: # mid 높이보다 클 때만 잘림
            wood += (i-mid) # mid 높이로 잘린 나무토막 길이

    # M보다 나무토막이 많을 경우, 더 길게 자르기
    if wood >= M:
        start = mid + 1
    else: # 나무토막이 부족하면, 더 짧게 자르기
        end = mid - 1
print(end)
