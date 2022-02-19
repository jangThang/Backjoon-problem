meatT = int(input()) # 고기 온도
targetT = int(input()) # 목표 온도
subZero = int(input()) # 영하일 때 1도 올리는 데 필요한 시간
defrost = int(input()) # 해동 시간
uponZero = int(input()) # 영상일 때 1도 올리는 데 필요한 시간

time = 0
while meatT != targetT: # 목표온도에 도달할 때까지 반복
    # 고기 온도가 영하일 때
    if meatT < 0:
        time += subZero
        meatT += 1

    # 고기 온도가 0도일 때
    elif meatT == 0:
        time += defrost #해동
        time += uponZero #0도에서 1도 올리는데 필요한 시간
        meatT += 1

    # 고기 온도가 영상일 때
    else:
        time += uponZero
        meatT += 1
print(time)
