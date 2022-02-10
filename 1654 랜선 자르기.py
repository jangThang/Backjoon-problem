import sys
input = sys.stdin.readline

K, N = map(int, input().split())
lanCable = []
for i in range(K):
    lanCable.append(int(input()))

start, end = 1, max(lanCable) # 랜선 길이의 최소, 최댓값
# 랜선길이를 찾는 이진 탐색
while start <= end:
    mid = (start+end)//2
    lan = 0 #랜선 수
    for i in lanCable:
        lan += i // mid # 중간 길이로 분할된 랜선 수

    # N보다 랜선 갯수가 많을 경우, 더 길게 자르기
    if lan >= N:
        start = mid + 1
    else: # 랜선 갯수가 적으며, 더 짧게 자르기
        end = mid - 1
print(end)
