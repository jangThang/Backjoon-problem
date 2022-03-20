import sys
input = sys.stdin.readline

# 입력
N, K = map(int, input().split())
item = []
for _ in range(N):
    item.append(list(map(int, input().split())))

# DP
cache = [[0]*(K+1) for _ in range(N+1)]

# 아이템 하나씩 넣고 빼며 가치 비교
for idx, thing in enumerate(item, 1):
    weight, value = thing
    # 1부터 K까지 무게를 늘려가며 가치의 최댓값 구하기
    for i in range(1, K + 1):
        # 베낭에 아이템을 넣을 수 있으면 비교 후 갱신
        if i >= weight:
            # [해당 아이템 이전의 가치의 최댓값]과 [해당 아이템을 추가한 후의 가치] 비교
            cache[idx][i] = max(cache[idx-1][i], cache[idx-1][i-weight] + value)
        # 아이템을 추가할 수 없으면 이전 가치의 최댓값 그대로
        else:
            cache[idx][i] = cache[idx-1][i]
print(cache[N][K])
