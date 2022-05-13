import sys
input = sys.stdin.readline

# 입력
N = int(input())
cow = []
for _ in range(N):
    cow.append(list(map(int, input().split())))  # start, duration

# 정렬
cow.sort()

# 시간 계산
res = 0
for start, duration in cow:
    # 도착시간까지 시간이 남았으면, 기다렸다가 입장
    if res < start:
        res = start+duration

    # 검문 중인 소가 있다면 기다렸다가 바로 입장
    else:
        res += duration
print(res)
