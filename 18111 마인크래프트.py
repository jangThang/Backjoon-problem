N, M, B = map(int, input().split())
block = []
for i in range(N):
    block.extend(map(int, input().split()))

res = [] # 결과값을 저장할 리스트
#가장 낮은 높이부터 가장 높은 높이까지 탐색
for h in range(min(block), max(block)+1):
    inventory = B #인벤토리 블록 수
    time = 0 #필요한 시간
    for i in block:
        if i > h: #지정 높이보다 큼
            time += 2*(i-h)
            inventory += i-h

        elif i < h: #지정 높이보다 작음
            time += h-i
            inventory -= h-i

    # 블록이 부족할 경우, 더 이상 높힐 수 없음
    if inventory < 0:
        break
    else:
        res.append([time, h])

res.sort(key=lambda x: (x[0], -x[1])) #시간은 작을수록, 높이는 높을수록 좋음
print(res[0][0], res[0][1])
