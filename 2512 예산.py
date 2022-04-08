import sys
input = sys.stdin.readline

# 입력
N = int(input())
budget = list(map(int, input().split()))
total_budget = int(input())

# 이진탐색
budget.sort()  # 오름차순 정렬
start, end = 1, budget[-1]  # 예산의 최소, 최댓값
while start <= end:
    mid = (start+end)//2  # 예산 제한
    cost = 0  # 비용
    for i in budget:
        if i > mid:  # 예산보다 더 많으면 잘림
            cost += mid
        else:
            cost += i

    # 총 예산보다 크면, 최대 예산액을 줄임
    if cost > total_budget:
        end = mid - 1

    # 총 예산이 남으면, 최대 예산액을 늘림
    else:
        start = mid + 1
print(end)
