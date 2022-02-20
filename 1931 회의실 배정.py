import sys
input = sys.stdin.readline

N = int(input())
room = []
for _ in range(N):
    start, end = map(int, input().split())
    room.append([start, end])

#끝나는 시간이 빠른 순서대로 정렬
room.sort(key=lambda x: (x[1], x[0]))

cnt = 0 #회의 개수
time = 0 #시간
for i in room:
    # 시간이 시작시간 이전일 경우, 회의 시작
    if time <= i[0]:
        cnt += 1
        time = i[1] #회의가 끝나는 시간으로 설정
print(cnt)
