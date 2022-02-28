import sys
input = sys.stdin.readline

#입력
N = int(input())
room = [] #방 구조 저장
row = 0 #가로
col = 0 #세로
for c in range(N):
    tmp = input().rstrip()
    cnt = 0 # .개수
    for i in tmp:
        if i == '.':
            cnt += 1
        #X를 만났을 때, 앞서 .이 2개 이상이었으면 자리 추가
        elif i == 'X':
            if cnt >= 2:
                row += 1
            cnt = 0
    #..이상임에도 벽을 만나지 못한채 끝났으면 자리 추가
    if cnt >= 2:
        row += 1
    room.append(tmp)

#세로로 누울자리 찾기
for i in range(N):
    cnt = 0 # .개수
    for j in range(N):
        if room[j][i] == '.':
            cnt += 1
        # X를 만났을 때, 앞서 .이 2개 이상이었으면 자리 추가
        elif room[j][i] == 'X':
            if cnt >= 2:
                col += 1
            cnt = 0
    # ..이상임에도 벽을 만나지 못한채 끝났으면 자리 추가
    if cnt >= 2:
        col += 1
#출력
print(row, col)
